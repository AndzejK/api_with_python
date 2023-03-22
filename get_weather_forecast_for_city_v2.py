#More organised script based on the tutorial

import requests
import os
personal_api_key=os.getenv("api_persnal_key_openweathermap")

#1st we're going to have one function just, called get_weather where we have default values and city value needs to be passed
def get_weather(city,units="metric", api_key=personal_api_key):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    #We http request to fetch data
    r=requests.get(url) # at this stage we just get the "reponse code"
    #Here we receive whole content/data 
    content=r.json() 
    #Before looping we're opening up a file and append the content to it
    with open("data.txt","a") as file:
    # We iterate through the list
        for dictionary in content["list"]:
            file.write(f"{city},{dictionary['dt_txt']},{dictionary['main']['temp']},{dictionary['weather'][0]['description']}\n")
    
get_weather("Sydney")