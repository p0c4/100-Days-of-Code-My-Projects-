#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

flight_search = FlightSearch()
data_manager = DataManager()
data_manager.sheety_data()
sheet_data = data_manager.destination_data

# for row in sheet_data:
#     row["iataCode"] = flight_search.get_destination_code(row["city"])
#
# data_manager.destination_data = sheet_data
# data_manager.sheety_put()

for row in sheet_data:
    (city, price) = flight_search.search_flight(row["iataCode"])
    print(city, price)


