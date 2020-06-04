# -*- coding = utf-8 -*-
# @Time: 2020/5/31 9:31
# @Author: Yudong Zhong
# @File: testUrllib.py
# @Software: PyCharm

import urllib.request


# # 获取一个get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))


# # 获取一个post请求
# # 测试http的网址 httpbin.org
# # 模拟用户真实登录
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data)
# print(response.read().decode('utf-8'))


# # 超时处理
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)


# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Bdqid'))


# 伪装浏览器
# 打开baidu网页 -> F12 -> Network(网络) -> 刷新网页 -> 点击左上角红点停止刷新 -> 鼠标放在第一条横线
# -> 点击下方www.baidu.com -> 点击左侧Headers(标头) -> 最底部 User-Agent -> 复制
# # url = 'https://www.douban.com'
# url = 'http://httpbin.org/post'
# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
# }
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url = 'https://www.douban.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))