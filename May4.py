import pandas as pd

# Load the DataFrame
df = pd.read_csv("your_file.csv")

# Create a list of IDs that have "Y" values
ids_with_y = df[df["Leveraged Flag Value"] == "Y"]["Source Facility IDs"].unique().tolist()

# Filter the DataFrame to keep only the IDs that have "Y" or both "Y" and "N" values
df_filtered = df[df["Source Facility IDs"].isin(ids_with_y)]

# Output the filtered DataFrame
print(df_filtered)

import pandas as pd

# Example data
data = {'Date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02', '2021-01-02', '2021-01-02', '2021-01-03', '2021-01-03'],
        'Source Facility IDs': ['ID1', 'ID2', 'ID3', 'ID4', 'ID1', 'ID2', 'ID3', 'ID4', 'ID1', 'ID2'],
        'Leveraged Flag Value': ['N', 'N', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y']}
df = pd.DataFrame(data)

# Convert date string to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date and group by Source Facility IDs
df = df.sort_values(by=['Date']).groupby(['Source Facility IDs'])

# Loop through each group and filter out rows where 'N' occurs before 'Y'
filtered_df = pd.DataFrame()
for _, group_df in df:
    y_occured = False
    for index, row in group_df.iterrows():
        if row['Leveraged Flag Value'] == 'Y':
            y_occured = True
            filtered_df = filtered_df.append(row)
        elif y_occured:
            filtered_df = filtered_df.append(row)
            
# Reset index and sort by date
filtered_df = filtered_df.reset_index(drop=True).sort_values(by=['Date'])

print('Original DataFrame:')
print(df)
print('\nCleaned DataFrame:')
print(filtered_df)

