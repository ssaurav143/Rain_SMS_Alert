# API Authentication

import requests
from twilio.rest import Client
import os

api_key = os.getenv("OPENWEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

weather_parameters = {
    "lat": 60.128162,
    "lon": 18.643501,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
print(response)
response.raise_for_status()

data = response.json()
print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain, get an umbrella with you!",
        from_=from_number,
        to=to_number,
    )
    print(message.sid)