import pandas as pd

# Load cleaned data
df = pd.read_csv("data/clean_weather.csv")

# Make sure datetime is parsed properly
df["datetime"] = pd.to_datetime(df["datetime"])

# Daily aggregation
daily_summary = (
    df.groupby("date")
      .agg(
          min_temp_c=("temperature_c", "min"),
          max_temp_c=("temperature_c", "max"),
          avg_temp_c=("temperature_c", "mean"),
          avg_humidity_percent=("humidity_percent", "mean")
      )
      .reset_index()
)

# Round numeric values
daily_summary["avg_temp_c"] = daily_summary["avg_temp_c"].round(2)
daily_summary["avg_humidity_percent"] = daily_summary["avg_humidity_percent"].round(2)

# Save analytics-ready table
daily_summary.to_csv("data/daily_weather_summary.csv", index=False)

print("Daily summary saved to data/daily_weather_summary.csv")
print(daily_summary.head())