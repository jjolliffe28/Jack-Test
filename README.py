# sort the dataframe by name and date
df = df.sort_values(['name', 'date'], ascending=[True, False])

# create an empty dictionary to store the last change dates
last_change_dates = {}

# iterate over each group of the dataframe in reverse order
for name, group in df.groupby('name', sort=False).apply(lambda x: x.iloc[::-1]):
    # get the flag values and dates of the group
    flags = group['flag'].values
    dates = group['date'].values
    
    # iterate over each pair of adjacent rows
    for i in range(len(flags)-1):
        # check if the flag values are different
        if flags[i] != flags[i+1]:
            # if they are different, add the last change date to the dictionary
            last_change_dates[name] = dates[i+1]
            break
    
    # if the last change date is not found, add None to the dictionary
    if name not in last_change_dates:
        last_change_dates[name] = None

# create a new column in the dataframe to store the last change dates
df['last_change_date'] = df['name'].apply(lambda x: last_change_dates.get(x, None))

# sort the dataframe back to its original order
df = df.sort_index()

print(df)
