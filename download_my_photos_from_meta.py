import requests
import os
import json
meta_api_key=os.getenv("my_fb_api_key")
url_v1=f"https://graph.facebook.com/v16.0/me/photos/uploaded?access_token={meta_api_key}"
reponse=requests.get(url_v1)
data=json.loads(reponse.text) # be able to work with this data
# get all ID of photos
photo_ids=[]
for photo_id in data["data"]:
    photo_ids.append(photo_id["id"])
photo_links=[] # looks like all my links are save as string and in order to have a photo I need to have bytes value

for photo_id in photo_ids:
    url_v2_by_photo_id=f"https://graph.facebook.com/v16.0/{photo_id}?fields=link%2Cimages&access_token={meta_api_key}"
    reponse_v2=requests.get(url_v2_by_photo_id)
    #print(reponse_v2)
    reponse_v2=json.loads(reponse_v2.text)
    #print(reponse_v2)
    #reponse_v2=requests.get(url_v2_by_photo_id).content
    photo_links.append(reponse_v2["images"][0]["source"])   
# Download all photos
for photo_link in photo_links:
    get_img=requests.get(photo_link).content
    with open(f"_FB_feed.jpg", "wb") as img_file:
        img_file.write(photo_link)