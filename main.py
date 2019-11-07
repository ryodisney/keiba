#cording:utf-8

import requests
from bs4 import BeautifulSoup
from scrayping_now import Pass_Url_Now,Scraping_Now,Get_Link_List_Now,Get_Race_Info_Now
from scrayping_past import Pass_Url_Past,Scraping_Past,Get_Link_List_Past,Get_Race_Info_Past
from weight import Weight


def main():
    #今回予想したいレースのURL
    url_now = "https://race.netkeiba.com/?pid=race_old&id=c201903030411"

    #学習するレースのURL
    url_past = "https://db.netkeiba.com/race/201905040911/"

    #ave_list_now = Pass_Url_Now(url_now)
    ave_list_past = Pass_Url_Past(url_past)
    
    weight_list = Weight(ave_list_past)

if __name__ == "__main__":
    main()