"""
Day 28 - Weather Data CLI
Retrieve current weather information for a city using Open-Meteo.
"""

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city):
    """Find a city's latitude, longitude, and location details."""
    try:
        response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])

        if not results:
            print(f"Error: No location found for '{city}'.")
            return None

        location = results[0]

        return {
            "name": location["name"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "country": location.get("country", "Unknown"),
            "admin1": location.get("admin1", ""),
        }

    except requests.exceptions.Timeout:
        print("Error: The location search timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"Location API HTTP error: {error}")

    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"Location API error: {error}")

    return None


def get_weather(latitude, longitude):
    """Retrieve current weather data for the given coordinates."""
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "is_day,"
                    "precipitation,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
                "timezone": "auto",
            },
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        current = data.get("current")

        if not current:
            print("Error: Current weather data is unavailable.")
            return None

        return {
            "time": current.get("time", "Unavailable"),
            "temperature": current.get("temperature_2m"),
            "feels_like": current.get("apparent_temperature"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "precipitation": current.get("precipitation"),
            "weather_code": current.get("weather_code"),
            "is_day": current.get("is_day"),
        }

    except requests.exceptions.Timeout:
        print("Error: The weather request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")

    except requests.exceptions.HTTPError as error:
        print(f"Weather API HTTP error: {error}")

    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"Weather API error: {error}")

    return None


def describe_weather(code):
    """Convert a WMO weather code into a readable description."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }

    return descriptions.get(code, "Unknown conditions")


def display_weather(location, weather):
    """Display weather information in a readable format."""
    print("\n" + "=" * 45)
    print("             CURRENT WEATHER")
    print("=" * 45)

    place = location["name"]

    if location["admin1"]:
        place += f", {location['admin1']}"

    place += f", {location['country']}"

    print(f"Location      : {place}")
    print(f"Observation  : {weather['time']}")
    print(
        f"Condition    : "
        f"{describe_weather(weather['weather_code'])}"
    )

    if weather["temperature"] is not None:
        print(f"Temperature  : {weather['temperature']} °C")

    if weather["feels_like"] is not None:
        print(f"Feels Like   : {weather['feels_like']} °C")

    if weather["humidity"] is not None:
        print(f"Humidity     : {weather['humidity']}%")

    if weather["wind_speed"] is not None:
        print(f"Wind Speed   : {weather['wind_speed']} km/h")

    if weather["precipitation"] is not None:
        print(f"Precipitation: {weather['precipitation']} mm")

    if weather["is_day"] is not None:
        print(
            "Day/Night    : "
            + ("Day" if weather["is_day"] == 1 else "Night")
        )

    print("=" * 45)


def main():
    """Run the interactive weather application."""
    print("=" * 45)
    print("             WEATHER DATA CLI")
    print("=" * 45)

    while True:
        city = input(
            "\nEnter a city name (or type 'exit' to quit): "
        ).strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Data CLI!")
            break

        if not city:
            print("Error: City name cannot be empty.")
            continue

        location = get_city_coordinates(city)

        if location is None:
            continue

        weather = get_weather(
            location["latitude"],
            location["longitude"],
        )

        if weather is not None:
            display_weather(location, weather)


if __name__ == "__main__":
    main()