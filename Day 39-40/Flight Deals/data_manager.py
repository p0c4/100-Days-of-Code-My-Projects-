import requests



class DataManager:

    def __init__(self):
        self.destination_data = {}

    def sheety_data(self):
        response = requests.get(url="https://api.sheety.co/4be9234d65140ce0fbd2b369b8b4f933/flightDeals/prices")
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
                url=f"https://api.sheety.co/4be9234d65140ce0fbd2b369b8b4f933/flightDeals/prices/{i['id']}",
                json=parameters)
