from selenium import webdriver
from selenium.webdriver.common.by import By

chorme_driver_path = "C:\PyLearning\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chorme_driver_path)
driver.get("https://www.python.org/")

widget = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
dates = widget.find_elements(By.TAG_NAME, "time")
names = widget.find_elements(By.TAG_NAME, 'a')
events = {}

for x in range(len(dates)):
    events[x] = {
        'time': "2022-" + dates[x].text, 
        'name': names[x].text
        }

print (events)


driver.close()