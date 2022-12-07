import requests

request_data = {"x": 3, "y": 4, "task": "prodd"}

a = requests.post("http://127.0.0.1:5000/api/task", json=request_data)

print(a.json())
