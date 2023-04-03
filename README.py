from google.cloud import bigquery
import pandas as pd

# create a bigquery client
client = bigquery.Client()

# read the CSV file into a pandas data frame
df = pd.read_csv('path/to/your/csv/file.csv')

# specify the schema for the "SICCode" column
schema = [
    bigquery.SchemaField('SICCode', 'STRING'),
]

# get the default schema for the other columns
default_schema = bigquery.Schema.from_dataframe(df.drop(columns=['SICCode']))

# merge the schemas
merged_schema = schema + default_schema

# create a bigquery table
table_ref = client.dataset('your_dataset').table('your_table')
table = bigquery.Table(table_ref, schema=merged_schema)
table = client.create_table(table)

# upload the data to the table
job_config = bigquery.LoadJobConfig(schema=merged_schema)
job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
job.result()
