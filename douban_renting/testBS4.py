# -*- coding = utf-8 -*-
# @Time: 2020/5/31 13:03
# @Author: Yudong Zhong
# @File: testBS4.py
# @Software: PyCharm

"""
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种
- Tag
- NavigableString
- BeautifulSoup
- Comment
"""

from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import urllib.error

url = "http://www.baidu.com"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
# print(response.read().decode('utf-8'))
# file = open('./baidu.html', 'rb')
# html = file.read()
bs = BeautifulSoup(html, 'html.parser')
# print(bs.title)
# print(bs.head)
# print(bs.a)

# # 1、Tag 标签及其内容，拿到它所找到的第一个内容
# print(type(bs.title))
# print(bs.title.string)

# # 2、NavigableString 标签里的内容（字符串）
# print(type(bs.title.string))
# print(bs.a.attrs) # 拿到标签里所有的内容，返回字典

# # 3、BeautifulSoup 表示整个文档
# print(type(bs))
# print(bs)
# print(bs.name)
# print(bs.attrs)

# 4、Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
# print(type(bs.a.string))


# --------------------------------------------
# 文档的遍历（更多内容搜索BeautifulSoup遍历文档树）
# --------------------------------------------
# 1、contents：获取Tag的所有子节点，返回一个list
# Tag的.contents属性可以将Tag的子节点以列表的方式输出
# print(bs.head.contents)
# 用列表索引来获取它的某一个元素
# print(bs.head.contents[1])
# 2、children：获取Tag的所有子节点，返回一个生成器
# for child in bs.head.children:
#     print(child)


# --------------------------------------------
# 文档的搜索
# --------------------------------------------
# 1、find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
# tlist = bs.find_all('a')
# print(tlist)

# 正则表达式搜索：使用search()方法来匹配内容
# tlist = bs.find_all(re.compile('a'))
# print(tlist)

# 方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr('name')
# tlist = bs.find_all(name_is_exists)
# print(tlist)
# for item in tlist:
#     print(item)

# 2、kwargs 参数
# tlist = bs.find_all(id='head')
# tlist = bs.find_all(class_=True)
# tlist = bs.find_all(herf='http://news.baidu.com')
# for item in tlist:
#     print(item)

# 3、text 参数
# tlist = bs.find_all(text='hao123')
# tlist = bs.find_all(text=['hao123', '地图', '贴吧'])
# tlist = bs.find_all(text=re.compile('\d')) # 应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in tlist:
#     print(item)

# 4、limit 参数
# tlist = bs.find_all('a', limit=3)
# for item in tlist:
#     print(item)

# css 选择器
# tlist = bs.select('title')  # 通过标签来查找
# tlist = bs.select('.mnav')  # 通过类名来查找
# tlist = bs.select('#u1')  # 通过id来查找
# tlist = bs.select('a[class="bri"]')  # 通过属性来查找
# tlist = bs.select('head > title')  # 通过子标签来查找
tlist = bs.select('.mnav ~ .mnav')  # 通过兄弟标签来查找
print(tlist[0].get_text())
# for item in tlist:
#     print(item)