#coding:utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://disneyreal.asumirai.info/realtime/disneyland-wait-today-wa.html"

html = requests.get(url)
#ページがないときにエラーを表示
#html.raise_for_status()
soup = BeautifulSoup(html.content,'lxml')

time_list = []

#リンク先取得
for ul in soup.find_all('ul',class_ = 'wait-time'):
    for li in ul.find_all('li',class_ = 'time'):
        for wait_time in li.find_all('p'):
            wait_time.find("span").extract()
            time_list.append(wait_time.text)
        
print(time_list)


