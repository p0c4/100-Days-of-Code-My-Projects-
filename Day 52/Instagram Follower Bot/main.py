import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


INSTAGRAM_USERNAME = os.environ.get("ENV_INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("ENV_INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = "ducane_cundioglu"

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, 
        '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, 
        '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')

        username.send_keys(INSTAGRAM_USERNAME)
        password.send_keys(INSTAGRAM_PASSWORD)

        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, 
        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        
        followers_button =  self.driver.find_element(By.XPATH, 
        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        followers_button.click()

        time.sleep(2)

    def follow(self):
        list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for person in list_of_people:
            try:
                if person.text == "Follow":
                    person.click()
                    time.sleep(5)
                print(len(list_of_people))
                self.driver.execute_script("argument[0].scrollIntoView(true);", list_of_people[-1])
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()