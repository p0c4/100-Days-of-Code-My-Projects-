from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

PRODUCT_URL = "https://www.python.org/"

driver.get(PRODUCT_URL)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")


event_names_list = []
for event in event_names:
    event_names_list.append(event.text)

event_dates_list = []
for event in event_dates:
    event_dates_list.append(event.text)

events_dict = {}
for i in range(len(event_dates_list)):
    events_dict[i] = {"date": event_dates_list[i], "name": event_names_list[i]}

print(events_dict)


