![App Logo](./docs/images/banner_large.png)

[![Swift](https://img.shields.io/badge/Swift-5.7-orange?style=for-the-badge&logo=pandas)](https://swiftversion.net/)
[![iOS](https://img.shields.io/badge/iOS-16.2-red?style=for-the-badge&logo=django)](https://support.apple.com/en-us/HT213407)
[![iOS](https://img.shields.io/badge/iOS-16.2-red?style=for-the-badge&logo=plotly)](https://support.apple.com/en-us/HT213407)
[![watchOS](https://img.shields.io/badge/watchOS-9.1-green?style=for-the-badge&logo=python)](https://support.apple.com/en-us/HT213436)
[![Email](https://img.shields.io/badge/email-contact_me-9cf?style=for-the-badge&logo=gmail)](mailto:scott.grivner@gmail.com)
[![BuyMeACoffee](https://img.shields.io/badge/donate-buy_me_a_coffee-yellow?style=for-the-badge&logo=buymeacoffee&color=ffdd00)](https://www.buymeacoffee.com/scottgriv)

-------

# River Charts

*NOTE* THIS README IS STILL WORK IN PROGRESS
python3 manage.py runserver 

River Charts is a project designed to visualize river data. It utilizes data from both the [National Weather Service (NWS)](https://www.weather.gov/) and [United States Geological Survey (USGS)](https://www.usgs.gov/).

## API Output Example

The application sources data using an API that returns JSON output. Here's an example of what the API response looks like:

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

## Calling the API

To call the API and retrieve the data:

1. Make a GET request to: `http://nwis.waterservices.usgs.gov/nwis/...` (based on your requirements).
2. Pass the necessary parameters in the request.
3. Process the JSON response as demonstrated in the example above.

## Local Installation and Running

To install and run the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone [YOUR REPO LINK]
   ```

2. Navigate to the project directory:
   ```bash
   cd [YOUR PROJECT DIRECTORY]
   ```

3. Install the required packages:
   ```bash
   pip install django pandas plotly requests python-decouple
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```

Now, you can visit `http://127.0.0.1:8000/` in your browser to access the application.

## Dependencies

This project makes use of several libraries and frameworks:
- Django: For web application functionality.
- Pandas: For data manipulation and analysis.
- Plotly: For creating interactive visualizations.

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
