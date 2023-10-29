import requests
import random

endpoint_url = "https://agrimo.up.railway.app/update_graphsmin"

sensors = ["Sunradiation", "Humidity", "Odor", "Raindrop", "Temperature", "Light", "Moisture", "Pressure"]

data = []
for sensor in sensors:
    random_data = {
        "username": "alisherr",
        "sensor": sensor,
        "targetmin": 30,
        "targetminper": random.randint(0, 100)
    }
    data.append(random_data)

response = requests.post(endpoint_url, json=data)

print("Response from server:", response.status_code)
print(response.json())
