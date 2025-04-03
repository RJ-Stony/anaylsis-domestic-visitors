# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:57:14 2025

@author: Roh Jun Seok
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1

titles = soup.select('table > tbody > tr > td > a.title.ellipsis')
artists = soup.select('table > tbody > tr > td > a.artist.ellipsis')

for i in range(len(titles)):
    title = titles[i].text.strip()
    artist = artists[i].text.strip()
    
    song_data.append(['Genie', rank, title, artist])
    rank += 1

url2 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250218&hh=10&rtm=Y&pg=2'
driver.get(url2)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('table > tbody > tr > td > a.title.ellipsis')
artists = soup.select('table > tbody > tr > td > a.artist.ellipsis')

for i in range(len(titles)):
    title = titles[i].text.strip()
    artist = artists[i].text.strip()
    
    song_data.append(['Genie', rank, title, artist])
    rank += 1

columns = ['서비스명', '순위', '타이틀', '아티스트']
genie = pd.DataFrame(song_data, columns=columns)
genie.tail()

genie.to_excel('./files/genie.xlsx', index=False)
