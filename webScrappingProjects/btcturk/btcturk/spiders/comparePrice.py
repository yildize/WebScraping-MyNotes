# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import pandas as pd
import os.path
from os import path

class ComparepriceSpider(scrapy.Spider):
    name = 'comparePrice'
    #allowed_domains = ['www.worldcoinindex.com']
    start_urls = ['https://www.worldcoinindex.com']

    df = pd.DataFrame(columns=['crypto', 'price'])
    list = []

    def parse(self, response):

        rows=  response.xpath("(//tr[position()=1])[2] | //tr[position()>1]")
        for row in rows:    
           self.df = self.df.append({'crypto': row.xpath(".//td[@class='ticker']/h2/text()").get(),'price':row.xpath(".//td[@class='number pricekoers lastprice']/span[2]/text()").get() }, ignore_index=True)
           list.append([row.xpath(".//td[@class='ticker']/h2/text()").get(),row.xpath(".//td[@class='number pricekoers lastprice']/span[2]/text()").get()])
        #self.df.drop(self.df.index[[10,21]], inplace=True)

        if path.exists("prices.csv"):
            dfOld = pd.read_csv("prices.csv")
            dfNew = pd.concat([dfOld.iloc[:,1:],self.df.iloc[:,-1]],axis=1)
        else:
            dfNew = self.df

        #print(dfNew.head(15))
        dfNew.to_csv('prices.csv')

