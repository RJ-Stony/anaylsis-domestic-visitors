from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'http://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1

# songs = soup.select('table.byChart > tbody > tr')
titles = soup.select('table > tbody > tr > th > p.title')
artists = soup.select('table > tbody > tr > td > p.artist')
len(artists)

for i in range(len(titles)):
    title = titles[i].text.strip()
    artist = artists[i].text.strip()
    
    song_data.append(['Bugs', rank, title, artist])
    rank += 1

columns = ['서비스명', '순위', '타이틀', '아티스트']
bugs = pd.DataFrame(song_data, columns=columns)
bugs.head()

bugs.to_excel('./files/bugs.xlsx', index=False)
