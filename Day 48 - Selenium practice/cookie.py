from cgitb import reset
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chorme_driver_path = "C:\PyLearning\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chorme_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

while True:
    t_end = time.time() + 5
    while time.time() < t_end:
        main_event = driver.find_element(By.ID, "cookie").click()

    money = driver.find_element(By.ID, "money").text
    money_value = int(''.join([i for i in money if i.isdigit()]))

    while money_value > 0:
        money = driver.find_element(By.ID, "money").text
        money_value = int(''.join([i for i in money if i.isdigit()]))

        cursor = driver.find_element(By.CSS_SELECTOR, '#buyCursor b').text
        cursor_value = int(''.join([i for i in cursor if i.isdigit()]))
        print (f"My Money = {money_value}")
        print (f"Cursor = {cursor_value}")
        
        if money_value > cursor_value:
            purchase = driver.find_element(By.ID, "buyCursor")
            purchase.click()
        else:
            break
