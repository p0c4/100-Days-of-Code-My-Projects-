import smtplib
import datetime as dt
import random


password = "xxxxxxx"
my_email = "test@gmail.com"

now = dt.datetime.now()
day_of_week = now.weekday()  # Gives number value and starts with 0. 0 = Monday, 1 = Tuesday

if day_of_week == 0:
    with open("quotes.txt") as data_file:
        quotes_list = data_file.readlines()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@yandex.com",
            msg=f"Subject:Quotes of the Day\n\n{random.choice(quotes_list)}"
        )

