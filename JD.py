import pandas as pd
import glob

# Folder containing all the excel sheets
folder_path = 'path_to_your_excel_files/*.xlsm'

# Initialize an empty list to store the data
all_data = []

# Loop through all Excel files in the folder
for file in glob.glob(folder_path):
    # Extract the month and year from the file name (assuming the format 'Simulation Rates MMYY.xlsm')
    forecast = file.split('Simulation Rates ')[1].replace('.xlsm', '')
    
    # Load the sheet 'RI MV' but without a header to identify the correct rows/columns
    df = pd.read_excel(file, sheet_name='RI MV', header=None)
    
    # Locate where the actual data starts by finding the first row that has dates (e.g., formatted like 12/31/2022)
    for i, row in df.iterrows():
        if pd.to_datetime(row, errors='coerce').notna().sum() > 0:
            start_row = i
            break
    
    # Now reload the file with the correct start row
    df = pd.read_excel(file, sheet_name='RI MV', skiprows=start_row)
    
    # Assume that the first row after skipping contains the dates
    df.columns = ['Metric'] + list(df.columns[1:])
    
    # Extract the rows containing 'Fed Fund' and 'Fed Fund Effective Rate'
    fed_fund_data = df[df['Metric'].str.contains('Fed Fund', na=False)]
    
    # Reshape the data using melt, keeping the dates as columns
    melted_data = pd.melt(fed_fund_data, id_vars=['Metric'], var_name='Date', value_name='Value')
    
    # Convert 'Date' column to datetime (since the date column should have proper dates now)
    melted_data['Date'] = pd.to_datetime(melted_data['Date'], errors='coerce', format='%m/%d/%Y')
    
    # Add a column for the forecast based on the file name
    melted_data['Forecast'] = forecast
    
    # Pivot the data to have 'Fed Fund' and 'Fed Fund Effective Rate' as separate columns
    pivoted_data = melted_data.pivot_table(index=['Date', 'Forecast'], columns='Metric', values='Value').reset_index()
    
    # Append the processed data to the list
    all_data.append(pivoted_data)

# Combine all the data into one dataframe
final_df = pd.concat(all_data, ignore_index=True)

# Rename columns for clarity
final_df.columns.name = None  # Remove the name for the columns after pivoting
final_df.rename(columns={
    'Fed Fund': 'Fed Fund Rate',
    'Fed Fund Effective Rate': 'Fed Fund Effective Rate'
}, inplace=True)

# Display the final dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Fed Fund Data", dataframe=final_df)

# You can now save the final dataframe to a new Excel file if desired
final_df.to_excel('Fed_Fund_Data_Combined.xlsx', index=False)




import pandas as pd
import glob

# Folder containing all the excel sheets
folder_path = 'path_to_your_excel_files/*.xlsm'

# Initialize an empty list to store the data
all_data = []

# Loop through all Excel files in the folder
for file in glob.glob(folder_path):
    # Extract the month and year from the file name (assuming the format 'Simulation Rates MMYY.xlsm')
    forecast = file.split('Simulation Rates ')[1].replace('.xlsm', '')
    
    # Load the sheet 'RI MV' but without a header to identify the correct rows/columns
    df = pd.read_excel(file, sheet_name='RI MV', header=None)
    
    # Locate where the actual data starts by finding the first row that has dates (e.g., formatted like 12/31/2022)
    for i, row in df.iterrows():
        if pd.to_datetime(row, errors='coerce').notna().sum() > 0:
            start_row = i
            break
    
    # Now reload the file with the correct start row
    df = pd.read_excel(file, sheet_name='RI MV', skiprows=start_row)
    
    # Assume that the first row after skipping contains the dates
    df.columns = ['Metric'] + list(df.columns[1:])
    
    # Extract the rows containing 'Fed Fund' and 'Fed Fund Effective Rate'
    fed_fund_data = df[df['Metric'].str.contains('Fed Fund', na=False)]
    
    # Reshape the data using melt, keeping the dates as columns
    melted_data = pd.melt(fed_fund_data, id_vars=['Metric'], var_name='Date', value_name='Value')
    
    # Convert 'Date' column to datetime (since the date column should have proper dates now)
    melted_data['Date'] = pd.to_datetime(melted_data['Date'], errors='coerce', format='%m/%d/%Y')
    
    # Add a column for the forecast based on the file name
    melted_data['Forecast'] = forecast
    
    # Append the processed data to the list
    all_data.append(melted_data)

# Combine all the data into one dataframe
final_df = pd.concat(all_data, ignore_index=True)

# Display the final dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Fed Fund Data", dataframe=final_df)

# You can now save the final dataframe to a new Excel file if desired
final_df.to_excel('Fed_Fund_Data_Combined.xlsx', index=False)
