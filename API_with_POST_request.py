# POST -> the server has to di something with data rather than just GETting some info
# https://languagetool.org/http-api/#/default

import requests
import json
url="https://api.languagetool.org/v2/check"

data={
    "text":"Hi hope you are well! If you are in Barcelona you should go to Salvador Dali museum in Figueres",
    "language":"auto"
}
reponse=requests.post(url,data=data)
"""
print(f"Just getting/posting URL': {type(reponse)} - {reponse}")
print(f"Once we set to 'content': {type(reponse.content)}") #  <class 'bytes'>
print(f"Once we set to 'text': {type(reponse.text)}") # <class 'str'> 
result=json.loads(reponse.text) # from STRING we converted to DICTIONARY 
print(f"Once we loaded 'response' to JSON lib: {type(result)}") # <class 'dict'>
"""
result=json.loads(reponse.text)
print(result)
