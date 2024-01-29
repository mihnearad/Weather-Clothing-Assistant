import requests
from dotenv import load_dotenv
import os 

load_dotenv()

def get_weather_info():
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Replace 'Namur' with the actual city name and 'BE' with the country code for Belgium
    city_name = 'Namur'
    country_code = 'BE'

    # API endpoint URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Convert temperature from Kelvin to Celsius
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15

        # Access and print relevant information from the response
        description = data['weather'][0]['description']
        question = (f"How should I dress for {temperature_celsius:.2f}°C with {description}?")
        return question
    else:
        # Print an error message if the request was not successful
        return f'Error: {response.status_code}, {response.text}'

# If the script is run directly, print the weather information
if __name__ == "__main__":
    print(get_weather_info())
