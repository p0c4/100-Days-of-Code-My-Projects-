import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("ENV_TEQUILA_API_KEY")


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
            parameters["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=self.headers,
                params=parameters,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=datetime.fromtimestamp(data["route"][0]["dTime"]),
                return_date=datetime.fromtimestamp(data["route"][2]["dTime"]),
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=datetime.fromtimestamp(data["route"][0]["dTime"]),
                return_date=datetime.fromtimestamp(data["route"][1]["dTime"])
            )
            return flight_data
