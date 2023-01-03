import time
import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfWCrJnpq9N91Bp_wsswLy5fToFSqHbuyD69VKCCkUu-ywqaQ/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Make a delicious soup. 

# with open("website.html") as file:
#         contents = file.read()

response = requests.get(ZILLOW_URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

anchor_address = soup.find_all(name="address")

address_list = [" ".join(anchor.getText().split()) for anchor in anchor_address]

print(len(address_list))

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

link_list = []
for a in soup.find_all('a', attrs={"class":"property-card-link"}, href=True):
    if a['href'] not in link_list:
        link_list.append(a['href'])
        print(a["href"])

price_data = soup.find_all("span", attrs={"data-test":"property-card-price"})
price_list = []
for price in price_data:
        price_text = price.string.split("+")[0].split("/")[0]
        price_list.append(price_text)

list_len = len(address_list)

for i in range(list_len):
        driver.get(FORM_URL)

        time.sleep(2)

        address_field =driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_field.send_keys(address_list[i])

        price_field =driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_field.send_keys(price_list[i])

        link_field =driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_field.send_keys(f"https://www.zillow.com{link_list[i]}")

        submit_button = driver.find_element(By.LINK_TEXT, "Submit")
        submit_button.click()
        

