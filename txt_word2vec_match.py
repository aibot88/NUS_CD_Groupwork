#!utf-8
#https://rare-technologies.com/word2vec-tutorial/
#min_count,0，100取决于数据集大小， size 几十到几百， wokers = 4
from gensim.models.word2vec import LineSentence, Word2Vec
import jieba 


name_list = []
poem_dict = {}
temp = []
temp1 = []
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

    txt_cut = list(jieba.cut_for_search(txt))
    txt_cut = [item for item in txt_cut if item in model_w2v.wv.vocab]
    score = []
    for key,value in poem_dict.items():
        value_cut = list(jieba.cut_for_search(value))
        value_cut = [item for item in value_cut if item in model_w2v.wv.vocab]
        score.append(model_w2v.n_similarity(txt_cut,value_cut))
    score.sort(key=lambda x: x)
    print(score)

def main():
    flag = input("\nTrain or Match: ")
    if flag == "train":
        train()
        print('\nTrainning Successfully\n')
    if flag == "match":
        match()
        print("\nMatching finish\n")

if __name__ == "__main__":
    main()