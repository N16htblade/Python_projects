from datetime import datetime
from time import time
import requests

#Request API - ISS coordonates
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)


#Request API with Parameters - Sunrise/Sunset
MY_LAT = 45.421532
MY_LONG = -75.697189

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

new_request = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
new_request.raise_for_status()
data = new_request.json()
sunrise = int(data["results"]["sunrise"].split("T")[1],split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1],split(":")[0])

time_now = datetime.now()
hour = time_now.hour()

print (sunrise, sunset, hour)
