Spider.BC
=========================
#### 项目简介
应用Python爬虫、Flask框架、Echarts、WordCloud等技术将豆瓣租房信息爬取出来保存于Excel和数据库中，进行数据可视化操作、制作网页展示。

#### 主要内容包括三部分：
douban_renting：Python 爬虫将 [豆瓣租房](https://www.douban.com/group/shanghaizufang/)上的租房信息爬取出来，解析数据后将其存储于Excel和SQLite数据库中。

flask_demo：测试使用Flask框架。

douban_flask：应用Flask框架、Echarts、WordCloud技术将数据库中的租房信息以网页的形式展示出来。


[爬虫](./douban_renting/douban.py)

[Flask](./douban_flask/app.py)


Results
===========================
### 将爬取的数据保存于Excel中：
![爬虫得到的数据](/img/renting_excel.jpg)

### 以网页的形式将数据展示出来：  
#### 首页  
![首页](/img/index.jpg)  
#### 帖子列表  
![帖子列表](/img/list.jpg)  
#### 词云  
![词云](/img/word.jpg)

****
	
|作者|Donvink|
|---|---

****
