from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from users import Users

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users = Users()

DEPARTING_CITY = "LON"
sheet_data = data_manager.get_data()


users.create_user()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_IATA(row["city"])

    data_manager.data = sheet_data
    data_manager.update_data()

from_time = (datetime.now() + timedelta(days=1)).strftime(r"%d/%m/%Y")
to_time = (datetime.now() + timedelta(days=(6*30))).strftime(r"%d/%m/%Y")

for city in sheet_data:
    flight = flight_search.check_flight(
        DEPARTING_CITY,
        city["iataCode"],
        from_time,
        to_time
        )

    if flight is None:
        continue

    if flight.price < city["lowestPrice"]:
        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop overs, via {flight.via_city}."
        
        notification_manager.sendsms(message)
        
        user_data = data_manager.get_users()
        to_email = user_data["email"]
        link_to_flight = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_email(to_email, message, link_to_flight)