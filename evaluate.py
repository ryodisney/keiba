import pandas as pd
import numpy as np


#################
def Evaluate(df,distance):
    #print('こっから今江ニキ')
    ###############Pandasの更新毎に初期化して使う変数とリストの説明
    p_list =[]
    ave_distinct = 0            ##平均距離
    ave_order = 0           ##平均着順(4以上は個人的に悪印象)
    ave_time = 0            ##平均時間(m/s)
    ave_agari = 0           ##平均上がり

    distinct_list = []      ##距離のリスト
    distinct_time_list = [] ##距離/時間をするために時間と同期させた距離のリスト
    order_list =[]          ##順位のリスト
    time_list = []          ##タイムのリスト
    ashi_list = []          ##脚質のためのリスト
    agari_list = []         ##上がりのリスト
    kisyu_list = []         ##騎手リスト
    ashi = "ashi"           ##脚質種類(nige, sashi, oikomi)

    count_1 ,count_2 , count_3 = 0, 0 , 0 ##カウント変数
    kisyu_dict = {}
    kisyu = ""
    i = 0
    

     
    ##store_list   受け渡す用のリスト
    store_list =[]
    ################################################
    ###ここからメインのプログラム

    p_list = df.values.tolist()
    for i in range(len(p_list)):                        ####ループでパンダからリストへ処理
        if p_list[i][1] is not "no_data":
            distinct_list.append(int(p_list[i][1]))
        if p_list[i][2] is not "no_data" and p_list[i][6] is not "no_data":
            order_list.append(int(p_list[i][2]))
            kisyu_list.append(p_list[i][6])
        if p_list[i][3] is not "no_data":
            time_list.append(int(p_list[i][3]))
            distinct_time_list.append(int(p_list[i][1]))
        if p_list[i][4] is not "no_data":
            ashi_list.append(int(p_list[i][4]))
        if p_list[i][5] is not "no_data":    
            agari_list.append(float(p_list[i][5]))
    
    ###########距離処理
    ave_distinct = sum(distinct_list) / len(distinct_list)
    
    ############着順処理
    ave_order = sum(order_list) / len(order_list)

    #############時間処理
    for i in range(len(distinct_time_list)):
        time_list[i] = distinct_time_list[i] / time_list[i]              ##距離/時間で単位時間あたりに処理
    ave_time = sum(time_list) / len(time_list)

    #############脚質処理
    for i in range(len(ashi_list)):
        if ashi_list[i] == 1:
            count_1 += 1
        elif 2 <= ashi_list[i] <= 9:
            count_2 += 1
        else:
            count_3 += 1

    if max(count_1, count_2, count_3) == count_1:
        ashi = "逃げ"
    elif max(count_1, count_2, count_3) == count_2:
        ashi = "差し"
    else:
        ashi = "追い込み"
    
    ###########登り処理
    ave_agari = sum(agari_list) / len(agari_list)

    ####騎手処理
    for i in range(len(kisyu_list)):                   ###騎手の辞書を初期化
        kisyu_dict[kisyu_list[i]] = 0

    for i in range(len(kisyu_list)):                           ##着順3位以下の騎手をカウント
        if order_list[i] <= 3:
            kisyu_dict[kisyu_list[i]] = kisyu_dict.get(kisyu_list[i]) + 1
    kisyu = max(kisyu_dict.items(), key = lambda x:x[1])[0]
    
    store_list.append([ave_distinct, ave_order, ave_time, ashi, ave_agari, kisyu])
    #print(store_list)
    return store_list
    
def main():
    print("モジュール確認作業")


if __name__ == "__main__":
    main()