from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chorme_driver_path = "C:\PyLearning\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chorme_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
test_end = time.time() + 60 * 5

def run_the_store():
    stores = ['buyShipment', 'buyMine', 'buyFactory'] # ',buyGrandma', 'buyCursor'
    for store in stores:
        attempt_buy(store)
    
def attempt_buy(element):
    time.sleep(0.05)
    money = driver.find_element(By.ID, "money").text
    money_value = int(''.join([i for i in money if i.isdigit()]))

    item = driver.find_element(By.CSS_SELECTOR, f'#{element} b').text
    item_value = int(''.join([i for i in item if i.isdigit()]))

    if money_value > item_value:
        purchase = driver.find_element(By.ID, element)
        purchase.click()


while time.time() < test_end:
    t_end = time.time() + 5
    while time.time() < t_end:
        main_event = driver.find_element(By.ID, "cookie").click()

    run_the_store()

score = driver.find_element(By.ID, "cps").text
print (f"Final cps: {score}")

driver.close()