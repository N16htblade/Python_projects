import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = "email"
MY_PASS = "pass"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def check_possition():
    if MY_LAT - 5 <= iss_latitude < MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#--- Comment as email can't be sent due to security settings updated this year
# time_now = datetime.now()
# while True:
#     time.sleep(60)
#     if time_now.hour() > sunset and time_now.hour() < sunrise and check_possition() == True:
#         with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#             connection.starttls()
#             connection.login(user=MY_EMAIL, password=MY_PASS)
#             connection.sendmail(
#                 from_addr=MY_EMAIL, 
#                 to_addrs=to_email, 
#                 msg=f"Subject:Look Up!\n\nISS is overhead"
#                 )
