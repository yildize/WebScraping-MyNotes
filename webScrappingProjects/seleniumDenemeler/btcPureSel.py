from shutil import which
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=1.2.3.4:8080')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://whatismyipaddress.com")
