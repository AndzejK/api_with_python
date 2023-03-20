#openweathermap.org 
import requests
import os

api_key_openweathermap=os.getenv("api_persnal_key_openweathermap")
city_name="Vilnius"
request_by_city=f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key_openweathermap}&units=metric"

api=requests.get(request_by_city)
data=api.json() #JSON in dictionary
org_list_from_openweathermap=data["list"]

#storing conditions info in the list, e.x. 'clear sky', 'light rain', 'light rain'
conditions=[]
for all in org_list_from_openweathermap:
    for desc in ((all["weather"])):
        conditions.append(desc["description"])

print(conditions)