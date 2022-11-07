from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

PROMISED_DOWN = 500
PROMISED_UP = 100
CHORME_DRIVER_PATH = "C:\PyLearning\dev\chromedriver.exe"
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
TWITTER_PASS = os.environ["TWITTER_PASS"]


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        
        time.sleep(2)
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()

        time.sleep(40)
        dismiss_notification = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        dismiss_notification.click()

        time.sleep(1)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        time.sleep(2)

        signIn = self.driver.find_element(By.NAME, 'text')
        signIn.send_keys(TWITTER_USERNAME)
        signIn.send_keys(Keys.ENTER)

        time.sleep(2)
        signIn = self.driver.find_element(By.NAME, 'password')
        signIn.send_keys(TWITTER_PASS)
        signIn.send_keys(Keys.ENTER)

        time.sleep(2)
        message = f"Hey Internet Provider, why is my instenr speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        message_area = self.driver.find_element (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        message_area.send_keys(message)

        time.sleep(1)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


bot = InternetSpeedTwitterBot(CHORME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()