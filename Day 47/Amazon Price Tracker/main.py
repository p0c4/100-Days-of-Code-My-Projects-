import requests
from bs4 import BeautifulSoup
import os
import smtplib

E_MAIL = os.environ.get("ENV_EMAIL")
PASSWORD = os.environ.get("ENV_EMAIL_API_PASSWORD")

PRODUCT_URL = "https://www.amazon.ca/Staging-Product-Receive-and-Stow/dp/B09RX3N8Z6?ref_=Oct_DLandingS_D_5bc2c225_66"
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

response = requests.get(PRODUCT_URL, headers=headers)
product_html = response.text

soup = BeautifulSoup(product_html, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
product_subject = soup.find(name="span", class_="a-size-large product-title-word-break", id="productTitle").getText().strip()

price = float(f"{price_whole}{price_fraction}")


if price <= 40:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=E_MAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=E_MAIL,
                    to_addrs=E_MAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{product_subject} is now ${price}.\n{PRODUCT_URL}"
                )