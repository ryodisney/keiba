#cording:utf-8

import numpy as np
import itertools as itr

def Weight(ave_list_past):
    parameter_list = np.zeros(5)
    
    #パラメータを作るための変数
    A = range(5)
    B = range(5)
    C = range(5)
    D = range(5)
    E = range(5)

    parameter_list = list(itr.product(A,B,C,D,E))

    score_data = []
    flag = False
    min_list = []

    for parameter in parameter_list:
        #行列に変換
        parameter_array = np.array(parameter)
    
        for list_past in ave_list_past:
            data = np.array(list_past)
            score_data.append(np.dot(parameter_array,data))

        flag = Judge_Sort(score_data,flag)

        if flag == True:
            min_list.append(parameter_array.tolist())
            print("Yes!")
            flag = False
        

    print(min_list)

def Judge_Sort(score_data,flag):
    
    if sorted(score_data) == score_data:
        flag = True
        
    return flag


def main():
    print("モジュール確認作業")

    #パラメータを作るための変数
    A = range(10)
    B = range(10)
    C = range(10)
    D = range(10)
    E = range(10)

    parameter_list = list(itr.product(A,B,C,D,E))
    print(len(parameter_list))
    


if __name__ == "__main__":
    main()