# -*- coding: utf-8 -*-
import scrapy

#Selector'ı string olan selenium response'unu selector'a çevirmek için kullanacağız.
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    
    #start_request class'ı override edilmediği için default olarak aşağıdaki adrese request gönderilir.
    #response da default olarak parse methodunda yakalanır.
    start_urls = [
        'https://www.livecoin.net/en'
    ]
    
    #selenium işlemleri consturctor içerisinde yapılacak:
    def __init__(self):
        #önce headless driver için ayar yapalım:
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        #driver'ın path'ini ve options'ı vererek driver objemizi elde edelim:
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(executable_path = chrome_path, options=chrome_options)

        #sayfadaki tüm elemanları tek seferde görebilmek için resolution'ı artıralım.
        driver.set_window_size(1920, 1080)
        #ana url'e giriş yapalım:
        driver.get("https://www.livecoin.net/en")

        #sekmelerden USD sekmesini seçelim ve tıklayalım, ilgili class'a sahip olan 3. eleman USD tab'i oluyor.
        usd_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        usd_tab[2].click()

        #sonuçta karşımıza çıkan sayfanın html markup'ını string olarak self.html adında kaydedelim.
        self.html = driver.page_source

        #işi biten driver'ı kapatalım.
        driver.close()



    def parse(self, response):
        #catch edilen response bize lazım değil, bize asıl lazım olan response
        #selenium içinde elde edilen self.html içine kaydedilen html markup'ı
        #ancak bu markup şuan string formatında bunu selector object'e çeviriyoruz:
        resp = Selector(text = self.html)

        #daha sonra bu sayfa üzerinde önceden olduğu gibi tüm satır elemanlarını seçiyoruz
        #ve for loop ile tek tek satırları dolanıp gerekli elemanları yield ediyoruz:
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                "currency pair": currency.xpath(".//div[1]/div/text()").get(),
                "volume(24h)": currency.xpath(".//div[2]/span/text()").get()
            }
