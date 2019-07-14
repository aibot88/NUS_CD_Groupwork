#!utf-8
#https://rare-technologies.com/word2vec-tutorial/
#min_count,0，100取决于数据集大小， size 几十到几百， wokers = 4
from gensim.models.word2vec import LineSentence, Word2Vec
from gensim.similarities import WmdSimilarity
import jieba 
import numpy as np
import random


name_list = []
poem_dict = {}
temp = []
# temp1 = []
poem_match_dict = {}
stopwords = [item.strip() for item in open("data/百度停用词表.txt",'r',encoding='utf-8').readlines()]
def match():
    model = 'data/m2v.mod'
    model_w2v = Word2Vec.load(model)
    sentences =list(LineSentence('data/cut_word.txt'))
    num_best = len(sentences)
    instance = WmdSimilarity(sentences, model_w2v,num_best = len(sentences))
    with open("data/weibo.txt","r",encoding='utf-8') as f:
            context = f.readline()
            while context:
                temp.append(context.split("\t"))
                context = f.readline()
                # if len(temp) >= 60178:
                #     break
    for item in temp:
        name_list.append(item[1].replace(" ",""))
    with open("data/input_data.csv","a",encoding='utf-8') as f:
        for item  in sentences:
            sims = instance[item]
            index1 = name_list[sentences.index(item)]
            # print(index1)
            for j in range(num_best):
                index2 = name_list[j]
                poem_dict[(index1,index2)] = 1-sims[j][1]
                f.write(str(index1)+","+str(index2)+","+str(1 - sims[j][1]))
                f.write("\n")
    # print(poem_dict)






    #         if key == name_list[i]:
    #             poem_match_dict[(name_list[i],key)] = 0
    #         if max_similarity<poem_match_dict[(name_list[i],key)]:max_similarity = poem_match_dict[(name_list[i],key)]
    #         if poem_match_dict[(name_list[i],key)] != 0:
    #             if min_similarity>poem_match_dict[(name_list[i],key)]:min_similarity = poem_match_dict[(name_list[i],key)]
    
    # for key_n, value in poem_match_dict.items():
    #     # print(poem_match_dict[key_n])
    #     poem_match_dict[key_n] = (value)/(max_similarity+min_similarity)
    #     tn = poem_match_dict[key_n]
    #     with open("data/input_data.csv","a",encoding='utf-8') as f:
    #         key_n = list(key_n)
    #         key_n.append(tn)
    #         # print(key_n)
    #         for ite in key_n:
    #             # print(ite)
    #             f.write(str(ite).replace('  ','')+" ")
    #         f.write('\n')   

    # print(poem_match_dict)

def main():
    flag = input("\nTrain or Match: ")
    if flag == "train":
        train()
        print('\nTrainning Successfully\n')
    if flag == "match":
        match()
        print("\nMatching finish\n")

if __name__ == "__main__":
    match()
    # main()
    # train()
    # simfilename = 'data/input_data.csv'
    # X = np.genfromtxt(simfilename, delimiter='\t', encoding='utf8', dtype=None)
    # print(X)