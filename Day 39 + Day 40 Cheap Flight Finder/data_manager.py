import requests
import os

SHEET_ENDPOINT = os.environ["SHEETY_FLIGHT_DEALS_ENDPOINT"]

class DataManager:

    def __init__(self):
        self.request = requests.get(url=f"{SHEET_ENDPOINT}/prices")
        self.request.raise_for_status()
        self.data = self.request.json()

    def get_data(self):
        self.prices = self.data["prices"]
        return self.prices

    def update_data(self):
        for city in self.data:
            sheet_input = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            update_price = requests.put(url=f"{SHEET_ENDPOINT}/prices/{city['id']}", json=sheet_input)
    
    def add_user(self, f_name, l_name, email):
        sheet_input = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }

        update_users = requests.post(url=f"{SHEET_ENDPOINT}/users", json=sheet_input)
        print (update_users.text)
    
    def get_users(self):
        self.users = requests.get(url=f"{SHEET_ENDPOINT}/users")
        self.users.raise_for_status()
        self.data = self.users.json()
        return self.data
