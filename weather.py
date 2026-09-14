import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API_URL = "https://wttr.in/{city}?format=j1"
TIMEOUT = 10


def fetch_weather(city: str) -> dict:
    """Retrieve current weather data for a city."""
    url = API_URL.format(city=quote(city))
    request = Request(
        url,
        headers={"User-Agent": "Command-Line-Weather-Fetcher/1.0"},
    )

    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        if exc.code == 404:
            raise ValueError(
                f"Weather data could not be found for '{city}'."
            ) from exc
        raise ConnectionError(
            "The weather service returned an unexpected error."
        ) from exc
    except (URLError, TimeoutError):
        raise ConnectionError(
            "Unable to connect to the weather service. "
            "Please check your internet connection and try again."
        ) from None
    except json.JSONDecodeError:
        raise ConnectionError(
            "The weather service returned an invalid response."
        ) from None


def display_weather(city: str, data: dict) -> None:
    """Display the required weather information."""
    current = data["current_condition"][0]

    description = current["weatherDesc"][0]["value"]
    temperature = current["temp_C"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]

    print("\n" + "=" * 48)
    print(f"              CURRENT WEATHER")
    print("=" * 48)
    print(f"City          : {city.title()}")
    print(f"Description   : {description}")
    print(f"Temperature   : {temperature} °C")
    print(f"Humidity      : {humidity}%")
    print(f"Wind Speed    : {wind_speed} km/h")
    print("=" * 48)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch current weather for a city."
    )
    parser.add_argument(
        "city",
        nargs="*",
        help="City name, for example: Hyderabad",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    city = " ".join(args.city).strip()

    if not city:
        try:
            city = input("Enter city name: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram cancelled.")
            return 0

    if not city:
        print("Error: Please enter a city name.")
        return 1

    try:
        weather_data = fetch_weather(city)
        display_weather(city, weather_data)
        return 0
    except ValueError as exc:
        print(f"\nError: {exc}")
        print("Please check the city name and try again.")
        return 1
    except ConnectionError as exc:
        print(f"\nError: {exc}")
        return 1
    except (KeyError, IndexError, TypeError):
        print(
            "\nError: The weather service returned unexpected data. "
            "Please try again later."
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
