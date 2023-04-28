import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'name': ['John', 'Mary', 'John', 'Mary', 'John'],
    'flag': ['Y', 'N', 'Y', 'Y', 'N'],
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']
})

# convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# sort the dataframe by name and date in descending order
df = df.sort_values(['name', 'date'], ascending=[True, False])

# add a new column to store the last changed date
df['last_change_date'] = None

# iterate over each unique name in the dataframe
for name in df['name'].unique():
    # get the rows for the current name
    name_df = df[df['name'] == name]
    
    # iterate over each row in the name_df in descending order
    for i, row in name_df[::-1].iterrows():
        # if it's the first row, set the last_change_date to the date of the row
        if i == name_df.index[-1]:
            df.loc[i, 'last_change_date'] = row['date']
        else:
            # get the previous row
            prev_row = name_df.loc[i + 1]
            # if the flag has changed from Y to N or from N to Y
            if prev_row['flag'] != row['flag']:
                df.loc[i, 'last_change_date'] = prev_row['date']

# output the final dataframe
print(df)
