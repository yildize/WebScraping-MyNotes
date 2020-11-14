# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:16:20 2020

@author: Erdo
"""


#%%
import requests
import bs4

#%%
dateList = []
openList = []
highList = []
lowList = []
closeList = []
volumeList = []
capList = []

#%%
#Type a request to get the page. https://coinmarketcap.com/currencies/bitcoin/historical-data/
r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130429&end=20200428')
# r <Response [200]> olarak görünüyorsa, her şey yolunda demektir.

#Now let's make our soup:
soup = bs4.BeautifulSoup(r.text,"lxml")#BeautrifulSoup, ilgili adresteki html'i organize etmeye yarayan bir parserdır.
#soup'un içinde ilgili sayfanın html yapısını organized bir şekilde elde etmiş oluyoruz.

#%%
#Sayfayı incelediğimizde ilk tarihin bir td etiketi içinde verildiğini gördük.
#Mesela diyelim ki sayfanın html yapısında, ilk td etiketini bize döndür.
soup.find('td') 
#<td class="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left">
#<div class="">Apr 27, 2020</div>
#</td>

#Yukarıdaki gibi bir şey dönüyor yani, ilk td etiketinin tamamı döndürülüyor.

#%%
#Spesifik bir etiket kısmını çağırmak istiyorsak, class name'inden yararlanabiliriz:
soup.find('tr',{'class':'cmc-table-row'}) # cmc-table-row class'lı ilk tr etiketini döndürür.
#Bu bize tablonun en üst satırını döndürür (header'ın bir altı)
#İçeriğine bakarsak, date, open, high, low, close, volume, market cap verilerinin sırasıyla yer aldığını görebiliriz.

#%%
#Biz sadece ilgili tr etiketini bulmak istemiyoruz diyelim ki ilgili tr etiketinin içindeki date verisine ulaşmak istiyoruz.
#Bu durumda we will keep using the find function:

soup.find('tr',{'class':'cmc-table-row'}).find('td',{'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'}).find('div').text
#.text diyerek, ilgili html tag'inin içindeki değeri text olarak almış oluyorum, find('div') kısmından önce de .text kullanılabilirdi yine aynı değeri veriyor.

#%%
#Şimdi bir loop yardımı ile tüm tr elementleri gezelim (her bir tr element bir satıra karşılık geliyor.)
#Her tr elementin içinde birçok td yani sütun elementi var.
#Biz şimdilik her tr elementi gezerek içindeki ilk td elementi alacağız, böylece her satırdan tarihleri çekeceğiz.

# soup.find('tr',{'class':'cmc-table-row'}) komutuyla cmc-table-row class'lı olan ilk tr etiketini buluyorduk, ben şimdi hepsini çağıracağım:

tr = soup.find_all('tr',{'class':'cmc-table-row'}) #find_all kullandığımız için, tr bir liste ve her elemanı bir tr etiketi!

#Bu listenin içinde dolaşalım ve her tr etiketinden, ilk td etikeni çekelim böylece date'leri çekmiş oluruz:
for item in tr:
    dateList.append(item.find('td',{'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'}).text) 
#Her elemanı dateList içine attık!
    
#%%
dateList = []
openList = []
highList = []
lowList = []
closeList = []
volumeList = []
capList = []

tr = soup.find_all('tr',{'class':'cmc-table-row'}) 

for item in tr:
    dateList.append(item.find_all('td')[0].text) 
    openList.append(item.find_all('td')[1].text) 
    highList.append(item.find_all('td')[2].text) 
    lowList.append(item.find_all('td')[3].text) 
    closeList.append(item.find_all('td')[4].text) 
    volumeList.append(item.find_all('td')[5].text) 
    capList.append(item.find_all('td')[6].text)


dateList = dateList[:2314]
dateList = dateList[::-1] 

openList = openList[:2314]
openList = openList[::-1]
openList = [float(i.replace(',','')) for i in openList] 

highList = highList[:2314]
highList = highList[::-1]
highList = [float(i.replace(',','')) for i in highList] 

lowList = lowList[:2314]
lowList = lowList[::-1]
lowList = [float(i.replace(',','')) for i in lowList] 

closeList = closeList[:2314]
closeList = closeList[::-1]
closeList = [float(i.replace(',','')) for i in closeList] 

volumeList = volumeList[:2314]
volumeList = volumeList[::-1]
volumeList = [float(i.replace(',','')) for i in volumeList] 

capList = capList[:2314]
capList = capList[::-1]
capList = [float(i.replace(',','')) for i in capList] 

#%%
import numpy as np
dateList = np.array(dateList)
openList = np.array(openList)
highList = np.array(highList)
lowList = np.array(lowList)
closeList = np.array(closeList)
volumeList = np.array(volumeList)
capList = np.array(capList)

#%%
Y = (closeList-openList)/openList*100
#%%


