import os

from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_temp_status(temp):
    """
    Function to get temperature status.
    :param temp: int (temperature in Celsius)
    :return: str (status)
    """
    if temp <= 0:
        return f"{temp}C: A cold, isn’t it?\n"
    elif 0 < temp < 10:
        return f"{temp}C: Cool.\n"
    else:
        return f"{temp}C: Nice weather we’re having.\n"


while True:
    choice = int(input("What would you like to do?]\n 1. Enter temperature\n 2. Enter city name\n 3. Exit\n"))

    if choice == 1:
        try:
            temperature = float(input("Please enter the temperature in degrees Celsius: "))
            print(get_temp_status(temperature))
        except ValueError:
            print("Please enter a valid temperature in degrees")

    elif choice == 2:
        city_name = input(str("Please enter the city:\n"))

        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
            )

            data = response.json()
            temperature = data["main"]["temp"]

            print(f"\n{data['name']} - {get_temp_status(float(temperature))}"
                  f'Main weather: {data["weather"][0]["main"]}\n'
                  f'Humidity: {data["main"]["humidity"]}2\n'
                  f'Wind speed: {data["wind"]["speed"]} m/s\n'
                  f'Pressure: {data["main"]["pressure"]} hPa\n'
                  )
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    elif choice == 3:
        print("Thank you for using this app. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
