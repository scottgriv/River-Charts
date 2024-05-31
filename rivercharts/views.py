# Description: This file contains the views for the rivercharts app.

# Import the necessary modules
import os
import requests
import math
import pytz
from datetime import datetime
import json
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from django.conf import settings
from datetime import datetime, timedelta
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .config import USE_DUMMY_DATA, USE_DEMO_DATA, SITE_CODE, PARAMETER_CODE, START_DATE, END_DATE, TIME_ZONE, API_URL, STATION_NAME, REQUEST_TIMEOUT_SECONDS

# These are the config variables from config.py
config_use_dummy_data = USE_DUMMY_DATA
config_use_demo_data = USE_DEMO_DATA
config_site_code = SITE_CODE
config_parameter_code = PARAMETER_CODE
config_start_date = START_DATE
config_end_date = END_DATE
config_time_zone = TIME_ZONE
config_api_url = API_URL
config_station_name = STATION_NAME
requests_timeout_seconds = REQUEST_TIMEOUT_SECONDS

# These are the default values
current_date = datetime.now().strftime("%Y-%m-%d")
start_date = datetime(2015, 7, 1, tzinfo=pytz.utc) # Start date for dummy data
dummy_data = {
    'value': {
        'timeSeries': [{
            'values': [{
                'value': [{
                    'dateTime': (start_date + timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                    'value': str(10 + 5*math.sin(i/10))
                } for i in range(3000)]  # 3000 or however many entries you want (days)
            }]
        }]
    }
}

# This is the CSV file that contains the float data
CSV_FILE_PATH = os.path.join(settings.BASE_DIR, 'static', 'data', 'river_charts.csv')
FLOAT_DATA = pd.read_csv(CSV_FILE_PATH)
FLOAT_DATA['Date'] = pd.to_datetime(FLOAT_DATA['Date'], format='%m-%d-%Y')
json_file_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'demo.json')

# This is the view that will be called when the page is first loaded
def river_graph_initial(request):
    return render(request, 'rivercharts/river_graph.html')

# This is the view that will be called when an error occurs
def error_view(request, error_message="An error occurred."):
    return render(request, 'rivercharts/error.html', {'error_message': error_message})

