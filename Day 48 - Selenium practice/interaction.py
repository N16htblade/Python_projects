from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chorme_driver_path = "C:\PyLearning\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chorme_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print (article_count.text)


driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Misa")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Junior")
email = driver.find_element(By.NAME, "email")
email.send_keys("StarWars@gmail.com")
accept = driver.find_element(By.CSS_SELECTOR, "button")
accept.click()

#driver.close()


