from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1

songs = soup.select('table > tbody > tr')
len(songs)

for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    artist = song.select('div.rank02 > a')[0].text
    
    song_data.append(['Melon', rank, title, artist])
    rank += 1
    
columns = ['서비스명', '순위', '타이틀', '아티스트']
melon = pd.DataFrame(song_data, columns=columns)
melon.head()

'''
    서비스명  순위                             타이틀       아티스트
0  Melon   1                     REBEL HEART  IVE (아이브)
1  Melon   2  HOME SWEET HOME (feat. 태양, 대성)   G-DRAGON
2  Melon   3                          나는 반딧불        황가람
3  Melon   4                        Whiplash      aespa
4  Melon   5                            APT.  로제 (ROSÉ)
'''

melon.to_excel('./files/melon.xlsx', index=False)
