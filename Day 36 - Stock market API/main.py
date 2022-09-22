import requests
import itertools
from twilio.rest import Client
import os


#Stock API info
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = "CFWNDYUFRFIYD4WT"
STOCK_URL = "https://www.alphavantage.co/query"

stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact", #compact last 100 data points, or full 20+years
    "apikey":STOCK_API_KEY,
}

#News API info
NEWS_API = "66884527bbde412e97479520bb65061d"
NEWS_URL = "https://newsapi.org/v2/everything"

news_parameters={
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API
}

#Twillio phone info
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


request = requests.get(STOCK_URL, params=stock_parameters)
request.raise_for_status()
data = request.json()["Time Series (Daily)"]

#Calculate difference between previous day close and the day before
compact_data = [value for (key, value) in data.items()]
new_price = float(compact_data[0]["4. close"])
old_price = float(compact_data[1]["4. close"])
difference = abs(new_price - old_price)
percent_difference = float("{:.2f}".format(difference/old_price*100))

#if difference is higher then if statement, grab the 1st news topic on company and send it as a SMS
if difference > 1:
    news_request = requests.get(NEWS_URL, params=news_parameters)
    news_request.raise_for_status()
    news_data = news_request.json()
    relevant = news_data["articles"]
    headline = relevant[0]["title"]
    news_body = relevant[0]["description"]
    print (headline)

    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #         body=f"DIS: 🔺{percent_difference}%\nHeadline: {headline}\nBrief: {news_body}",
    #         from_='+111111111',
    #         to='+12222222'
    #             )
    # print (message.status)