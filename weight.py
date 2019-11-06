#cording:utf-8

import numpy as np

def Weight(ave_list_past):
    parameter_list = np.zeros(5)
    MAX = 25
    score_data = []
    flag = False
    min_list = []

    while(parameter_list[-1] < MAX):
    
        for list_past in ave_list_past:
            data = np.array(list_past)
            score_data.append(np.dot(parameter_list,data))

        flag = Judge_Sort(score_data,flag)

        if flag == True:
            min_list.append(parameter_list.tolist())
            flag = False
        
        parameter_list = Change_parameter(parameter_list,MAX)

    print(min_list)

def Judge_Sort(score_data,flag):
    
    if sorted(score_data) == score_data:
        flag = True
        
    return flag


def Change_parameter(parameter_list,MAX):
    for i,weight_parameter in enumerate(parameter_list):
        if weight_parameter < MAX:
            weight_parameter += 1
            parameter_list[i] = weight_parameter
            break

    return parameter_list

def main():
    print("モジュール確認作業")
    """
    parameter_list = np.zeros(5)
    MAX = 10

    while(parameter_list[-1] < MAX):
        parameter_list = Change_parameter(parameter_list,MAX)
        print(parameter_list)
    """

if __name__ == "__main__":
    main()