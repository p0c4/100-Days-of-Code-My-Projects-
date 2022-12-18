import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_KEY")
}
parameters_news = {
    "q": "tesla",
    "language": "en",
    "apiKey": os.environ.get("NEWS_API")
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response_stock.raise_for_status()

stock_data = response_stock.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
close_yesterday = float(data_list[0]["4. close"])
close_bf_yesterday = float(data_list[1]["4. close"])

diff = close_yesterday - close_bf_yesterday
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_yesterday_percent = round(diff / close_yesterday * 100)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

if abs(diff_yesterday_percent) > 5:
    message = client.messages.create(body="Get News!", from_=os.environ.get("TWILIO_PHONE"),
                                     to=os.environ.get("MY_PHONE"))
    print(message.status)
else:
    response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    response_news.raise_for_status()
    news = response_news.json()["articles"][:3]
    [(client.messages.create(
        body=f"{STOCK}: {up_down}{diff}%\nHeadline: {new['title']} \nBrief: {new['description']}", 
        from_=os.environ.get("TWILIO_PHONE"), 
        to=os.environ.get("MY_PHONE"))) for new in news]