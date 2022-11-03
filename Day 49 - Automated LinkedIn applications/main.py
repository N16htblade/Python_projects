from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

ACCOUNT_EMAIL = os.environ["GMAIL_USERNAME"]
ACCOUNT_PASS = os.environ["LINKEDIN_PASS"]

chorme_driver_path = "C:\PyLearning\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chorme_driver_path)
driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3336161621&f_AL=true&geoId=101174742&keywords=software%20engineer&location=Canada&refresh=true")

time.sleep(2)
signIn = driver.find_element(By.LINK_TEXT, "Sign in")
signIn.click()

time.sleep(1)
username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASS)
password.send_keys(Keys.ENTER)

time.sleep(3)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(3)

    save_button = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button')
    save_button.click()
    
