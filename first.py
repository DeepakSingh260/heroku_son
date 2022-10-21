
from flask import Flask ,redirect , url_for ,request 
try:
    from selenium import webdriver 
except:
    print("no module name selenoum")


import asyncio
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

options = Options()
# options.binary_location  = r"C:\Program Files\Mozilla Firefox\firefox.exe"

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.binary_location =GOOGLE_CHROME_PATH
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
options.add_argument("window-size=1400,800")

app = Flask(__name__)


@app.route('/')
def func():
    return "python project"
@app.route('/<Query>')
def mining(Query):
    
   
    
    

    loop= asyncio.get_event_loop()
    obj = loop.create_task(query(str))
    return loop.run_until_complete(obj)


async def query(string):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://www.meesho.com/search?q="+str(string))
    driver.implicitly_wait(10) 
    el = driver.find_elements(By.CLASS_NAME,"sc-dkPtyc")
    link = []
    for i in el:
        try:
            # print("var",i.find_element(By.CLASS_NAME ,"a-link-normal").get_attribute("href"))
            if i.find_element(By.CLASS_NAME ,"BBZyK").text == '':
                pass
            else:
                link.append([i.find_element(By.TAG_NAME ,"a").get_attribute("href"),i.find_element(By.CLASS_NAME ,"NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5").text,i.find_element(By.CLASS_NAME ,"BBZyK").text])
        except:
            pass  

    return link

if __name__ == "__main__":
    app.debug = True 
    app.run()
