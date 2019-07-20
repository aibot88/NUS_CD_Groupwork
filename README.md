# CD大作业小组讨论

## 写在最前面

    请老铁们对文件进行分支修改, 不要直接覆盖原文件; 乘此机会一起学习一下GitHub的基本操作哈.
---

## 古诗词共性探测

`txt_match.py`  文件是使用基本的词袋向量基于jieba包的搜索引擎分词模式`cut_for_search` . 进行最原始的诗句相似度计算文件;它证实了诗词相似度的评判是可行的, 但是这样的评判是不科学的, 接下来将给出使用隐式马尔科夫方法进行相似度计算的新方法.

`data`文件夹下放置了所需要用到的古诗文件

`txt_word2vec_match.py` 文件是基于word2vec的分词方式进行的短文本相似度计算方法, 还是一个demo; 不是很成熟

`weiboCrawler.py`文件下放的是基于GitHub上MIT协议的微博爬虫已经调整成我们所需要的文字模式; 所需要做的就是按照源码中的注释修改一下带爬取的人员uid; uid的获取方式在源码中有给出; 约在`第80行`; 数据保存在weibo_data目录中


## 微博原始数据 rawdata
`/data/rawdata` 中存放了所有1号2号，“撑不下去” “开心快乐”关键词的微博原始数据
