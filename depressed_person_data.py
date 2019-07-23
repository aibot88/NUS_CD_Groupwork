#!utf-8
import csv
import numpy as np
import random


temp = []
name_list = []
filter_list = []
conetxt_dic = {}
cnt = 0
# threshold = input('threshold:\t')
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
print('read full successfully')

with open('common.csv','r',encoding='utf-8') as f:
    content = f.readline()
    while content:
        filter_list.append(content.replace('\n','').replace(',',''))
        content = f.readline()
print("Read filtered_name list suc")

with open('common_person_data.csv','a',encoding='utf-8') as w:
    for item1 in filter_list:
        for item2 in filter_list:
            s_t = tuple((item1,item2))
            w.write(str(item1)+','+str(item2)+','+conetxt_dic[s_t])



