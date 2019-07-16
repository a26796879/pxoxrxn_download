# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:47:02 2019

@author: user
"""
import requests, json
from bs4 import BeautifulSoup
import re

url = 'https://www.helloavgirls.com/av/592'

res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
sc = soup.find('script',{'type': 'text/JavaScript'}).text
#s = sc.find('file')

print (sc[168:214])

'''
下載檔案
import urllib.request
urllib.request.urlretrieve(sc[168:214], sc[200:214]+'.mp4')
'''
#part = re.compile(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/]+", re.MULTILINE)

#part = re.compile(r"^playerInstance.setup")
#print(re.match(part,sc))
print(sc[sc.find('https://v4'):sc.find('skin')-4])

