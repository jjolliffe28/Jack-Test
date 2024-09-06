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
    
    # Load the sheet 'RI MV' but let pandas auto-detect where the table starts
    df = pd.read_excel(file, sheet_name='RI MV', header=None)
    
    # Find the row where the table actually starts (e.g., where dates start)
    for i, row in df.iterrows():
        if pd.to_datetime(row, errors='coerce').notna().sum() > 0:
            start_row = i - 1  # The header row with metric names is typically just above the first date row
            break

    # Reload the file with the correct starting row
    df = pd.read_excel(file, sheet_name='RI MV', skiprows=start_row)

    # Extract the rows containing 'Fed Fund' and 'Fed Fund Effective Rate'
    fed_fund_data = df[df.iloc[:, 0].str.contains('Fed Fund', na=False)]
    
    # Rename the first column to 'Metric' and retain date columns
    fed_fund_data.rename(columns={fed_fund_data.columns[0]: 'Metric'}, inplace=True)
    
    # Melt the dataframe to make it long-format (Metric, Date, Value)
    melted_data = pd.melt(fed_fund_data, id_vars=['Metric'], var_name='Date', value_name='Value')
    
    # Ensure the 'Date' column is in datetime format
    melted_data['Date'] = pd.to_datetime(melted_data['Date'], errors='coerce')
    
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
