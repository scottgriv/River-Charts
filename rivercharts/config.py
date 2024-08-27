# Config file for the rivercharts application

# Variables that will be used in the views.py file, consult the README for more information
USE_DUMMY_DATA = False  # Set this flag to False when you want to use the real API vs. using Dummy static data (False is the default)
USE_SNAPSHOT_DATA = True  # Set this flag to False when you want to use the dynamic API data vs. Snapshot static data via the snapshot/snapshot.json file (Manual Data Entry) (False is the default)
SITE_CODE = "01533400" # Site Code: Susquehanna River at Meshoppen, PA
PARAMETER_CODE = "00065" # Parameter Code: Gage height, ft
START_DATE = "2015-07-01" # Replace this with how you determine your start date
END_DATE = "" # Replace this with how you determine your end date, leave blank if you want to use the current date
TIME_ZONE = "America/New_York" # Replace with your current Time Zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
API_URL = "https://waterservices.usgs.gov/nwis/iv" # USGS API URL
STATION_NAME = "Susquehanna River at Meshoppen, PA"  # Replace this with your station name to be displayed on the main page of the website
REQUEST_TIMEOUT_SECONDS = 90  # Set this to a reasonable timeout for your API retrieval (90 seconds is the default)

# These are the codes for the NWS URL found in the river_graph.html template <footer> tag
# These are not being used in the main app and used as a reference only but be sure to update the link for your application
GAGE_CODE = "mhpp1" # Gauge: Meshoppen, PA
WFO_CODE = "bgm" # Weather Forecast Office (WFO): Binghamton, NY