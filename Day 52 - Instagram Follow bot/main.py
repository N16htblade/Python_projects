from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

SIMILAR_ACCOUNT = "bloombergbusiness"
CHORME_DRIVER_PATH = "C:\PyLearning\dev\chromedriver.exe"
EMAIL = os.environ["FACEBOOK_EMAIL"]
PASS = os.environ["FACEBOOK_PASS"]

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        # sign in using Username and Password
        signIn_user = self.driver.find_element(By.NAME, 'username')
        signIn_user.send_keys(EMAIL)
        signIn_pass = self.driver.find_element(By.NAME, 'password')
        signIn_pass.send_keys(PASS)
        signIn_pass.send_keys(Keys.ENTER)

        # wait and dismiss notifications
        time.sleep(4)
        notification1 = self.driver.find_element(By.XPATH , '//button[text()="Not Now"]')
        notification1.send_keys(Keys.ENTER)
        time.sleep(1)
        notification2 = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        notification2.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(2)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/')
        
        # find popup window and scroll to bottom 
        time.sleep(5)
        popup = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)


    def follow(self):
        # index all available follow buttons and click on them in order
        followers = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano button')
        for follower in followers:
            if follower.text == "Follow":
                follower.click()
                time.sleep(2)


bot = InstaFollower(CHORME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()