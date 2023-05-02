import pandas as pd

# create sample dataset
data = {'Name': ['Jack', 'Paige', 'Grace', 'Jack', 'Paige', 'Grace', 'Jack', 'Paige', 'Grace'],
        'Field': ['Y', 'Y', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'N']}
df = pd.DataFrame(data)

# create a new column that counts the changes between 'Y' and 'N' values for each name
df['Changes'] = df.groupby('Name')['Field'].transform(lambda x: x.ne(x.shift()).astype(int).cumsum())

print(df)


# Counts flag changes

import pandas as pd

# create sample dataset
data = {'Name': ['Jack', 'Paige', 'Grace', 'Jack', 'Paige', 'Grace', 'Jack', 'Paige', 'Grace'],
        'Leveraged Flag': ['Y', 'Y', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'N'],
        'Date': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04', '2015-01-05', '2015-01-06', '2015-03-15', '2015-03-16', '2015-03-17']}
df = pd.DataFrame(data)

# get the list of unique names in the dataset
names = df['Name'].unique()

# loop over each name, and add a column that shows the date of the last entry for the name,
# and another column that shows the last value of the Leveraged Flag field
for name in names:
    df_name = df[df['Name'] == name]
    last_date = df_name['Date'].max()
    last_flag = df_name['Leveraged Flag'].iloc[-1]
    df.loc[df['Name'] == name, 'Last Date'] = last_date
    df.loc[df['Name'] == name, 'Last Flag'] = last_flag

print(df)


# Last flag, Last Date on Record
