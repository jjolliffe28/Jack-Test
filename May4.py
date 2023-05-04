import pandas as pd

# Load the DataFrame
df = pd.read_csv("your_file.csv")

# Create a list of IDs that have "Y" values
ids_with_y = df[df["Leveraged Flag Value"] == "Y"]["Source Facility IDs"].unique().tolist()

# Filter the DataFrame to keep only the IDs that have "Y" or both "Y" and "N" values
df_filtered = df[df["Source Facility IDs"].isin(ids_with_y)]

# Output the filtered DataFrame
print(df_filtered)
