import requests

parameters={
    "amount":10,
    "type":"boolean",
    "category":18,
}

data = requests.get(url="https://opentdb.com/api.php?", params=parameters)
data.raise_for_status()

new_questions = data.json()
question_data = new_questions["results"]