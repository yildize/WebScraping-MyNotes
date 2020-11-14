import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os.path
from os import path
import time
import numpy as np
import pandas as pd
#from spiders.crypto import cryptoSpider

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from twisted.internet import task

from time import sleep
import subprocess

#Read drom website for 5 mins.
timeout = 1
for i in range(5):
    command = 'scrapy crawl cryptoS'
    subprocess.run(command, shell=True)
    sleep(timeout)
    print(i)

#After 5 mins get the data 
df = pd.read_csv("prices.csv",  thousands=',', header=None) #csv'nin headerı yok olarak kabul edecek, yani ilk satırı data olacak alacak.
#df.drop(df.index[[10,21]], inplace=True)


#Calculate the trends for last 5 mins
diffPercent = df.iloc[:,1:].pct_change(axis=1)
diffPercent = pd.concat([df.iloc[:,0],diffPercent.iloc[:,1:]],ignore_index=True,axis=1)
diffPercent.to_csv('diffPercent.csv', index=False, header=False) #otomatik yazdığı header'ı ve index'i eklemeyecek.

#Detect important subjects

