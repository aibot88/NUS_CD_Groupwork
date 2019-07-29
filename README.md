# CD大作业小组讨论

## 写在最前面

请老铁们对文件进行分支修改, 不要直接覆盖原文件; 乘此机会一起学习一下GitHub的基本操作哈.
使用本項目之前, 先用`pip install -r requirements.txt`安裝所需的環境

---

---

## 微博共性探测

* `weibotxt_match.py`的match函数已经被wmd.py中的match函数取代, `weibotxt_match.py`文件目前只用于词典模型的训练, 日后会与wmd.py进行功能整合
* `wmd.py`文件使用gensim封装的WordMoveDistance函数来计算短文本之间的相似度是一种比基于word2vec但是比word2vec更高效的短文本相似度算法`instance(text)`会得到一个相似度降序排列的列表
* `data`文件夹下放置了所需要用的微博爬虫的各种数据(有抑郁症倾向和五抑郁症倾向各一半的数据)约1500条post简单解释一下data各种文件的解释, `.txt`文件都是中间临时变量,`.csv`是将运用于CD算法的数据.
* `louvain_new.py`文件用於進行Threshold的值來進行數據的篩選, 和louvain算法的使用, 最終將生成的數據使用前端代碼進行繪圖.
* ``文件是前端繪圖軟件, 最終的網站部署在<http://45.77.25.61:8080/SWS3001_TEAM5/>
![image](https://github.com/Talbot1/NUS_CD_Groupwork/raw/master/image/QR.png)

---

## 古诗词共性探测

最終并沒有私用一下文件; 但是他們可以用於進行詩歌的探測

* `txt_match.py`  文件是使用基本的词袋向量基于jieba包的搜索引擎分词模式`cut_for_search` . 进行最原始的诗句相似度计算文件;它证实了诗词相似度的评判是可行的, 但是这样的评判是不科学的, 接下来将给出使用隐式马尔科夫方法进行相似度计算的新方法.
* `data`文件夹下放置了所需要用到的古诗文件和微博爬虫的各种数据
* `txt_word2vec_match.py` 文件是基于word2vec的分词方式进行的短文本相似度计算方法, 还是一个demo; 不是很成熟
* `weiboCrawler.py`文件下放的是基于GitHub上MIT协议的微博爬虫已经调整成我们所需要的文字模式; 所需要做的就是按照源码中的注释修改一下带爬取的人员uid; uid的获取方式在源码中有给出; 约在`第80行`; 数据保存在weibo_data目录中;
=======
`weiboCrawler.py`文件下放的是基于GitHub上MIT协议的微博爬虫已经调整成我们所需要的文字模式; 所需要做的就是按照源码中的注释修改一下带爬取的人员uid; uid的获取方式在源码中有给出; 约在`第80行`; 数据保存在weibo_data目录中


## 微博原始数据 rawdata
`/data/rawdata` 中存放了所有1号2号，“撑不下去” “开心快乐”关键词的微博原始数据
