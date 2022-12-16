import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")


parameters = {
    "lat": 49.282730,
    "lon": -123.120735,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/opencall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

condition_data = [hour["weather"][0]["id"] for hour in weather_slice]
for cd in condition_data:
    if cd < 700:
        will_rain = True

if will_rain:
    # In order to use pythonanywhere free account, we created this proxy client.
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂.",
        from_="+19295670794",
        to="***REMOVED***"
    )
    print(message.status)

