import random, pandas, smtplib
import datetime as dt

MY_EMAIL = ""
MY_PASS = ""
PATH = "C:/PyLearning/projects/Day 32 - Automated email"
now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv(PATH+"/birthdays.csv")
birthdays = data.to_dict(orient="records")

for item in birthdays:
    if day == item["day"] and month == item["month"]:
        name = item["name"]
        to_email = item["email"]
        with open (PATH + f"/letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)

#--- Comment as email can't be sent due to security settings updated this year
#       with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#           connection.starttls()
#           connection.login(user=MY_EMAIL, password=MY_PASS)
#           connection.sendmail(
#               from_addr=MY_EMAIL, 
#               to_addrs=to_email, 
#               msg=f"Subject:Happy Birthday!\n\n{letter}"
#               )