import requests
import json
import os

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=28.61"
    "&longitude=77.23"
    "&hourly=temperature_2m,relative_humidity_2m"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/raw_weather.json", "w") as f:
    json.dump(data, f, indent=4)

print("Weather data saved to data/raw_weather.json")
