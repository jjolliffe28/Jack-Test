import tableauserverclient as TSC
from tableauserverclient import Server
from tableauserverclient import TableauAuth
from tableauserverclient import OAuth2Auth

# Replace with your Tableau Server URL
server_url = 'https://your-server.com'

# Replace with your OAuth access token
access_token = 'your-oauth-access-token'

# Replace with the name of your workbook and data source
workbook_name = 'your-workbook-name'
datasource_name = 'your-data-source-name'

# Replace with the path where you want to save the CSV file
csv_path = 'path/to/output.csv'

# Create a Server object
server = Server(server_url)

# Create an OAuth authentication object
auth = OAuth2Auth(access_token)

# Authenticate and sign in to the server
server.auth.sign_in(auth)

# Find the workbook
workbook = server.workbooks.get_by_name(workbook_name)

# Get the data source
datasource = workbook.datasources.get_by_name(datasource_name)

# Download the data source as a CSV
with open(csv_path, 'wb') as f:
    f.write(datasource.download())

# Sign out of the server
server.auth.sign_out()
