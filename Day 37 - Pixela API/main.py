from urllib import response
import requests

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = ""
TOKEN = ""

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print (response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

ID = "graph1"

graph_params = {
    "id":ID,
    "name":"Coding time",
    "unit":"min",
    "type":"float",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print (response.text)

post_value_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}"

value_config = {
    "date": "20220815",
    "quantity": "1",
}

response = requests.post(url=post_value_endpoint, json=value_config, headers=headers)
print (response.text)