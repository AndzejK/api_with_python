#openweathermap.org 
"""Search weather forecast for 5 days with data every 3 hours by city name """

import requests
import os

api_key_openweathermap=os.getenv("api_persnal_key_openweathermap")
city_name="Vilnius"
request_by_city=f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key_openweathermap}&units=metric"

api=requests.get(request_by_city)
data=api.json() #JSON in dictionary
org_list_from_openweathermap=data["list"]
msc=data["city"] #getting info about city

#storing conditions info in the list, e.x. 'clear sky', 'light rain', 'light rain'
conditions=[]
for all in org_list_from_openweathermap:
    conditions.append(all["weather"][0]["description"]) # coz the key "weather" stores another list 

#storing date and time         
time_dt=[]
for time in org_list_from_openweathermap:
    time_dt.append(time["dt_txt"])

#Storing temprature 
tempratures=[]
for temp in org_list_from_openweathermap:
    tempratures.append(temp["main"]["temp"])

#Fetching city name from API
city=msc["name"]

# Combing all data and write/add to  the file
def combines_data(time,temp,cond):
    city=city_name
    line=''
    i=0
    while i<len(time):
        line+=(f"{city}, {time[i]}, {temp[i]}, {cond[i]}\n")
        i+=1
    # Mistake was having the open() method inside the loop and caused some unnecessary repetition   
    with open("data.txt","a") as file: # append to the file 
        file.write(line)
combines_data(time_dt,tempratures,conditions)