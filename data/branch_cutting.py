#!utf-8
import csv
import numpy as np
import random


temp = []
name_list = []
conetxt_dic = {}
mis = []
cnt = 0
dismat = []
threshold = input('threshold:\t')
simfilename = "input_data_full.csv"
with open("input_data_full.csv",'r',encoding='utf-8') as f:
    content = f.readline()
    while content:
        k = content.split(',')
        key = tuple(k[0:2])
        temp.append(k)
        if content.split(',')[0] not in name_list: name_list.append(content.split(',')[0])
        conetxt_dic[key] = content.split(',')[2]
        content = f.readline()
print('read successfully')

new_len =150
new_name_list = []
for i in range(new_len):
    index = random.randint(0,950)
    while name_list[index] in new_name_list: 
            index = random.randint(0,950)
    new_name_list.append(name_list[index])
print("new name_list create successfully")
sorted(new_name_list,key = lambda k: k[0])
print("sort Successfully")

counter = 0
with open('new_input_data.csv','a',encoding='utf-8') as f:
    f.write('source,target,weight\n')
    for it1 in new_name_list:
        for it2 in new_name_list:
            if conetxt_dic[(it1,it2)] > threshold:  f.write(str(it1)+','+str(it2)+','+str(conetxt_dic[(it1,it2)]))
            else: counter += 1
print("Ending\n %dis cutting, %d in total"%(counter,new_len*new_len))
