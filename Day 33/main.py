import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.289887
MY_LNG = -122.755930
PASSWORD = "leqiorwgsslkfnvx"
MY_EMAIL = "codehisla@gmail.com"


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json?lat=49.289887&lng=-122.755930", params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(data["results"]["sunset"])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print(time_now.hour, sunset, sunrise)
        return True


while True:
    time.sleep(60)
    if is_nighttime() and is_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS is Close\n\nGo out and look at sky, Maybe you can see the ISS :)"
            )
