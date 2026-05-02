from src.API_Fetch import fetch_weather
from src.clean_weather_Data import clean_weather_data
from src.aggregation import aggregate_weather_data

def main():
    fetch_weather()
    clean_weather_data()
    aggregate_weather_data()

if __name__ == "__main__":
    main()