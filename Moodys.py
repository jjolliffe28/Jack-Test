import requests
import pandas as pd
from datetime import date

# Moody's Data Buffet API endpoint
api_url = "https://api.moodys.com/data-buffet-api-endpoint"

# Define your API request parameters
params = {
    "indicator": "GDP",            # Indicator code for GDP
    "start_date": date.today(),    # Start date (today)
    "end_date": date.today().replace(year=date.today().year - 8),  # End date (8 years ago)
    "frequency": "M",              # Monthly frequency
}

# Replace 'YOUR_API_KEY' with your actual API key from Moody's
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

# Make the API request
response = requests.get(api_url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the API response to a DataFrame
    df = pd.read_json(response.text)

    # Assuming the API response provides data in a JSON format
    # You may need to adjust this part based on the actual API response structure

    # Print the DataFrame with GDP data
    print(df)
else:
    print(f"API request failed with status code: {response.status_code}")
