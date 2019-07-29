## Readme      [English version is included as behind]

### 开发工具

```IntelliJ IDEA Ultimate 2019.1.3 x64```

```Gephi 0.9.2 x64```

### 网页介绍：

​	由于导航栏(``` siebar.jsp```)能插入的文字有限，故作一下介绍：

+ MainPage: ```intro.jsp```. 

  ​	主页，放了一张项目的海报

+ step 1：```sigmaNeoDemo.jsp```. 

  ​	966条微博数据构成的网络输入进CD算法(Louvain) 之后的结果。网络的Threshold被设置成0.05，可以保证每个点都包含在初始网络中。结果能够表明消极群体(黄色)与积极群体(浅蓝色)在发表的微博内容上具有较明显的不同。

+ mixed : ```mixed.jsp```. 

  ​	将step 1中的社区分析结果中的混合社区(橙色)再一次进行社区分析(Louvain)。然后能够比较明显的将不同社区划分出来。

+ depre：```depre.jsp```.

  ​	 将step 1中的消极社区(黄色)再一次进行社区分析(Louvain)。能够明显的将具有抑郁倾向的人群聚类到同一个紧密连接的小社区中（我们人为的检查了这些用户的主页，发现其中近70%的用户的确会经常发一些内容极度消极的微博，或者提到“抑郁”、“死亡”等字眼，甚至有一些抑郁症的诊断经历）。

+ step 2 ： ```48.jsp```.

  ​	将depre中聚类出来的我们确定为抑郁症（至少是潜在抑郁症）的用户，外加上我们通过“#抑郁症”或者“#走饭”等tag寻找到的抑郁症用户，一共48位，我们取了每个人3-5条微博来代表一个用户的微博文本数据，来进行社区分析(Louvain)，可以发现这些用户明显的被聚成了4小类。

+ WordHist： ```wordsCount.jsp```.

  ​	直方统计图，统计了这4类抑郁用户的共性，发现了他们经常使用的高频词汇。

+ TimeLine：```more.jsp```

  ​	统计图，统计了抑郁用户经常发布微博的(平均)时间以及微博条数。

### 画图所使用的库：

​	step 1(```sigmaNeoDemo.jsp```)由于节点数目较多，使用了```sigma.js```，其余关系图及统计图均使用了百度开发的```echarts.js```

```---------------------------------------------------------------```

## Readme

### Development tools:

```IntelliJ IDEA Ultimate 2019.1.3 x64```

```Gephi 0.9.2 x64```

### Introduction to the web page:

​	Because of the limitation of the size of the sidebar(``` siebar.jsp```), here is a brief intro to what each web page represents.

- MainPage: ```intro.jsp```. 

  ​	Main page, a rough poster of this project.

- step 1：```sigmaNeoDemo.jsp```. 

  ​	The graph generated from the CD algorithm(Louvain) and there are 996 pieces of Weibo posts in our initial dataset. And the threshold is set as 0.05 so that all the nodes could be included in the net before put into Louvain. The result shows that there is a huge difference in the content of posts between the negative community(in yellow) and the positive community(in light blue).

- mixed : ```mixed.jsp```. 

  ​	Again, Louvain is applied on the mixed community(in orange) from the graph of step 1. And then we can see the CD algorithm can divide all the communities much more efficiently.

- depre：```depre.jsp```.

  ​	To make potential depressive community clearer, we put the negative community in step 1 into CD algorithm(Louvain). This time all the depressive people are mainly included in one communities and the connections between these nodes are quite close. Manually we check their main page and we are certain that 70% of them are potential depressive individuals.

- step 2 ： ```48.jsp```.

  ​	There are 48 depressive users in the graph and some of them are the depressive individuals we get from ```depre``` above and others are depressive users who we select through the hashtag ```#depressive disorders```. And we choose 3-5 pieces of posts to represent each user. After CD we can find out that the users are divided into 4 communities with their own group characteristics.

- WordHist： ```wordsCount.jsp```.

  ​	The histogram which shows common words mentioned in the posts of the depressive users.

- TimeLine：```more.jsp```

  ​	The curve chart which shows the number of posts in different periods during a day.

### The JS libraries used in generating the graph

​	step 1 have used ```sigma.js``` due to the large number of the nodes. Others have used ```echarts.js``` developed by Baidu.