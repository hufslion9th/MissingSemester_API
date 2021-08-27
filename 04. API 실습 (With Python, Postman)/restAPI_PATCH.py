import requests
import json

url_items = "http://localhost:8001/todos/4"

new_item = {"content": "Dart"}

response = requests.patch(url_items, data=new_item)

print(response.text)
