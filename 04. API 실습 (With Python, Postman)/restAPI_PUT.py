import requests
import json

url_items = "http://localhost:8001/todos/4"

new_item = {
    "id": 4,
    "content": "CPP",
    "completed": False
}
response = requests.put(url_items, data=new_item)

print(response.text)
