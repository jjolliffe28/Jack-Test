import certifi
import ssl
from tableauserverclient import Server

# specify the path to the trusted SSL certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())

# create a server object
server = Server('https://yourtableauserver.com', use_server_version=True)

# set the SSL context for the server
server.add_http_options({'verify': ssl_context})

# connect to the Tableau Server using username and password
server.auth.sign_in('yourusername', 'yourpassword')

# get the workbook and download data sources as csv
workbook = server.workbooks.get_by_name('yourworkbookname')
for datasource in workbook.datasources:
    csv_path = datasource.download_as_file('csv')
    print(f"Data source '{datasource.name}' downloaded to '{csv_path}'")

# sign out of the Tableau Server
server.auth.sign_out()
