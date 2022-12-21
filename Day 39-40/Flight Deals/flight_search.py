import requests
from datetime import datetime, timedelta
from pprint import pprint

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

    def search_flight(self, code):
        today = datetime.today()
        dt_from = today + timedelta(days=1)
        dt_to = today + timedelta(days=180)
        parameters = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": dt_from.strftime("%d/%m/%Y"),
            "date_to": dt_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.departure_city = data["data"][0]["cityTo"]
        self.price = data["data"][0]["price"]
        return self.data


ft = FlightSearch()
pprint(ft.search_flight("IST"))