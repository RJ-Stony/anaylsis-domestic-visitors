from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

browser = webdriver.Chrome()
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

channel_list = soup.select('form > table > tbody > tr')
len(channel_list)

channel = channel_list[0]
category = channel.select('p.category')[0].text.strip()
title = channel.select('h1 > a')[0].text.strip()
subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text

def clean_text(text):
    return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', text)

results = []

for page in range(1, 10+1):
    url = f'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}'
    browser.get(url)
    time.sleep(2)
    
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    channel_list = soup.select('form > table > tbody > tr')
    
    for channel in channel_list:
        title = clean_text(channel.select('h1 > a')[0].text.strip())
        category = clean_text(channel.select('p.category')[0].text.strip())
        subscriber = clean_text(channel.select('.subscriber_cnt')[0].text)
        view = clean_text(channel.select('.view_cnt')[0].text)
        video = clean_text(channel.select('.video_cnt')[0].text)
        
        data = [title, category, subscriber, view, video]
        results.append(data)

df = pd.DataFrame(results)
df.columns = ['Title', 'Category', 'Subscriber', 'View', 'Video']

df.to_excel('./files/youtube_rank.xlsx', index=False)
