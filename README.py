from google.cloud import bigquery
import pandas as pd

# create a bigquery client
client = bigquery.Client()

# read the CSV file into a pandas data frame
df = pd.read_csv('path/to/your/csv/file.csv')

# specify the schema of the table
schema = [
    bigquery.SchemaField('SICCode', 'STRING'),
    # add the schema for the other columns in the table here
]

# create a bigquery table
table_ref = client.dataset('your_dataset').table('your_table')
table = bigquery.Table(table_ref, schema=schema)
table = client.create_table(table)

# upload the data to the table
job_config = bigquery.LoadJobConfig(schema=schema)
job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
job.result()
