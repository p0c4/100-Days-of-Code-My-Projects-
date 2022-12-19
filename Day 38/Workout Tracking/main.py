import requests
from datetime import datetime
import os

APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# With nutritionix API, calculate the calories
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutrition_parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 65,
    "height_cm": 168,
    "age": 45
}

response = requests.post(url=API_ENDPOINT, json=nutrition_parameters, headers=headers)
response.raise_for_status()
data_exercises = response.json()

exercise_name = (data_exercises["exercises"][0]["name"]).title()
exercise_duration = data_exercises["exercises"][0]["duration_min"]
exercise_calories = data_exercises["exercises"][0]["nf_calories"]


# Add a row to my sheet with Sheety API

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": os.environ.get("ENV_SHEETY_TOKEN")
}
sheety_parameters = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

post_workout = requests.post(url=os.environ.get("ENV_SHEET_ENDPOINT"), json=sheety_parameters, headers=sheety_headers)
post_workout.raise_for_status()

