# Flask is a class
from flask import Flask,jsonify,send_from_directory,send_file

from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_cur, out_cur):
    url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
    # if you enter "EUR","AUD" the result would be https://www.x-rates.com/calculator/?from=EUR&to=AUD&amount=1
    get_content=requests.get(url).text # getting SOURCE CODE 
    # At this stage we start using bs4 lib
    soup = BeautifulSoup(get_content,"html.parser")
    # finding class for our rate in HTML format
    soup.find("span", class_="ccOutputRslt")
    # display just text as browser for an user!
    rate=soup.find("span", class_="ccOutputRslt").get_text() # result is 1.598466 AUD and we want to have just numbers
    rate=float(rate[:-4])
    return rate
# Here the app variable will hold/keep a string/data of our script named "my_own_api.py", 
# it's standard way of doing it
app = Flask(__name__)

# defining route for my API, home "/" - default page
@app.route('/')
def home():
    home_content = "<center><h1>Currency Rate API</h1></center> Here you can find all needed info regarding this API!"
    api_usage="<p>To access currency rate use this link and specufy desired currency nominals  - <i>/api/v1/<b>cur_in</b>-<b>cur_out</b></i></p>"
    example="<p>API URL: domain/api/v1/usd-eur -> http://127.0.0.1:5000/api/v1/usd-eur</p>"
    return f"{home_content} {api_usage} {example}"

@app.route('/api/v1/<cur_in>-<cur_out>')
def api(cur_in,cur_out):
    rate=get_currency_rate(cur_in,cur_out)
    result_dictionary={"input_currency":cur_in,"output_currency":cur_out,"rate":rate}
    return jsonify(result_dictionary)


#run this web app/API  
app.run()