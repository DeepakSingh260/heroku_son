
from flask import Flask ,redirect , url_for ,request 
try:
    from selenium import webdriver 
except:
    print("no module name selenoum")
import time
import locale

import asyncio
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from bs4 import BeautifulSoup
import requests

options = Options()
# options.binary_location  = r"C:\Program Files\Mozilla Firefox\firefox.exe"

secret_token = 'EAALE1CNsKmUBAFTVO2pbd2m8m9GKakJTW6UZACknrDWoZCghIF4Ew6fJdsDCEX96ReQz7AIIof1Shh2yHbiO9UIFVYzZCZC61HqQ44zaaAcjNxB43U4CFCyZAYG06lZCX27bdpfV7YrNT89UwbQLUaeMMcOVYljvaEZAYqUqkUV6jhOZCnnauLUZBvnu4WblQo4jmALDyT58SKAZDZD'

GOOGLE_CHROME_PATH = '/bin/google-chrome-stable'
CHROMEDRIVER_PATH = '/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.binary_location =GOOGLE_CHROME_PATH
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
options.add_argument("window-size=1400,800")

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
app = Flask(__name__)

@app.route('/message' , methods=["GET"])
def func():
    print("hub token",request.args.get("hub.verify_token") , "mode" , request.args.get("hub.mode") )
    sent_token = str(request.args.get("hub.verify_token")).split(" ")[0]
    print(sent_token , "/n" , secret_token)
    if sent_token != secret_token :
        return app.make_response(("forbidden token",403))
    
    if request.args.get("hub.mode") != "subscribe" :
        return app.make_response(("forbidden mode",403))
    sub = request.args.get('entry')

    res = request.args.get("hub.challenge")
    return app.make_response((res , 200))
    # if sub:
    #     return app.make_response((sub , 200))
    # else:
    #     return app.make_response(("python project",200))
@app.route('/' )
def init():
    
    return "Welcome to What-is-app bot"

@app.route('/Question/<Query>')
def miningbs4(Query):
    
    py_url = "https://shopping.google.com/search?q="+str(Query)
    py_con = requests.get(py_url)
    
    py_soup = BeautifulSoup (py_con.text, 'html.parser')
    lt=[]
    for cell in py_soup.find_all('td' , attrs={'class':'KEJLN'}):
      
        txt = cell.find('h2' , attrs={'class': 'MPhl6c'})
        price = cell.find('span', attrs={'class': 'aZK3gc Lhpu7d'})
        link = cell.find('a', attrs={'class':'loT5Qd kneS6c'})
        # print(price.text)
        if txt:
            lt.append((locale.atof(price.text[1:]),txt["title"],link['href']))

    return sorted(lt)




if __name__ == "__main__":
    app.debug = True 
    app.run()
