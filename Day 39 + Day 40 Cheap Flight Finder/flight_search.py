import requests
import os
from flight_data import FlightData

URL = "https://tequila-api.kiwi.com/"
API = os.environ["KIWI_API"]
ID = os.environ["KIWI_AFFILID"]

headers = {
    "apikey" : API
}

class FlightSearch:

    def get_IATA(self, city):
        parameters = {
            "term" : city,
        }
        request = requests.get(url=f"{URL}locations/query", params=parameters, headers=headers)
        request.raise_for_status()
        new_data = request.json()["locations"]
        code = new_data[0]["code"]
        return code

    def check_flight(self, departing_city, destination_city, from_time, to_time):
        flight_check_params = {
            "fly_from": departing_city,
            "fly_to": destination_city,
            "dateFrom": from_time,
            "dateTo": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0
        }

        request = requests.get(url=f"{URL}v2/search", params=flight_check_params, headers=headers)
        request.raise_for_status()
        
        try:
            data = request.json()["data"][0]
            print(f"{flight_data.destination_city}: £{flight_data.price}")
        except IndexError:
            flight_check_params["max_stopovers"] = 1
            request = requests.get(url=f"{URL}v2/search", params=flight_check_params, headers=headers)
            request.raise_for_status()
            data = request.json()
            
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data