from setuptools import setup


text = """
## Azure Devops PySpark:  A productive library to extract data from Azure Devops and apply agile metrics.

## What is it?

Azure Devops PySpark is a Python package that provides the most productive way to extract data from Azure Devops and build agile metrics.
It runs on PySpark, enabling all the features the technology makes available.

## Main Features

- Get authenticated quickly and simply.

- All columns of the project are automatically mapped, use the filter_columns method to filter only those you want to form your dataframes with.
- SparkSession already created in spark variable.
- Get all your organization's backlogs with the method **backlog**.
- Get all your organization's items with the method **items**.
- Get all your organization's iterations with the method **iterations**.
- Get all your organization's members with the method **members**.
- Get all your organization's tags with the method **tags**.
- Get all your organization's teams with the method **teams**.
- Explore the simplicity of Agile class to build powerful metrics for your organization.

## Quick example

```python
from AzureDevopsPySpark import Azure, Agile
from pyspark.sql.functions import datediff #use in agile metrics

devops = Azure('ORGANIZATION', 'PROJECT', 'PERSONAL ACCESS TOKENS')
```

```python
## Filter columns
devops.filter_columns([
    'IterationPath', 'Id', 'State', 'WorkItemType',
    'CreatedDate', 'ClosedDate', 'Iteration_Start_Date', 'Iteration_End_Date'
])


## Pyspark Dataframe
df_backlog = devops.backlog()
df_items = devops.items()
df_iterations = devops.iterations()
df_members = devops.members()
df_tags = devops.tags()
df_teams = devops.teams()
```

```python
## Agile Metrics
agile = Agile()

## A new dataframe
df_agil = df.items.join(df_iterations, 'IterationPath')

## Metrics

## Average time between CreatedDate and ClosedDate of items in the last 90 days.
lead_time = agile.avg(
    df=df_agil,
    ref=[datediff, 'ClosedDate', 'CreatedDate'], # The day difference between the CreatedDate and ClosedDate of each item.
    iteration_path='IterationPath', # GroupBy.
    new='LeadTimeDays', # New column name.
    literal_filter=['ClosedDate >= 90'], # Filtering items from the last 90 days.
    filters={'WorkItemType': 'Task', 'State': 'Closed'} # Custom filters for metric.
).df
```

## Author

The Azure-Devops-PySpark library was written by Guilherme Silva <<https://www.linkedin.com/in/gusantosdev/>> in 2022.

https://github.com/gusantos1/Azure-Devops-Spark

## License

GNU General Public License v3.0.
"""

setup(
    name = 'azure-devops-pyspark',
    version = '0.0.0.35',
    author = 'Guilherme Silva dos Santos',
    author_email = 'gusantos.ok@gmail.com',
    packages = ['AzureDevopsPySpark'],
    description = 'A productive library to extract data from Azure Devops and apply agile metrics.',
    long_description= text,
    long_description_content_type='text/markdown',
    license = 'GNU General Public License v3.0',
    keywords = 'Azure AzureDevops WorkItems PySpark Agile',
    install_requires= [
        'certifi>=2021.10.8',
        'charset-normalizer>=2.0.12',
        'idna>=3.3',
        'requests>=2.27.1',
        'urllib3>=1.26.9',
        'python-dateutil>=2.8.2',
        'pandas>=1.0.0',
        'PyArrow>=5.0.0'
    ]
)