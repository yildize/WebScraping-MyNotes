# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import pandas as pd
import os.path
from os import path


class cryptoSpider(scrapy.Spider):
    name = 'crypto'
    start_urls = ['https://www.worldcoinindex.com']

    list = []

    def parse(self, response):

        rows=  response.xpath("(//tr[position()=1])[2] | //tr[position()>1]")
        for row in rows:    
           self.list.append([row.xpath(".//td[@class='ticker']/h2/text()").get(),row.xpath(".//td[@class='number pricekoers lastprice']/span[2]/text()").get()])

        self.list = np.array(self.list) 
        
        if path.exists("prices.csv"):
            arrayOld = np.genfromtxt('prices.csv', delimiter=',')
            arrayFinal = np.concatenate((arrayOld[:,-1:], self.list[:,-1:]),axis=1)
        else:
            arrayFinal = self.list

        #print(dfNew.head(15))
        np.savetxt("prices.csv", arrayFinal, delimiter=",")
