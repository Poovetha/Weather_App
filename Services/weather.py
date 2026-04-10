import os

import requests
from  dotenv import load_dotenv
load_dotenv()
WURL = os.getenv("WURL")

class Weather:

    def get_weather(self, city):
        try:

            url = f"{WURL}{city}?format=j1"
            response = requests.get(url, timeout=5)

            data = response.json()

            current = data["current_condition"][0]

            result = {
                "city": city.title(),
                "temperature": current["temp_C"],
                "description": current["weatherDesc"][0]["value"],
                "humidity": current["humidity"],
                "wind": current["windspeedKmph"]
            }

            return result

        except :
            print("Something went wrong , Please check your internet connection and try again")
            return None