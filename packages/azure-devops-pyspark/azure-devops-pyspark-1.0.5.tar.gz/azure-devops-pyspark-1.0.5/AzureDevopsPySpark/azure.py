from __future__ import annotations
from base64 import b64encode
from pyspark.sql.types import DateType, IntegerType, StringType, StructField, StructType
from pyspark.pandas.frame import DataFrame
from pyspark.sql import SparkSession
from typing import List
from requests import get, post
from copy import deepcopy
from array import array
from AzureDevopsPySpark.endpoints import *
from AzureDevopsPySpark.process import *
from AzureDevopsPySpark.schemas import *


class Azure:
    def __init__(self, organization: str, project: str, token: str):
        self._organization = organization
        self._project = project
        self._token = b64encode(f":{token}".encode()).decode()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self._token}",
            "Proxy-Authorization": f"Basic {self._token}",
        }
        self._process = None
        self._columns = {
            "System.AreaPath": StructField("AreaPath", StringType(), True),
            "System.IterationPath": StructField("IterationPath", StringType(), True),
            "System.WorkItemType": StructField("WorkItemType", StringType(), True),
            "System.Id": StructField("Id", IntegerType(), True),
            "System.Parent": StructField("Parent", IntegerType(), True),
            "System.State": StructField("State", StringType(), True),
            "System.AssignedTo": StructField("AssignedTo", StringType(), True),
            "System.CreatedDate": StructField("CreatedDate", DateType(), False),
            "System.ChangedDate": StructField("ChangedDate", DateType(), True),
            "System.Title": StructField("Title", StringType(), True),
            "System.Tags": StructField("Tags", StringType(), True),
            "System.BoardColumn": StructField("BoardColumn", StringType(), True),
            "System.BoardColumnDone": StructField(
                "BoardColumnDone", StringType(), True
            ),
            "System.ChangedBy": StructField("ChangedBy", StringType(), True),
            "Microsoft.VSTS.Common.ActivatedDate": StructField(
                "ActivatedDate", DateType(), True
            ),
        }
        self._fields_displayname = [
            "System.AssignedTo",
            "System.ChangedBy",
            "Microsoft.VSTS.Common.ActivatedBy",
            "Microsoft.VSTS.Common.ClosedBy",
        ]
        self.spark = SparkSession.builder.appName("AzureDevopsSpark").getOrCreate()
        self.__validade_status()

    def __repr__(self):
        return f"Organization: {self._organization}\nProject: {self._project}\nToken base64: {self._token}\n{self.headers}"

    def filter_columns(self, only: List[str]) -> List[str, StructField]:
        """
        `Mapped columns that are not in the list passed as an argument will be excluded.`

        Ex:
            filter_columns( ['System.AreaPath', 'System.Id'] ) -> Only System.AreaPath and System.Id will be returned.
        """
        backup_keys = deepcopy(list(self._columns.keys()))
        return [self._columns.pop(item) for item in backup_keys if item not in only]

    def backlog(self) -> DataFrame:
        """
        Returns all backlog work items within a project.
        """
        items = []
        squads = [item["Squad"] for item in self.teams().collect()]
        for squad in squads:
            endpoint = Endpoint.team_backlog(self._organization, self._project, squad)
            response = self.__get(endpoint)
            if response.status_code == 200 and response.json()["value"]:
                levels = [
                    {item["name"]: item["id"]} for item in response.json()["value"]
                ]
                for item in levels:
                    for level, id_level in item.items():
                        endp_items = Endpoint.backlog_items(
                            self._organization, self._project, squad, id_level
                        )
                        response = self.__get(endp_items).json()
                        if response["workItems"]:
                            id_list = array(
                                "I",
                                [
                                    item["target"]["id"]
                                    for item in response["workItems"]
                                ],
                            )
                            original = self.__get_items(id_list)
                            for item in original:
                                item["Backlog"] = level
                            items.extend(original)
        self._columns["Backlog"] = StructField("Backlog", StringType(), True)
        SCHEMA_ITEMS = StructType([column for column in self._columns.values()])

        data = [tuple(item.values()) for item in items]
        return self.spark.createDataFrame(data, schema=SCHEMA_ITEMS)

    def teams(
        self,
        only: List[str] = None,
        exclude: List[str] = None,
        params_endpoint: str = None,
    ) -> DataFrame:
        """
        `Returns all teams registered in the project.`

        :param only: teams(only = ['Squad 1', 'Squad 2']) -> Only Squad 1 and Squad 2 will be returned.
        :param exclude: teams(exclude = ['Squad 3']) -> Squad 3 will not be returned.
        :param only and exclude:  teams(['Squad 1', 'Squad 2', ...], ['Squad 3']) -> The squads in only will be returned and Squad 3 will not be returned.
        """
        endpoint = Endpoint.teams(self._organization, params_endpoint)
        response = self.__get(endpoint).json()
        clean_response = Process.teams(response)
        teams = (
            [item for item in clean_response if item["Squad"] in only]
            if only
            else clean_response
        )
        remove = (
            [teams.remove(item) for item in teams if item["Squad"] in exclude]
            if exclude
            else None
        )

        data = [tuple(item.values()) for item in teams]
        return self.spark.createDataFrame(data, schema=SCHEMA_ALL_TEAMS)

    def iterations(
        self,
        only: List[str] = None,
        exclude: List[str] = None,
        params_endpoint: str = None,
    ) -> DataFrame:
        """
        `Returns all iterations in the project.`

        :param only: iterations(only = ['iterations 1', 'iterations 2']) -> Only iterations 1 and iterations 2 will be returned.
        :param exclude: iterations(exclude = ['iterations 3']) -> iterations 3 will not be returned.
        :param only and exclude:  iterations(['iterations 1', 'iterations 2', ...], ['iterations 3']) -> The iterations in only will be returned and iterations 3 will not be returned.
        """
        teams = (
            [item["Squad"] for item in self.teams().collect()] if not only else only
        )
        remove = [teams.remove(squad) for squad in exclude] if exclude else None
        iteration_matrix = []
        for squad in teams:
            endpoint = Endpoint.team_iterations(
                self._organization, self._project, squad, params_endpoint
            )
            response = self.__get(endpoint)
            if response.status_code == 200:
                clean_response = Process.team_interation(response.json(), squad)
                iteration_matrix.extend(clean_response)
            else:
                print(
                    f"{squad}: does not exist, or you do not have permission to access it."
                )

        data = [tuple(item.values()) for item in iteration_matrix]
        return self.spark.createDataFrame(data, schema=SCHEMA_ITERATIONS)

    def members(
        self,
        only: List[str] = None,
        exclude: List[str] = None,
        params_endpoint: str = None,
    ) -> DataFrame:
        """
        `Returns all members in the project.`

        :param only: members(only = ['member 1', 'member 2']) -> Only member 1 and member 2 will be returned.
        :param exclude: members(exclude = ['member 3']) -> member 3 will not be returned.
        :param only and exclude:  members(['member 1', 'member 2', ...], ['member 3']) -> The members in only will be returned and member 3 will not be returned.
        """
        teams = (
            self.teams().collect()
            if not only
            else [{"Squad": item} for item in only]
        )
        remove = (
            [teams.remove(item) for item in teams if item["Squad"] in exclude]
            if exclude
            else None
        )
        members_matrix = []

        for squad in teams:
            url = Endpoint.members(
                self._organization, self._project, squad["Squad"], params_endpoint
            )
            response = self.__get(url)
            if response.status_code == 200:
                clear_response = Process.members(response.json(), squad["Squad"])
                members_matrix.append(clear_response)

        members = [member for squad in members_matrix for member in squad]

        data = [tuple(item.values()) for item in members]
        return self.spark.createDataFrame(data, schema=SCHEMA_ALL_MEMBERS)

    def items(self, query: str = None, params_endpoint: str = None) -> DataFrame:
        """
            `Returns all work items in the project. It is possible to filter by SQL in the query parameter set to None`.
            :param query: SQL statements after FROM WorkItems. Ex: [System.WorkItemType] = 'Task' AND [System.AssignedTo] = 'Guilherme Silva'\
                 \n Returns all tasks associated with Guilherme Silva.
        """
        matrix = []
        start = 0
        stop = 19999
        while True:
            sql = f"Select [System.Id] FROM WorkItems WHERE [System.Id] >= {start} AND [System.Id] <= {stop}"
            data = {"query": f"{sql} AND {query}"} if query else {"query": sql}
            endpoint = Endpoint.wiql(self._organization, self._project, params_endpoint)
            response = post(endpoint, headers=self.headers, json=data).json()
            if response["workItems"]:
                id_list = array(
                    "I", sorted({item["id"] for item in response["workItems"]})
                )
                items = self.__get_items(id_list)
                matrix.extend(items)
                start = stop + 1
                stop += 19999
            else:
                break

        SCHEMA_ITEMS = StructType([column for column in self._columns.values()])
        data = [tuple(item.values()) for item in matrix]
        return self.spark.createDataFrame(data, schema=SCHEMA_ITEMS)

    def tags(self) -> DataFrame:
        """
        `Returns all tags registered in the project.`
        """
        endpoint = Endpoint.tags(self._organization, self._project)
        response = self.__get(endpoint).json()
        clear_response = Process.tags(response)
        data = [tuple(item.values()) for item in clear_response]
        return self.spark.createDataFrame(data, schema=SCHEMA_TAGS)

    def __mapping_columns(self) -> bool:
        """
        `Maps all columns in the project.`
        """
        try:
            all_process = Endpoint.all_process(self._organization)
            resp_all_process = self.__get(all_process)
            clean_all_process = Process.all_process(
                resp_all_process.json()
            )  # [{'id':..., 'name':...}]
            for process in clean_all_process:
                project_ref = Endpoint.project_reference(
                    self._organization, process["id"]
                )
                resp_project = self.__get(project_ref).json()
                if "projects" in resp_project:
                    projects = resp_project["projects"]
                    for project in projects:
                        if project["name"].replace(" ", "%20") == self._project:
                            self._process = process["id"]
                            break
            list_work_items = Endpoint.list_work_item_types(
                self._organization, self._process
            )
            resp_list = self.__get(list_work_items)
            clean_all_work_items = Process.all_work_items(resp_list.json())
            for type_id in clean_all_work_items:
                fields = Endpoint.fields_process(
                    self._organization, self._process, type_id
                )
                resp_fields = self.__get(fields)
                schema = Process.clean_fields(resp_fields.json())
                self._columns.update(Process.spark_equivalent(schema))
            print("Ok")
            return True
        except Exception as e:
            raise (f"Error in __mapping_columns: {e}")

    def __get_items(self, items: array[int]) -> List[dict]:
        """
        `Get a list of ids and returns a maximum of 200 work items per request.`
        :param items: An array of unsigned int with all items of the project -> ['85','86','87',...].
        """
        matrix = []
        while True:
            if len(items) >= 200:
                slice_items = items[:200]
                del items[:200]
                matrix.append(self.__max_items(slice_items))
            else:
                slice_items = items
                matrix.append(self.__max_items(slice_items))
                break

        return [item for data in matrix for item in data]

    def __max_items(self, work_items: array[int]) -> List[dict]:
        """
        `Get assignment of `maximum 200 ids` of work items and returns the corresponding data.`
        :param work_items: An array of unsigned int with a maximum size of 200 ids -> [1, 2, 3,..., 4].
        """
        data = []
        id_list = ",".join([str(item) for item in work_items])
        fields = ",".join(self._columns.keys())
        url = Endpoint.work_items(self._organization, self._project, id_list, fields)
        response = self.__get(url).json()
        if "value" in response:
            len_fields = len(response["value"])
            for i in range(0, len_fields):
                fields = response["value"][i]["fields"]
                clean_response = Process.columns(
                    fields, self._columns, self._fields_displayname
                )
                data.append(clean_response)
        return data

    def __get(self, url: str):
        return get(url=url, headers=self.headers)

    def __validade_status(self) -> bool:
        """
        `Validates access credentials with the platform.`
        """
        endpoint = Endpoint.build(self._organization, self._project)
        status = self.__get(endpoint).status_code
        http_status = {
            "302": f"Found.",
            "400": f"Bad Request.",
            "404": f"Not Found.",
            "203": f"No Authorized.",
        }
        if status == 200:
            print("200 - Ok")
            print("Mapping columns...")
            return self.__mapping_columns()
        else:
            err = f"{status} - {http_status.get(str(status))}"
            raise Exception(err)
