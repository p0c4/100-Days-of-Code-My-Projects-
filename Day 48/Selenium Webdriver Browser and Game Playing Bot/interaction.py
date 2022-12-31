from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

PRODUCT_URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(PRODUCT_URL)

statistics_article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

# statistics_article_count.click()

# all_potals = driver.find_element(By.LINK_TEXT, "All portals")
# all_potals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)


#------ Filling Out a Form ------#
name_input = driver.find_element(By.NAME, 'fname')
name_input.send_keys("Test")
name_input.send_keys(Keys.TAB)

surname_input = driver.find_element(By.NAME, 'lname')
surname_input.send_keys("Test")
surname_input.send_keys(Keys.TAB)

email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys("Test@test.com")

sign_up = driver.find_element(By.CSS_SELECTOR, 'form button')
sign_up.click()