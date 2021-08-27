import requests
import json

url_items = "http://localhost:8001/todos"

new_item = {
    "id": 5,
    "content": "R",
    "completed": False
}

response = requests.post(url_items, data=new_item)

print(response.text)
