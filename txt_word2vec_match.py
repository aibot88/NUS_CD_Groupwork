#!utf-8
#https://rare-technologies.com/word2vec-tutorial/
#min_count,0，100取决于数据集大小， size 几十到几百， wokers = 4
from gensim.models.word2vec import LineSentence, Word2Vec
import jieba 
import numpy as np


name_list = []
poem_dict = {}
temp = []
temp1 = []
poem_match_dict = {}
stopwords = ['，','。',' ']

def train():
    with open("data/wulv-all.txt","r",encoding='utf-8') as f:
        while f.readline():
            temp.append(f.readline().split(":"))
            if len(temp) > 100:
                break
    for item in temp:
        name_list.append(temp[temp.index(item)][0])
        poem_dict[temp[temp.index(item)][0]] = temp[temp.index(item)][1]

    with open("data/cut_word.txt","a",encoding='utf-8') as f:
        for i in range(len(poem_dict)):
            words = jieba.cut_for_search(poem_dict[name_list[i]])
            f.write(name_list[i]+":")
            for word in words:
                if word not in stopwords:
                    f.write(word+' ')

    sentences = LineSentence('data/cut_word.txt')
    model = Word2Vec(sentences,min_count=3,size = 50,workers = 6)
    model.save('data/m2v.mod')

def match():
    txt = '欲上青天揽明月'
    target = 'data/cut_word.txt'
    model = 'data/m2v.mod'
    model_w2v = Word2Vec.load(model)
    stopwords = ['，','。',' ']
    with open("data/wulv-all.txt","r",encoding='utf-8') as f:
        while f.readline():
            temp.append(f.readline().split(":"))
            if len(temp) > 100:
                break
    for item in temp:
        name_list.append(temp[temp.index(item)][0])
        poem_dict[temp[temp.index(item)][0]] = temp[temp.index(item)][1]
    
    max_similarity = 0
    min_similarity = 100
    for i in range(len(poem_dict)):
        word = poem_dict[name_list[i]]
        # print(word)
        txt_cut = jieba.cut_for_search(word)
        txt_cut = [item for item in txt_cut if item in model_w2v.wv.vocab]
        for key,value in poem_dict.items():
            value_cut = list(jieba.cut_for_search(value))
            value_cut = [item for item in value_cut if item in model_w2v.wv.vocab]
            poem_match_dict[(name_list[i],key)] = (model_w2v.n_similarity(txt_cut,value_cut))
            if key == name_list[i]:
                poem_match_dict[(name_list[i],key)] = 0
            if max_similarity<poem_match_dict[(name_list[i],key)]:max_similarity = poem_match_dict[(name_list[i],key)]
            if min_similarity>poem_match_dict[(name_list[i],key)]:min_similarity = poem_match_dict[(name_list[i],key)]
    
    for key_n, value in poem_match_dict.items():
        poem_match_dict[key_n] = (value)/(max_similarity+min_similarity)
        tn = poem_match_dict[key_n]
        with open("data/input_data.csv","a",encoding='utf-8') as f:
            key_n = list(key_n)
            key_n.append(tn)
            # print(key_n)
            for ite in key_n:
                # print(ite)
                f.write(str(ite).replace('  ','')+" ")
            f.write('\n')   

    print(poem_match_dict)

def main():
    flag = input("\nTrain or Match: ")
    if flag == "train":
        train()
        print('\nTrainning Successfully\n')
    if flag == "match":
        match()
        print("\nMatching finish\n")

if __name__ == "__main__":
    # match()
    simfilename = 'data/input_data.csv'
    X = np.genfromtxt(simfilename, delimiter='\t', encoding='utf8', dtype=None)
    print(X)