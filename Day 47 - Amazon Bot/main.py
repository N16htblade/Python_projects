from bs4 import BeautifulSoup
import requests
import smtplib

URL = ("https://www.amazon.ca/NVIDIA-GeForce-Express-Graphics-Platinum" \
    "/dp/B097PZT7J3/ref=sr_1_6?crid=3ETG8WKQCH1DQ&keywords=nvidia&qid=1663871366&"\
    "sprefix=nvidia%2Caps%2C80&sr=8-6")
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
}
MY_EMAIL = ""
MY_PASS = ""

target_price = 800

response = requests.get(URL, headers=headers)
data = BeautifulSoup(response.text, "html.parser")
price = data.find(name="span", class_="a-price-whole").get_text()
current_price = int((price.split(",")[0] + price.split(",")[1]).strip("."))

if current_price < target_price:
    message = f"Your 'VIDIA - GeForce RTX 3070 Ti' is now bellow your requested price, currently at ${current_price}."

#--- Comment as email can't be sent due to security settings updated this year
#       with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#           connection.starttls()
#           connection.login(user=MY_EMAIL, password=MY_PASS)
#           connection.sendmail(
#               from_addr=MY_EMAIL, 
#               to_addrs=to_email, 
#               msg=f"Subject:Amazon Discount!\n\n{message}"
#               )