last_change_dates = {}

# loop through each row of the dataframe
for index, row in df.iterrows():
    # check if the name is already in the dictionary
    if row['name'] in last_change_dates:
        # check if the flag has changed
        if row['flag'] != last_change_dates[row['name']][0]:
            # if flag has changed, update the dictionary with the new date
            last_change_dates[row['name']] = (row['flag'], row['date'])
    else:
        # if name is not in the dictionary, add it with current flag and date
        last_change_dates[row['name']] = (row['flag'], row['date'])

# create a new column in the dataframe to store the last change dates
df['last_change_date'] = df['name'].apply(lambda x: last_change_dates[x][1])

# sort the dataframe back to its original order
df = df.sort_index()

print(df)
