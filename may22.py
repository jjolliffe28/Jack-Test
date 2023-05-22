import pandas as pd

# Specify the file path of your Excel file
file_path = 'your_file.xlsx'  # Replace with your actual file path

# Specify the row name
row_name = 'Cash'  # Replace with your actual row name

# Read the Excel file, skipping hidden rows
df = pd.read_excel(file_path, skiprows=lambda x: x in pd.read_excel(file_path, header=None, skiprows=None, nrows=x, na_values=['NA']).dropna(how='all').index)

# Find the index of the row containing the given row name
row_index = df.index[df.iloc[:, 0] == row_name].tolist()[0]

# Extract the values from the next 4 visible cells to the right
values = df.iloc[row_index, df.columns.get_loc('G'):df.columns.get_loc('J')+1].tolist()

# Print the extracted values
print(values)
