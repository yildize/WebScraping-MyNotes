# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from shutil import which
from selenium import webdriver


class ComparepriceSpiderSelenium(scrapy.Spider):
    name = 'comparePriceSelenium'
    allowed_domains = ['https://pro.btcturk.com']
    start_urls = ['https://pro.btcturk.com']


    def __init__(self):

        chrome_path = which('chromedriver')
        driver = webdriver.Chrome(executable_path = chrome_path)

        driver.set_window_size(1920, 1080)
        driver.get("https://pro.btcturk.com")

        self.html = driver.page_source
        



    def parse(self, response):

        #resp = Selector(text=self.html)
        print(self.html)
            


