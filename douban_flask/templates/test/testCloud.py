# -*- coding = utf-8 -*-
# @Time: 2020/6/3 11:34
# @Author: Yudong Zhong
# @File: testCloud.py
# @Software: PyCharm

import jieba                            # 分词
from matplotlib import pyplot as plt    # 绘图，数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
import sqlite3                          # 数据库

# 参考文档：https://amueller.github.io/word_cloud/

con = sqlite3.connect('..\..\douban_renting.db')
cur = con.cursor()
sql = "select introduction from renting"
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))

img = Image.open(r'..\..\static\assets\img\tree.jpg')   # 打开遮罩图片
img_arr = np.array(img) # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_arr,
    font_path='msyh.ttc'    # 字体所在位置：C:\Windows\Fonts
).generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴

# plt.show()  # 显示生成的词云图片

# 输出词云图片到文件
plt.savefig(r'..\..\static\assets\img\word.jpg', dpi=500)