from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument("--disable-dev-sha-usage")
chromeOptions.add_argument("--no-sandbox")

drivers = []
def insta_login():    
    if drivers != []:
        return drivers
    else:   
        x = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        x.maximize_window()
        drivers.append(x)
        x.get("https://instagram.com")
        sleep(2)
        x.find_element_by_name("username").send_keys("topliketagsbot")
        x.find_element_by_name("password").send_keys("tomtom852")
        sleep(2)
        try:
            x.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        except NoSuchElementException:
            x.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        sleep(2)
        j = 0
        try:
            if j == 0:
                captcha_present = x.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div[2]/div/div/div[2]/div/button')
                print("Captcha Locked")
                x.close()
        except NoSuchElementException:
            print("Logged In")
        return drivers

