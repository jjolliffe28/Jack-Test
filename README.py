import pandas as pd

# Load your data frame into a pandas DataFrame object called "df"

# Calculate the FIRST WAPD value
df['FIRST_WAPD'] = df['FIRST_PD_CMT_AMT'] / df['CMT Open']

# Calculate the LAST WAPD value
df['LAST_WAPD'] = df['LAST_PD_CMT_AMT'] / df['CMT Last']

# Print the resulting DataFrame with the new columns
print(df.head())


import pandas as pd

# Load your data frame into a pandas DataFrame object called "df"

# Define the bin edges for the FIRST WAPD values
bin_edges = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

# Create a new column in the data frame with the bin labels based on FIRST WAPD values
df['FIRST_WAPD_BIN'] = pd.cut(df['FIRST_WAPD'], bins=bin_edges, labels=[f'{x:.2f}-{y:.2f}' for x, y in zip(bin_edges[:-1], bin_edges[1:])])

# Group the data frame by FIRST WAPD bins and calculate the average LAST WAPD for each bin
avg_last_wapd = df.groupby('FIRST_WAPD_BIN')['LAST_WAPD'].mean()

# Print the resulting Series with the average LAST WAPD for each bin
print(avg_last_wapd)


CASE 
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.05 THEN "0-0.04999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.05 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.1 THEN "0.05-0.09999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.1 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.15 THEN "0.1-0.14999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.15 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.2 THEN "0.15-0.19999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.2 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.25 THEN "0.2-0.24999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.25 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.3 THEN "0.25-0.29999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.3 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.35 THEN "0.3-0.34999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.35 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.4 THEN "0.35-0.39999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.4 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.45 THEN "0.4-0.44999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.45 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.5 THEN "0.45-0.49999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.5 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.55 THEN "0.5-0.54999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.55 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.6 THEN "0.55-0.59999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.6 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.65 THEN "0.6-0.64999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.65 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.7 THEN "0.65-0.69999"
  WHEN [FIRST_PD_CMT_AMT]/[CMT_OPEN] >= 0.7 AND [FIRST_PD_CMT_AMT]/[CMT_OPEN] < 0.75 THEN "0.7-0.74999"
  ELSE NULL
END
