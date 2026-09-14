# Command-Line Weather Fetcher

A simple command-line application that retrieves and displays current meteorological conditions for a user-specified city using the free public wttr.in weather API.

## Features

- Accepts a city name through a command-line prompt or argument.
- Uses a free public weather endpoint with no API key required.
- Displays:
  - Temperature
  - Humidity
  - Wind speed
  - General weather description
- Handles invalid city input and network/API failures with friendly messages.

## Requirements

- Python 3.9 or later
- Internet connection

No third-party Python packages are required.

## Setup

Clone the repository and open the project directory:

```bash
git clone https://github.com/AkshayMamillapalli/weather-fetcher.git
cd weather-fetcher
```

```bash
pip install -r requirements.txt
```

There are currently no external Python packages to install.

## Run the Application

### Interactive prompt

```bash
python weather.py
```

Then enter a city:

```text
Enter city name: Hyderabad
```

### Command-line argument

```bash
python weather.py Hyderabad
```

For a city containing spaces:

```bash
python weather.py New York
```

## Example Output

```text
================================================
              CURRENT WEATHER
================================================
City          : Hyderabad
Description   : Partly cloudy
Temperature   : 28 °C
Humidity      : 74%
Wind Speed    : 11 km/h
================================================
```

The values shown above are illustrative. Live weather values are retrieved from the API when the application runs.

## Error Handling

### Invalid location

Run:

```bash
python weather.py xyzabc-not-a-city
```

The program displays a friendly error instead of crashing:


Error: Weather data could not be found for 'xyzabc-not-a-city'.
Please check the city name and try again.


### Network failure

If the weather service cannot be reached, the application catches the connection failure and displays a clear message asking the user to check their internet connection.

## API

The application uses the public `wttr.in` endpoint:

```text
https://wttr.in/{city}?format=j1
```

No API key is required.

## Demo Video

The required **1–2 minute walkthrough video** demonstrates:

1. Starting the application.
2. Entering a valid city name.
3. Viewing the fetched temperature, humidity, wind speed, and weather description.
4. Testing an invalid location and showing the friendly error.

```html
<video src="./demo.mp4" controls width="800"></video>
```