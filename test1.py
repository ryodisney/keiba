#coding:utf-8

import requests
from bs4 import BeautifulSoup

url = "https://www.yoshinoya.com/menu/takeout/"

headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url,headers=headers)
#ページがないときにエラーを表示
#html.raise_for_status()
soup = BeautifulSoup(html.content,'lxml')

member = []


for p in soup.find_all('li',class_ = "menu-content"):
    for gyuu in p.find_all('h3'):
        member_name = gyuu.text.strip()
        member.append(member_name)
    
print(member)
"""
i = 0
for ngzk in member:
    i += 1
    print(str(i)+ '.' + ngzk)
"""
