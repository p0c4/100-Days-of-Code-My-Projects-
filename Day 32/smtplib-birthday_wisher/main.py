import smtplib
import datetime as dt
import random
import pandas


password = "xxxxxxxxx" # my e-mail password
my_email = "test@gmail.com"
LETTERS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

now = dt.datetime.now()
month = now.month
day = now.day

data_file = pandas.read_csv("birthdays.csv")
birthday_people_list = data_file.to_dict(orient="records")
for bd_dict in birthday_people_list:
    if bd_dict["day"] == day and bd_dict["month"] == month:
        random_letter = random.choice(LETTERS)
        name = bd_dict["name"]
        with open(random_letter) as data_file:
            temp_letter = data_file.read()
            bd_letter = temp_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bd_dict["email"],
                msg=f"Subject:Happy Birthday dear {name}\n\n{bd_letter}"
            )
