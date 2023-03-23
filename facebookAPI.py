import requests
import os
import json
meta_api_key=os.getenv("my_fb_api_key")
api_url_for_a_photo=f"https://graph.facebook.com/v16.0/5332709826750995?fields=link%2Cimages&access_token={meta_api_key}"
url=f"https://graph.facebook.com/v16.0/me?fields=id%2Cname%2Cposts&access_token={meta_api_key}"
response=requests.get(api_url_for_a_photo)
#print(response.content) # binary result

"""Downlaod images/photos from FB via API using python"""

data=response.text # plain txt result - type STRING
data=json.loads(data) # coverted to DICTIONARY - json format and now we can parse this data with python
img_url_max_size=(data["images"][0]["source"])
get_img=requests.get(img_url_max_size).content # get bits rather than txt :)

with open("photo_downloaed_from_FB_ME.jpg", "wb") as img_file:
    img_file.write(get_img)
