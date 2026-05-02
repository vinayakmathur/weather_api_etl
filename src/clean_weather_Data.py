
import pandas as pd
import requests
import json
import os

with open("data/raw_weather.json", "r") as f:
    data = json.load(f)

# Extract hourly weather data
hourly = data["hourly"]

# Create clean dataframe
df = pd.DataFrame({
    "datetime": hourly["time"],
    "temperature_c": hourly["temperature_2m"],
    "humidity_percent": hourly["relative_humidity_2m"]
})

# Convert datetime column
df["datetime"] = pd.to_datetime(df["datetime"])

# Optional extra useful columns
df["date"] = df["datetime"].dt.date
df["hour"] = df["datetime"].dt.hour

# Save clean CSV
df.to_csv("data/clean_weather.csv", index=False)

print("Clean weather data saved to data/clean_weather.csv")
print(df.head())