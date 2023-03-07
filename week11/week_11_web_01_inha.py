# from selenium import webdriver
#
# wd = webdriver.Chrome('../WebDriver/chromedriver')
# wd.get('http://www.inha.ac.kr')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return d

wd = set_chrome_driver()
wd.get('http://www.inha.ac.kr')