#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.sheety_data()


ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for destination in sheet_data:
        destination["iataCode"] = flight_search.get_destination_code(destination["city"])
    data_manager.destination_data = sheet_data
    data_manager.sheety_put()

for destination in sheet_data:
    flight = flight_search.search_flight(destination["iataCode"], ORIGIN_CITY_IATA)

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
