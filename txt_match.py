'''
字典存前十个句子; 列表寸诗的名字
使用jieba全分词建立词袋列表
字典:用词袋列表里面的文字来表达整个诗句,将诗句向量化
建立第二个字典key为名字对, value 为相似的数量
'''
#!---utf-8---
import jieba


def Count(i):
    sum = 0
    for it in i: sum += 1
    return sum

temp = []
temp1 = []
name_list = []
poem_dict = {}
jieba_list = []
poem_match_dict = {}
with open("data/wulv-all.txt","r",encoding='utf-8') as f:
    while f.readline():
        temp.append(f.readline().split(":"))
        if len(temp) > 100:
            break
for item in temp:
    name_list.append(temp[temp.index(item)][0])
    poem_dict[temp[temp.index(item)][0]] = temp[temp.index(item)][1]
# print(name_list)
# print(poem_dict)
for key, value in poem_dict.items():
    poem_list = []
    temp_list = list(jieba.cut_for_search(value))
    for word in temp_list:
        if word not in jieba_list:
            jieba_list.append(word)
        poem_list.append(jieba_list.index(word))  
    poem_dict[key] = poem_list
# print(jieba_list)
# print(poem_dict)
sum_similarity = 0
for key1, value1 in poem_dict.items():
    for key2,value2 in poem_dict.items():
        poem_match_dict[(key1,key2)] = Count(set(value1) & set(value2))
        if key1 == key2:
            poem_match_dict[(key1,key2)] = 0
        sum_similarity += poem_match_dict[(key1,key2)]
for key, value in poem_match_dict.items():
    poem_match_dict[key] = int(value)/sum_similarity*100
print(poem_match_dict)


