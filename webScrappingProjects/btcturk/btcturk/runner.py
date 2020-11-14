import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os.path
from os import path
import time
import numpy as np
import pandas as pd
from spiders.comparePrice import ComparepriceSpider

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from twisted.internet import task

from time import sleep
import subprocess

#Read drom website for 5 mins.
timeout = 1
for i in range(5):
    command = 'scrapy crawl comparePrice'
    subprocess.run(command, shell=True)
    sleep(timeout)
    print(i)

#After 5 mins get the data 
#df = pd.read_csv("prices.csv", sep='\t', thousands=',')   
df = pd.read_csv("prices.csv",  thousands=',')
#df.drop(df.index[[10,21]], inplace=True)

#Cast string columns to float
#df.iloc[:,-5:] = df.iloc[:,-5:].str.replace(',', '').astype(float)

#Calculate the trends for last 5 mins
diff = df.diff(axis=1)
diff.to_csv('diff.csv')




#process = CrawlerProcess(settings=get_project_settings())
#process.crawl(ComparepriceSpider)
#process.start()

