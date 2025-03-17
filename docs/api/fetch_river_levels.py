import requests
import json

# Define API parameters as variables
BASE_URL = "https://waterservices.usgs.gov/nwis/iv"
format_type = "json"
sites = "01533400"  # Site ID
start_date = "2022-01-01"
end_date = "2025-03-16"
parameter_code = "00065"  # Gage height, feet
site_status = "active"
site_type = "ST"

# Construct the API URL dynamically
API_URL = f"{BASE_URL}?format={format_type}&sites={sites}&startDT={start_date}&parameterCd={parameter_code}&siteStatus={site_status}&siteType={site_type}&endDT={end_date}"

def fetch_river_data():
    """Fetch river level data from USGS API and save it as a JSON file."""
    try:
        print(f"Fetching data from USGS API:\n{API_URL}")
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()

        # Save JSON response to a file
        json_file = "snapshot.json"
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"✅ JSON data saved to {json_file}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    fetch_river_data()