# This is the view that will be called by the AJAX request
def river_graph_data(request):
    api_url = config_api_url
    site_code = config_site_code
    start_date = config_start_date
    end_date = current_date if config_end_date == "" else config_end_date
    parameter_code = config_parameter_code

    params = {
        "format": "json",
        "sites": site_code,
        "startDT": start_date,
        "endDT": end_date,
        "parameterCd": parameter_code,
        "siteStatus": "active",
        "siteType": "ST",
    }

    # Path to the JSON file
    # json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'demo.json')
    
    # Function to load JSON data
    def load_json_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)


    # Use dummy data if the config variable is set to True
    if config_use_dummy_data:
        data = dummy_data
    elif config_use_demo_data:
        data = load_json_data(json_file_path)
    # Otherwise, make the request to the API
    else:
        try:
            response = requests.get(api_url, params=params, timeout=requests_timeout_seconds)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
            print('Timeout')
            # return redirect('error_view_with_message', error_message="Request timed out after 3 seconds.")
            return JsonResponse({"error": f"Request timed out after {requests_timeout_seconds} seconds."})
        except requests.exceptions.HTTPError as http_err:
            print('HTTP Error')
            return JsonResponse({"error": f"HTTP error occurred: {http_err}."})
        except requests.exceptions.RequestException as req_err:
            print('Request Exception')
            return JsonResponse({"error": f"Request error occurred: {req_err}."})
        except ValueError as json_err:
            print('Value Error')
            return JsonResponse({"error": f"JSON decode error: {json_err}."})
        
    print('Response OK')
    time_series = data['value']['timeSeries'][0]
    values = time_series['values'][0]['value']

    # Time zone for EST/EDT
    time_zone = pytz.timezone(config_time_zone)

    # Create a list of dictionaries to store the data
    data_list = []
    for i, entry in enumerate(values):
        # date_time = datetime.strptime(entry['dateTime'], "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%B %d, %Y %I:%M:%S %p EST')
        # Step 1: Parse the datetime with the time zone information
        parsed_date_time = datetime.strptime(entry['dateTime'], "%Y-%m-%dT%H:%M:%S.%f%z")
        # Step 2: Convert to the desired time zone
        date_time = parsed_date_time.astimezone(time_zone)
        # Step 3: Format the datetime for display
        formatted_date_time = date_time.strftime('%B %d, %Y %I:%M:%S %p %Z')
        
        data_list.append({
            'Date Time': datetime.strptime(entry['dateTime'], "%Y-%m-%dT%H:%M:%S.%f%z"),
            'River Level': float(entry['value']),
            'Date': datetime.strptime(entry['dateTime'], "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%B %d, %Y %I:%M:%S %p EST')
        })

        if i == 0:
            first_date_time = formatted_date_time
        last_date_time = formatted_date_time  # Update last_date_time to the most recent entry
        last_river_level = float(entry['value'])  # Update last_river_level to the most recent entry

    # Create a dataframe from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Debug: Print the last few rows of the dataframe to ensure it includes the latest date
    # print("Last few rows of the DataFrame:")
    # print(df.tail())
    
    # Optional: Resample the DataFrame to hourly means vs. the current more granular approach
    # FYI: There is no code to support this as of now, this would be the start below:
    # df_resampled = df.resample('H', on='Date Time').mean().reset_index()

    # Create line trace
    fig = px.line(df, x='Date Time', y='River Level', title='River Levels')
    fig.update_traces(line=dict(color='black', width=0.5))

    # Create filled scatter trace and add hovertemplate
    fig_filled = go.Scatter(
        x=df['Date Time'], 
        y=df['River Level'], 
        name=f"River Level",  # This line sets the name in the legend
        fill='tozeroy', 
        fillcolor='#32C5FF', 
        line=dict(color='#0091FF', width=1.0),
        hovertemplate='%{x|%B %d, %Y %I:%M:%S %p EST}<br>River Level: %{y:.2f} ft<extra></extra>',
        hoverlabel=dict(bgcolor='rgba(0, 0, 0, 1.0)')  # Use RGBA format here
        # hoverlabel=dict(bgcolor='#')  # Use this to trigger a HTTP Error
    )

    fig.add_trace(fig_filled)

    # Drawing vertical lines for each float from the CSV data
    # Loop through each row of the FLOAT_DATA to add lines and scatter points
    for _, row in FLOAT_DATA.iterrows():
        float_date = row['Date']
        float_number = row['Float']
        floated_status = row['Floated']

        # Determine the color based on the Floated status
        if floated_status == "N":
            color = "red" # Red: #FF0000
        elif floated_status == "Y":
            color = "green" # Green: #008000
        else:
            color = "orange" # Orange: #FFA500

        # Determine the floated status text
        floated_status_text = "No" if floated_status == "N" else ("Yes" if floated_status == "Y" else "Skipped")

        # Find the closest date in df to the float_date and get its river level
        closest_date = df.iloc[((df['Date Time'].apply(lambda x: x.timestamp() * 1e9) - float_date.value).abs()).argsort()[:1]]

        if not closest_date.empty:
            river_level = closest_date['River Level'].values[0]

            # Add vertical line for each float from the CSV data
            fig.add_shape(
                type="line",
                x0=float_date,
                y0=2.0,  # starting from the bottom of the graph
                x1=float_date,
                y1=river_level,  # ending at the river level for the closest date
                line=dict(color=color, width=1)
            )

            # Add annotation (number) from CSV above the line
            fig.add_annotation(
                x=float_date,
                y=1.0,  # Place the annotation slightly above the line
                text=str(float_number),
                showarrow=False,
                font=dict(
                    size=20,
                    color=color
                )
            )

            # Add scatter points for each float from the CSV data
            fig.add_trace(
                go.Scatter(
                    x=[float_date],
                    y=[river_level],
                    mode='markers',
                    marker=dict(color=color, size=10),
                    name=f"Float {float_number} - {river_level:.2f} ft",  # This line sets the name in the legend
                    text=[str(float_number)],  # This places the float number next to the point
                    hoverinfo="text",
                    hovertext=[f"Date: {float_date.strftime('%m-%d-%Y')}<br>Float #: {float_number}<br>Height: {river_level:.2f} ft<br>Floated: {floated_status_text}"]
                )
            )

            width = request.GET.get('width', 1400) # Default to 1400 if width is not provided

            # Adjust the threshold as necessary. For example, 768 is a common breakpoint for tablets and below.
            is_mobile = int(width) <= 768 

            # Adjust the bottom margin based on whether it's mobile or not
            bottom_margin_value = 110 if is_mobile else 50

            x_min = df['Date Time'].min()  # Get the earliest date
            x_max = df['Date Time'].max()  # Get the latest date

            # Debug: Print the min and max x-axes
            # print(f"x_min: {x_min}, x_max: {x_max}")

            fig.update_layout(
                font=dict(family='GochiHand, sans-serif'), # This changes the font for the entire plot
                plot_bgcolor='#F5F5F5',   # This changes the plot's background color
                paper_bgcolor='#F5F5F5',  # This changes the area around the plot's background color
                xaxis=dict(
                    title="Year", 
                    tickformat="%Y",
                    range=[x_min, x_max],
                    gridcolor='#d1e7ff',
                    zerolinecolor='#d1e7ff'
                ),
                yaxis=dict(
                    title="River Level (ft)",
                    gridcolor='#d1e7ff',
                    zerolinecolor='#d1e7ff'
                ),
                width=int(width),
                height=590,
                autosize=True,
                margin=dict(l=50, r=50, b=bottom_margin_value, t=50, pad=0) # Adjusting the margins
            )

    # Convert the plot to HTML
    graph_div = fig.to_html(full_html=True)

    # Return the plot as JSON
    return JsonResponse({'graph_div': graph_div, 'station_name': config_station_name, 'first_date_time': first_date_time, 'last_date_time': last_date_time, 'last_river_level': last_river_level})
