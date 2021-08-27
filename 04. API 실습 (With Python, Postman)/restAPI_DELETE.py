import requests
import json

url_items = "http://localhost:8001/todos/5"

response = requests.delete(url_items)

print(response.text)
