import requests
import os
import json

meta_api_key = os.getenv("my_fb_api_key")
batch_request = []
photo_links = []

url_v1 = f"https://graph.facebook.com/v16.0/me/photos/uploaded?access_token={meta_api_key}"
response_v1 = requests.get(url_v1).json()
photo_ids = [photo['id'] for photo in response_v1['data']]

for photo_id in photo_ids:
    batch_request.append({
        "method": "GET",
        "relative_url": f"{photo_id}?fields=link%2Cimages&type=large"
    })
batch_url = f"https://graph.facebook.com/v16.0/?access_token={meta_api_key}"
batch_response = requests.post(batch_url, data={"batch": json.dumps(batch_request)})
batch_data = json.loads(batch_response.text)

for data in batch_data:
    response_v2 = json.loads(data["body"])
    photo_links.append(response_v2["link"])
    image_url = response_v2["images"][0]["source"]
    image_data = requests.get(image_url).content
    photo_id = response_v2['id']
    with open(f"{photo_id}.jpg", "wb") as img_file:
        img_file.write(image_data)





"""
import requests
import os
import json
meta_api_key=os.getenv("my_fb_api_key")
api_url_for_a_photo=f"https://graph.facebook.com/v16.0/5332709826750995?fields=link%2Cimages&access_token={meta_api_key}"
url=f"https://graph.facebook.com/v16.0/me?fields=id%2Cname%2Cposts&access_token={meta_api_key}"
response=requests.get(api_url_for_a_photo)
#print(response.content) # binary result

#Downlaod images/photos from FB via API using python

data=response.text # plain txt result - type STRING
data=json.loads(data) # coverted to DICTIONARY - json format and now we can parse this data with python
img_url_max_size=(data["images"][0]["source"])
get_img=requests.get(img_url_max_size).content # get bits rather than txt :)

with open("photo_downloaed_from_FB_ME.jpg", "wb") as img_file:
    img_file.write(get_img)
"""