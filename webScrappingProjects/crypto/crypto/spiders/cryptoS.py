# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import pandas as pd
import os.path
from os import path


class CryptosSpider(scrapy.Spider):
    name = 'cryptoS'
    allowed_domains = ['worldcoinindex.com']
    start_urls = ['https://www.worldcoinindex.com']

    list = []

    def parse(self, response):

        rows=  response.xpath("(//tr[position()=1])[2] | //tr[position()>1]")
        for row in rows:    
           self.list.append([row.xpath(".//td[@class='ticker']/h2/text()").get(),row.xpath(".//td[@class='number pricekoers lastprice']/span[2]/text()").get()])

        self.list = np.array(self.list) 
        
        if path.exists("prices.csv"):
            dfOld = pd.read_csv("prices.csv", header=None)
            arrayOld = dfOld.values
            print("old")
            print(arrayOld)
            print("self")
            print(self.list)
            arrayFinal = np.concatenate((arrayOld, self.list[:,-1:]), axis=1)
        else:
            arrayFinal = self.list

       
        df = pd.DataFrame(arrayFinal)
        df.to_csv('prices.csv',index=False, header=False)
