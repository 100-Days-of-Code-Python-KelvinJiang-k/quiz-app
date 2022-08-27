import html
import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameter)
question_data = response.json()["results"]

# Unescape html entities in question text
for index, question in enumerate(question_data):
    question_data[index]["question"] = html.unescape(question_data[index]["question"])
