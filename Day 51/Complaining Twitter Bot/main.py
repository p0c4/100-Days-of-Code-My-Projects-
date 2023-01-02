import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 200
PROMISED_UP = 200
TWITTER_EMAIL = os.environ.get("ENV_TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("ENV_TWITTER_PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.promied_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        #Click Log in Button.
        go_button = self.driver.find_element(By.LINK_TEXT, "Go")
        go_button.click()
        
        #Wait for speed caltulation period.
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH, 
        "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.up = self.driver.find_element(By.XPATH, 
        "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/pocaispoca_")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, 
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        
        #Click Tweet Button.
        tweet_button = self.driver.find_element(By.XPATH, "G/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        tweet_button.click()

        #Create Tweet.
        tweet_area = self.driver.find_element(By.XPATH, 
        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_area.send_keys(f"Hey @serviceprovider, why is my internet speed {self.down} down / {self.up} up when I pay for 250 down/ 250 up?")

        #Send Tweet
        send_tweet_button = self.driver.find_element(By.XPATH, 
        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span")
        send_tweet_button.click()

        time.sleep(2)
        self.driver.quit()




bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
time.sleep(2)
if bot.promied_down < bot.down or bot.promised_up < bot.up:
    bot.tweet_at_provider()

