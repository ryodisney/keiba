#cording:utf-8

import requests
from bs4 import BeautifulSoup
from scrayping_now import Scraping_now,Get_Link_List,Get_Race_Info
from scrayping_past import Scraping_Past
from evaluate import Evaluate
from weight import Weight


def main():
    url = "https://race.netkeiba.com/?pid=race_old&id=c201903030411"

    html = requests.get(url)
    soup = BeautifulSoup(html.content,'lxml')

    race_name,distance = Get_Race_Info(soup)
    print(race_name)
    link_list,horse_list,jockey_list = Get_Link_List(soup)

    #print(link_list)

    for link_url,horse_name,jockey_name in zip(link_list,horse_list,jockey_list): 
        df = Scraping(link_url)
        print(horse_name)
        print(jockey_name)
        print(df)
        
        ave_list = Evaluate(df,distance)
        #print(ave_list)

        weight_list = Weight(ave_list)

        

if __name__ == "__main__":
    main()