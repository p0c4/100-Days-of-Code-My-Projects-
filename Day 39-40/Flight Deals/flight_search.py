import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint
from datetime import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "AMffCfH2tIVu89kHjyOj_DOVDzWNz3OD"


class FlightSearch:
    def __init__(self):
        self.headers = {"apikey": TEQUILA_API_KEY}
        self.data = {}

    def get_destination_code(self, city_name):
        parameters = {"term": city_name}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=self.headers)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def search_flight(self, code, origin_city_code):
        today = datetime.today()
        dt_from = today + timedelta(days=1)
        dt_to = today + timedelta(days=180)
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": code,
            "date_from": dt_from.strftime("%d/%m/%Y"),
            "date_to": dt_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "one_for_city": 1
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=datetime.fromtimestamp(data["route"][0]["dTime"]),
            return_date=datetime.fromtimestamp(data["route"][1]["dTime"])
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
