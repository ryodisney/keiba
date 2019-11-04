#coding:utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from evaluate import Evaluate


pd.set_option('display.unicode.east_asian_width', True)


def Get_Race_Info(soup):
    
    for dl in soup.find_all('dl',class_='racedata fc'):
        for dd in dl.find_all('dd'):
            race_name = dd.find('h1').get_text()
            distance_moji = dd.find('p').get_text()
            distance = re.sub(r'[芝ダm左右内外()]','',distance_moji)

    return race_name,distance


def Get_Link_List(soup):

    link = []
    horse_list = []

    #リンク先取得
    for td in soup.find_all('td',class_ = 'txt_l horsename'):
        link.append(td.a.get('href'))
        horse_list.append(td.a.get_text())

    return link,horse_list


def Scraping(link_url):

    #要素を取り出す
    ele_html = requests.get(link_url)
    ele_soup = BeautifulSoup(ele_html.content,'lxml')


    table = ele_soup.find('table',class_ = 'db_h_race_results nk_tb_common')
    tr = table.find_all('tr')


    for i,row in enumerate(tr):
        Row = []
        colum = []
        for cell in row.find_all(['td','th']):
            Row.append(cell.get_text())
        
        #順番は日付、距離、着順、タイム、通過、上り、騎手
        if i == 0:
            final = [Row[0],Row[14],Row[11],Row[17],Row[20],Row[22],Row[12].strip()]
            colum = final
            df = pd.DataFrame(columns=colum)

        else:

            date = Row[0]
            this_distance = re.sub(r'[芝ダ]','',Row[14])
            arrival_order = Row[11]
            total_time = Row[17]
            pass_order = Row[20]
            last_spart = Row[22]
            jockey = Row[12].strip()

            temp = [date,this_distance,arrival_order,total_time,pass_order,last_spart,jockey]
            
            for i in range(len(temp)):
                if temp[i] == '\xa0' or temp[i] == '＆nbsp;':
                    temp[i] = 'no_data'

            if total_time != '\xa0':
                split_time = total_time.split(':')
                minutes = int(split_time[0])
                seconds = float(split_time[1])
                temp[3] = minutes * 60 + seconds
            
            if pass_order != '\xa0':
                #通過
                split_by = pass_order.split('-')
                temp[4] = split_by[0]
            
            if arrival_order != '\xa0':
                flag = is_int(arrival_order)
                if flag:
                    temp[2] = int(arrival_order)
                
                else:
                    temp[2] = 'no_data'

            final = temp
            temp_data_list = pd.Series(final,index=df.columns)
            df = df.append(temp_data_list,ignore_index=True)
        #print(final)

    return df

#文字列がintに変換できるかの判断   
def is_int(s):
  try:
    int(s)
  except:
    return False
  return True

def main():
    url = "https://race.netkeiba.com/?pid=race_old&id=n201908050411"

    html = requests.get(url)
    soup = BeautifulSoup(html.content,'lxml')

    race_name,distance = Get_Race_Info(soup)
    print(race_name)
    link_list,horse_list = Get_Link_List(soup)

    #print(link_list)

    for link_url,horse_name in zip(link_list,horse_list): 
        df = Scraping(link_url)
        print(horse_name)
        #print(df)
        
        ave_list = Evaluate(df,distance)
        print(ave_list)

        

if __name__ == "__main__":
    main()