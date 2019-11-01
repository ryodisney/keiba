#coding:utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.set_headless(True)

driver = webdriver.Chrome(options=options)

url = "https://www.tokyodisneyresort.jp/tds/realtime/attraction/"

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html,"html.parser")

print(soup)
"""
for li in soup.find_all('li',class_ = 'listItem'):
    print(li)
"""

driver.close()
driver.quit()

