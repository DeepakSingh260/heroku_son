
from flask import Flask ,redirect , url_for ,request 
try:
    from selenium import webdriver 
except:
    print("no module name selenoum")
import time

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

secret_token = "wekf3ru93bdk2cmk2"

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.binary_location =GOOGLE_CHROME_PATH
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
options.add_argument("window-size=1400,800")

app = Flask(__name__)


@app.route('/message' , methods=["GET"])
def func():
    if request.args.get("hub.verify_token") != secret_token:
        return app.make_response(("forbidden",403))
    sub = request.args.get('entry')
    if sub:
        return sub
    else:
        return "python project"
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
        if txt:
            lt.append(txt["title"])

    return lt   




if __name__ == "__main__":
    app.debug = True 
    app.run()
