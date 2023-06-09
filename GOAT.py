flag_changed = df.groupby(['name', 'flag'])['flag'].count().unstack().fillna(0)
flag_changed['Reentered Leverage'] = ((flag_changed['Y'] > 1) & (flag_changed['N'] > 0)).astype(bool)

# merge the flag_changed DataFrame back into the original DataFrame on the 'name' column
df = df.merge(flag_changed['Reentered Leverage'], on='name')

# save the updated DataFrame to a new file or overwrite the original
df.to_csv('updated_dataset.csv', index=False)


# load your dataset into a DataFrame object
df = pd.read_csv('your_dataset.csv')

# group by name and flag, then check if all the flags are N for a given name
flag_counts = df.groupby('name')['flag'].value_counts().unstack().fillna(0)
n_only_names = flag_counts[flag_counts['Y'] == 0].index

# remove all records for names with flags that are always N
df = df[~df['name'].isin(n_only_names)]

# save the updated DataFrame to a new file or overwrite the original
df.to_csv('updated_dataset.csv', index=False)

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
