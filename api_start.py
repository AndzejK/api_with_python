import requests # for HTTP
import os
my_API_key=os.getenv('personal_api_key') 
API_from_tutorial="890603a55bfa47048e4490069ebee18c" 

api_link=f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-3-18&to=2023-3-20&sortBy=popularity&language=en&apiKey={my_API_key}"

http_req=requests.get(api_link)
stored_content_in_dictionary_form=http_req.json() #JSON in dictionary
articles=stored_content_in_dictionary_form["articles"]
#print(articles[1]["title"])
recent_articles=''
for article in articles:
    recent_articles+=(f"\nTitle: {article['title']},\n\tDescription:\n\t{article['description']}")
    print(recent_articles)
    with open("artciles.csv", 'w') as csv_file:
        csv_file.write(recent_articles)