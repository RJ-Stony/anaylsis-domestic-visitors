# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:57:02 2025

@author: Roh Jun Seok
"""

from selenium import webdriver
driver = webdriver.Chrome()

url = 'https://www.naver.com/'
driver.get(url)

html = driver.page_source

html = '''
<html>
    <head>
    </head>
    <body>
        <h1> 우리동네시장</h1>
            <div class = 'sale'>
                <p id='fruits1' class='fruits'>
                    <span class = 'name'> 바나나 </span>
                    <span class = 'price'> 3000원 </span>
                    <span class = 'inventory'> 500개 </span>
                    <span class = 'store'> 가나다상회 </span>
                    <a href = 'http://bit.ly/forPlaywithData' > 홈페이지 </a>
                </p>
            </div>
            <div class = 'prepare'>
                <p id='fruits2' class='fruits'>
                    <span class ='name'> 파인애플 </span>
                </p>
            </div>
    </body>
</html>
'''

from bs4 import BeautifulSoup as bs

soup = bs(html, 'html.parser')

tags_span = soup.select('span.name')
tags_p = soup.select('#fruits2 > span.name')
tags_p

tags_banana = soup.select('div.sale span.name')

content = tags_banana[0].text

tags_a = soup.select('a')
a = tags_a[0]
content = a.text

link = a['href']
link


driver = webdriver.Chrome()
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = bs(html, 'html.parser')
tags_tr = soup.select('tr')[0]

songs = soup.select('tr')[1:]
len(songs)

song = songs[0]
song

song_info = []

for i in range(len(songs)):
    song = songs[i]
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    artist = song.select('div.ellipsis.rank02 > a')[0].text
    song_info.append((title, artist))
    
song_info
