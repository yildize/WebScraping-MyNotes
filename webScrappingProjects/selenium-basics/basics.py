#selenium içerisinden webdriver paketini import ediyoruz.
from selenium import webdriver
#indirilen chrome driver'ının path'ini elde etmek için kullanacağız.
from shutil import which

#chrome driver'ının sadece adını vererek path'i elde ettik.
chrome_path = which("chromedriver")

#indirilen chromedriver'ı driver olarak atadık.
driver = webdriver.Chrome(executable_path = chrome_path)

#driver ile istediğimiz url'i açtık.
driver.get("https://duckduckgo.com")

#input elemanını id'sini kullanarak bulalım:
search_input = driver.find_element_by_id("search_form_input_homepage") # alternative : search_input = driver.find_element_by_xpath("(//input[@contains(@class,'js-search-input')])[1]")
search_input.send_keys("My User Agent")

#şimdi de search button'ını seçip elemana tıklayalım:
search_btn = driver.find_element_by_id("search_button_homepage")
search_btn.click()

