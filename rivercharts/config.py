# Config file for the rivercharts application

# Variables that will be used in the views.py file
USE_DUMMY_DATA = False  # Set this flag to False when you want to use the real API (False is the default)
SITE_CODE = "01533400" # Site Code: Susquehanna River at Meshoppen, PA
PARAMETER_CODE = "00065" # Parameter Code: Gage height, ft
START_DATE = "2015-07-01" # Replace this with how you determine your start date
API_URL = "https://waterservices.usgs.gov/nwis/iv" # USGS API URL
STATION_NAME = "Susquehanna River at Meshoppen, PA"  # Replace this with how you determine your station name
REQUEST_TIMEOUT_SECONDS = 60  # Set this to a reasonable timeout for your API retrieval (6o seconds is the default)

# These are the codes for the NWS URL found in the river_graph.html template <footer> tag
# These are not being used and used as a reference only but be sure to update the link for your application
GAGE_CODE = "mhpp1" # Gauge: Meshoppen, PA
WFO_CODE = "bgm" # Weather Forecast Office (WFO): Binghamton, NY