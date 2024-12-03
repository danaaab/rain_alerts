import requests
from twilio.rest import Client

api_key = "873221da66e817dce14bc8f61c8e0c70"
account_sid = "ACa144dfc78fa264c646e177332a0e288d"
auth_token = "eb4b18bdaf2e1aeb40e494e9b79f414a"
LAT = 52.229675
LON = 21.012230
parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 3
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring Umbrella!",
        from_="+16812305183",
        to="+48518532282",
    )
    print(message.status)