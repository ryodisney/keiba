#cording:utf-8

import numpy as np
import itertools as itr

def Weight(ave_list_past):
    parameter_list = np.zeros(5)
    
    #パラメータを作るための変数
    A = range(1,26)
    B = range(32,801,32)
    C = range(16,401,16)
    D = range(4,101,4)
    E = range(4,101,4)

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
        
        print(parameter)
        score_data.clear()
        

    print(min_list)

def Judge_Sort(score_data,flag):
    
    score_data_sorted = sorted(score_data)

    for i,score in enumerate(score_data_sorted):
        if score == score_data[i]:
            if i > 1:
                flag = True
                break
        
        else:
            break
    
    return flag

        
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