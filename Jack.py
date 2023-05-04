import pandas as pd

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Sort the dataframe by date and Current_Source_Facility_ID
df = df.sort_values(by=['Date', 'Current_Source_Facility_ID'])

# Backfill null values with the value of the last non-null value
df['Key_Leveraged_FDICHIGHRisk'] = df.groupby('Current_Source_Facility_ID')['Key_Leveraged_FDICHIGHRisk'].bfill()

# Forward fill null values with the value of the last non-null value
df['Key_Leveraged_FDICHIGHRisk'] = df.groupby('Current_Source_Facility_ID')['Key_Leveraged_FDICHIGHRisk'].ffill()

# Check the resulting dataframe
print(df)
