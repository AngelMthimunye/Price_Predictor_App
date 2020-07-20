import requests

url = "http://localhost:5000/predict_api"
r = requests.post(url, json={"carat":0.2, "cut": 1, "color":2, "clarity":1, "length": 0.2. "width": 0.3, "depth": 0.4})

print(r.json())


