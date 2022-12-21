import os
import requests

SHEETY_ENDPOINT = os.environ.get("ENV_SHEETY_FLIGHT_ENDPOINT")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def sheety_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        d_data = response.json()
        self.destination_data = d_data["prices"]
        return self.destination_data

    def sheety_put(self):
        for i in self.destination_data:
            parameters = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_ENDPOINT}/{i['id']}",
                json=parameters)
