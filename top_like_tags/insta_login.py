
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from django.conf import settings
import os

path_of_file = os.path.join(settings.BASE_DIR, 'static')

chromeOptions = Options()
chromeOptions.add_argument("user-data-dir={}".format(path_of_file+'/topliketags-profile'))
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-dev-sha-usage")
chromeOptions.add_argument("--no-sandbox")


drivers = []
def insta_login():    
    if drivers != []:
        return drivers
    else:   
        x = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        x.set_window_size(1366, 768)  
        drivers.append(x)
        x.get("https://www.instagram.com/")
        return drivers

