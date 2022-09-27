from twilio.rest import Client
import os
import datetime as dt
import smtplib

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = ""
TWILIO_VERIFIED_NUMBER = os.environ["MY_PHONE"]
MY_EMAIL = "testing@yahoo.com"
MY_PASS = "notmypass"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
    
    def send_email(self, to_email, email_body, flight_link):
        pass
        #--- Comment as email can't be sent due to security settings updated this year
        #   with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        #       connection.starttls()
        #       connection.login(user=MY_EMAIL, password=MY_PASS)
        #       connection.sendmail(
        #           from_addr=MY_EMAIL, 
        #           to_addrs=to_email, 
        #           msg=f"Subject:New Low Price Flight!\n\n{email_body}\n{flight_link}}".encode(UTF-8)
        #           )