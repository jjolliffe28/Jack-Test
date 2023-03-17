import getpass
import tableauserverclient as TSC

# Set up the authentication
username = '<username>'
password = getpass.getpass()
site_id = '<site_id>'

auth = TSC.TableauAuth(username, password, site_id=site_id)

# Set up the server object
server = TSC.Server('<server_url>')

# Connect to the server
with server.auth.sign_in(auth):
    # Find the workbook by name
    workbook_name = '<workbook_name>'
    workbooks, _ = server.workbooks.get()

    for workbook in workbooks:
        if workbook.name == workbook_name:
            # Download each data source in the workbook
            for ds in workbook.published_ds:
                ds_data = server.datasources.download(ds.id)
                ds_file_name = f'{ds.name}.csv'
                with open(ds_file_name, 'wb') as f:
                    f.write(ds_data)
                print(f'Successfully downloaded data source {ds.name} to {ds_file_name}')
