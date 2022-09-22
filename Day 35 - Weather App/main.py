import requests
from twilio.rest import Client


OPM_URL = "https://api.openweathermap.org/data/2.5/onecall"
OPM_API_KEY = "9dbbb28205d83be71e11f61f28678178"
account_sid = "---"
auth_token = "---"

opm_parameters = { 
    "lat":45.421532,
    "lon":-75.697189,
    "exclude":"current,mintely,daily",
    "appid":OPM_API_KEY,
    }

request = requests.get(OPM_URL, params=opm_parameters)
request.raise_for_status()
weather_data = request.json()

weather_slice = weather_data["hourly"][7:19]
will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Bring an umbrella.",
                     from_='+11112223333',
                     to='+18190000000'
                 )
    print (message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Looks like a sunny day today.",
                     from_='+11112223333',
                     to='+18190000000'
                 )
    print (message.status)