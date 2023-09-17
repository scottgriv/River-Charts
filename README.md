<!-- Begin README -->

[![App Logo](./docs/images/banner_large.png)](http://scottgriv.pythonanywhere.com/)

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.10.13-244C6F?style=for-the-badge&logo=python" alt="Python Badge" />
    </a>
    <a href="https://www.djangoproject.com/">
        <img src="https://img.shields.io/badge/Django-4.2.5-0B4B33?style=for-the-badge&logo=django" alt="Django Badge" />
    </a>
    <a href="https://plotly.com/">
        <img src="https://img.shields.io/badge/Plotly-5.17.0-7976FF?style=for-the-badge&logo=plotly" alt="Plotly Badge" />
    </a>
    <a href="https://pandas.pydata.org/">
        <img src="https://img.shields.io/badge/Pandas-2.1.0-130753?style=for-the-badge&logo=pandas" alt="Pandas Badge" />
    </a>
    <br>
    <a href="mailto:scott.grivner@gmail.com">
        <img src="https://img.shields.io/badge/email-contact_me-red?style=for-the-badge&logo=gmail" alt="Email Badge" />
    </a>
    <a href="https://www.buymeacoffee.com/scottgriv">
        <img src="https://img.shields.io/badge/donate-buy_me_a_coffee-yellow?style=for-the-badge&logo=buymeacoffee&color=ffdd00" alt="BuyMeACoffee Badge" />
    </a>
</p>

-------

# River Charts
- River Charts is a `Python`, `Django`, `Plotly`, and `Pandas` web application that visualizes river data for a specific river/site/location.
- The line graph is driven by data pulled using an `API` from the [United States Geological Survey (USGS)](https://www.usgs.gov/).
- The data is updated with the most recent river height data every time the application is loaded.
- The data is captured by the USGS using a [gage height](#gage-height) sensor every 15 minutes.
- I recommend using the application on a desktop since the chart is interactive has a wider view, but it can be used on a mobile device as well.
- Visit the application [here](http://scottgriv.pythonanywhere.com/).

<div align="center">
  <img src="./docs/images/demo_1.gif" alt="Demo_1" style="width: 80%; margin: 5px;">
  <img src="./docs/images/demo_2.png" alt="Demo_2" style="width: 80%; margin: 5px;">
</div>

# Table of Contents
- [Background](#background)
- [Gage Height](#gage-height)
- [What's Inside?](#whats-inside)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Calling the API](#calling-the-api)
- [API Output Example](#api-output-example)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Credit](#credit)

# Background
Every year, my friends and I float 2 miles down the **Susquehanna River** in **NEPA** on river tubes (a 2 hour float). I wanted to create a web application that would allow us to visualize past river data in order to see the river height on the days we floated down the river. Some float dates, we still got together, but we didn't float due to the dangerous river levels. 
<span style="color:green"><b>Green</b></span> plots on the graph represent the dates we did float (with a "Floated" status of "Yes"), and 
<span style="color:red"><b>Red</b></span> plots represent the dates we did not float (with a "Floated" status of "No").

<div align="center">
    <a href="https://pawilds.com/journey/west-branch-susquehanna" target="_blank">
        <img src="./docs/images/susquehanna_river.jpg" style="width: 80%;"/>
    </a>
    <br>
    <i>West Branch, Susquehanna River.</i>
</div>

## Gage Height
<div align="center">
    <a href="https://waterdata.usgs.gov/blog/gage_height/" target="_blank">
        <img src="./docs/images/gage_height_1.jpg" style="width: 80%;"/>
    </a>
    <br>
    <a href="https://www.usgs.gov/media/images/usgs-stage-discharge-relation-example" target="_blank">
        <img src="./docs/images/gage_height_2.jpg" style="width: 80%;"/>
    </a>
    <br>
    <i>The application uses gage height data to plot the river height in feet on a given date.</i>
</span>
</div>

## What's Inside?
A quick look at the important files and directories you'll see in this project:

```bash
├── README.md # This file.
├── config.py # A file that contains sensitive information (excluded from this repository).
├── manage.py # A command-line utility that lets you interact with this Django project in various ways.
├── requirements.txt # A list of Python packages required to run this project.
├── River_Charts # A directory for the river_charts app.
│   ├── __init__.py # An empty file that tells Python that this directory should be considered a Python package.
│   ├── admin.py # A file that registers models to be displayed in the Django admin site.
│   ├── apps.py # A file that contains the application configuration.
│   ├── models.py # A file that contains the database models.
│   ├── tests.py # A file that contains the tests for the application.
│   ├── urls.py # A file that contains the URL declarations for the application.
│   └── views.py # A file that contains the application logic.
├── river_charts # The Django project directory.
│   ├── __init__.py # An empty file that tells Python that this directory should be considered a Python package.
│   ├── asgi.py # An entry-point for ASGI-compatible web servers to serve your project.
│   ├── settings.py # Settings/configuration for this Django project.
│   ├── urls.py # The URL declarations for this Django project.
│   └── wsgi.py # An entry-point for WSGI-compatible web servers to serve your project.
├── static # A directory for static files that are used in this Django project.
│   ├── css # A directory for CSS files.
│   │   └── styles.css # A CSS file that contains the styles for the application.
│   ├── data # A directory for data files.
│   │   └── river_charts.csv # A CSV file that contains the float dates for the application.
│   └── images # A directory for image files.
├── templates # A directory for HTML templates.
│   └── river_charts # A directory for HTML templates specific to the river_charts app.
│       ├── error.html # An HTML template that displays an error message.
│       └── index.html # An HTML template that displays the application.
├── views.py # A file that contains the application logic.
├── VERSION # A file that contains the current version of the application.
├── LICENSE # A file that contains the license for this project.
└── CREDITS # A file that contains the credits for this project.
```

## Dependencies
This project makes use of several libraries and frameworks:
- **Python:** For the application logic.
- **Django:** For web application functionality.
- **Plotly:** For creating interactive visualizations.
- **Pandas:** For data manipulation and analysis.
- **Requests:** For making `API` calls.
- **Python-Decouple:** For storing sensitive information in a `.env` file.
- *See [requirements.txt](requirements.txt) for a full list of dependencies.*

## Getting Started
To install and run the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/scottgriv/River-Charts
   ```
    - [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

2. Navigate to the project directory:
   ```bash
   cd [YOUR PROJECT DIRECTORY]
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
    - [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
    - [Activating a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

5. Install the required packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
    - [Installing Packages](https://packaging.python.org/tutorials/installing-packages/)

    **Note:** If you wany to generate a new `requirements.txt` file, run the following command:
    ```bash
    pip freeze > requirements.txt
    ```
    - [Requirements Files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

6. Run the Django server:
   ```bash
   python manage.py runserver
   ```
    - [Running the Django server](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#the-development-server)

Now, you can visit `http://127.0.0.1:8000/` in your browser to access the application.

## Configuration
- Edit `config.py` to add your own USGS `API` (and other) information.
    - [USGS API](https://waterservices.usgs.gov/rest/IV-Service.html)
    - [USGS API Documentation](https://help.waterdata.usgs.gov/faq/automated-retrievals)
- Toggle `USE_DUMMY_DATA` to `True` in `config.py` to use dummy data instead of the `API`.
    - This is useful for testing the application without making `API` calls.
- The float data plots are driven from a `.csv` file located in `static/data/river_charts.csv`.
    - This file can be edited to add/remove float dates.
    - The file is read in `views.py` and passed to the template as a `context` variable.

## Deployment
- The application is hosted [here](http://scottgriv.pythonanywhere.com/) on [PythonAnywhere](https://www.pythonanywhere.com/).
- The application is deployed using a `WSGI` configuration file.
    - [WSGI Configuration](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/)
- First, make sure you adjust your `settings.py` file `ALLOWED_HOSTS` to include your deployment host.
    - [Deploying Django](https://docs.djangoproject.com/en/3.2/howto/deployment/)
- Second, make sure you adjust your `settings.py` file `DEBUG` to `False` for production.
    - [Django Settings](https://docs.djangoproject.com/en/3.2/ref/settings/)
- Finnaly, be sure to create a `.env` file where you host your application to store your sensitive information (excluded from this repository).
    - [Python-Decouple](https://pypi.org/project/python-decouple/)

## Calling the API
To call the `API` and retrieve the data:

1. Make a GET request to: `http://nwis.waterservices.usgs.gov/nwis/...` (based on your requirements).
    - ex. `https://waterservices.usgs.gov/nwis/iv?format=json&sites=01533400&startDT=2015-07-01&endDT=2023-08-16&parameterCd=00065&siteStatus=active&siteType=ST`
2. Pass the necessary parameters in the request.
    - ex.
    ```python
    params = {
        "format": "json", # Set your interchange format.
        "sites": "01533400", # Site Code: Susquehanna River at Meshoppen, PA.
        "startDT": "2015-07-01", # Set the date you want to start collecting data from.
        "endDT": "2023-09-14", # This is based on the current date in the application.
        "parameterCd": "00065", # Parameter Code: Gage height, ft.
        "siteStatus": "active", # Selects sites based on whether or not they are currently active. Each USGS Water Science Center determines whether a site is active or inactive. The default is all (show both active and inactive sites).
        "siteType": "ST", # ST = A body of running water moving under gravity flow in a defined channel. The channel may be entirely natural, or altered by engineering practices through straightening, dredging, and (or) lining. An entirely artificial channel should be qualified with the "canal" or "ditch" secondary site type.
    }
    ```
    - [USGS Site Web Service](https://waterservices.usgs.gov/rest/Site-Service.html)
        - [Format](https://waterservices.usgs.gov/rest/Site-Service.html#format)
        - [Sites](https://waterservices.usgs.gov/rest/Site-Service.html#sites)
            - [Site Example](https://waterdata.usgs.gov/monitoring-location/01533400/#parameterCode=00065&period=P7D&showMedian=true)
        - [Parameter Codes](https://waterservices.usgs.gov/rest/Site-Service.html#parameterCd)
            - [List of Parameter Codes](https://help.waterdata.usgs.gov/parameter_cd?group_cd=PHY)
        - [Site Status](https://waterservices.usgs.gov/rest/Site-Service.html#siteStatus)
        - [Site Type](https://waterservices.usgs.gov/rest/Site-Service.html#siteType)
            - [List of valid Site Types](http://help.waterdata.usgs.gov/site_tp_cd)
    - [Codes and Parameters](https://help.waterdata.usgs.gov/codes-and-parameters)

3. Process the JSON response as demonstrated in the example above.

**Notes:** 
- The application uses the `API` to source data for the graph. If the `API` is down, the graph will not render.
- The `API` is rate limited to 30 calls per minute. If you exceed this limit, you will receive a `429` error.
- Errors are handled in the application by redirecting the user to an error page with the appropriate error message.
<div align="center">
    <img src="./docs/images/error_page_example.jpg" style="width: 80%;"/>
    <br>
    <i>Example of an Error Page.</i>
</div>

## API Output Example
The application sources data using an `API` that returns `JSON` output. Here's an example of what the API response looks like:

```json
{
    "name": "ns1:timeSeriesResponseType",
    ...
    "timeSeries": [
        {
            "sourceInfo": {
                "siteName": "Susquehanna River at Meshoppen, PA",
                ...
            },
            "variable": {
                "variableName": "Gage height, ft",
                ...
            },
            "values": [
                {
                    "value": [
                        {
                            "value": "15.13",
                            "dateTime": "2015-07-01T00:00:00.000-04:00"
                        },
                        ...
                    ]
                }
            ]
        }
    ]
}
```
(For the sake of brevity, the full output is abbreviated with `...`)

## Disclaimer
The data provided by this application is sourced from the [USGS](https://www.usgs.gov/). It's subject to revision, and for more information, please refer to their [official disclaimer](http://waterdata.usgs.gov/nwis/help/?provisional).

## License
- **River Charts** is released under the terms of the **GNU General Public License, version 3 (GPLv3)**. The GPLv3 is a "copyleft" license, ensuring that derivatives of the software remain open source and under the GPL.
- For more details and to understand all requirements and conditions, see the [LICENSE](LICENSE) file in this repository.

## Credit
**Author:** Scott Grivner <br>
**Email:** scott.grivner@gmail.com <br>
**Website:** [scottgrivner.dev](https://www.scottgrivner.dev) <br>
**Reference:** [Main Branch](https://github.com/scottgriv/River-Charts) <br>
<div align="center">
    <a href="https://github.com/scottgriv/River-Charts" target="_blank">
        <img src="./docs/images/app_icon.png" width="100" height="100"/>
    </a>
</div>

<!-- End README -->
