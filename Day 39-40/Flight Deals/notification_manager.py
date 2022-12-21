import requests
import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, price, departure_from, arrival_destination, date_from, date_to):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{price} to fly from {departure_from} to {arrival_destination}, "
                 f"from {date_from} to {date_to}.",
            from_=os.environ.get("TWILIO_PHONE"), to=os.environ.get("MY_PHONE"))
