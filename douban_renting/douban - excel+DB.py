# -*- coding = utf-8 -*-
# @Time: 2020/5/30 19:57
# @Author: Yudong Zhong
# @File: douban.py
# @Software: PyCharm

"""
推荐视频课程：https://www.bilibili.com/video/BV12E411A7ZQ?p=16

查看robots协议：https://www.douban.com/robots.txt

零、流程
    准备工作 -> 获取数据 -> 解析内容 -> 保存数据

一、准备工作
    URL分析：
        首页  https://www.douban.com/group/558444/ （包含50条数据，和第一第二页数据相同）
        第一页 https://www.douban.com/group/558444/discussion?start=0
        第二页 https://www.douban.com/group/558444/discussion?start=25
        1）页面包含x条租房数据，每页25条
        2）每页的URL的不同之处：最后的数值 = (页数 - 1) * 25
    1、分析页面
        1）借助Chrome开发者工具（F12）来分析页面，在Elements下找到需要的数据位置。
        2）在页面中选择一个元素以进行检查（Ctrl+Shift+C）（开发者工具最左上方的小箭头），点击页面内容即可定位到具体标签位置。
        3）点击Network，可以查看每个时间点发送的请求和交互情况，可点击最上方小红点（停止记录网络日志Ctrl+E）停止交互。
        4）Headers查看发送给服务器的命令情况。
        5）服务器返回信息可在Response中查看。
    2、编码规范
        1）一般Python程序第一行需要加入
                    # -*- coding = utf-8 -*-
        这样可以在代码中包含中文。
        2）使用函数实现单一功能或相关联功能的代码段，可以提高可读性和代码重复利用率。
        3）Python文件中可以加入main函数用于测试程序
                    if __name__ == "__main__":
        4）Python使用#添加注释，说明代码（段）的作用
    3、引入模块
        sys, bs4 -> BeautifulSoup, re, urllib, xlwt

二、获取数据
    python一般使用urllib2库获取页面
    获取页面数据：
        1）对每一个页面，调用askURL函数获取页面内容
        2）定义一个获取页面的函数askURL，传入一个url参数，表示网址，如https://www.douban.com/group/558444/discussion?start=0
        3）urllib.Request生成请求，urllib.urlopen发送请求获取响应，read获取页面内容
        4）在访问页面时经常会出现错误，为了程序正常运行，假如异常捕获try...except...语句

三、解析内容
    对爬取的html文件进行解析
    1、使用BeautifulSoup定位特定的标签位置
    2、使用正则表达式找到具体的内容

四、保存数据
    Excel表格存储：利用python库xlwt将抽取的数据datalist写入Excel表格

Hint：
    1、添加筛选【浦东，张江，小区名，地铁站】
    2、添加租房详情内容（进入网页内抽取数据）
    3、保存图片，命名方式 (帖子序号)_x
    3、class获取各种不同途径信息（豆瓣，自如，链家，贝壳）

"""

import sys
from bs4 import BeautifulSoup   # 网页解析，获取数据
import re                       # 正则表达式，进行文件匹配
import urllib
import urllib.request           # 制定URL，获取网页数据
import urllib.error
import xlwt                     # 进行excel操作
import sqlite3                  # 进行SQLite数据库操作


def main():
    """
    1.爬取网页
    2.逐一解析数据
    3.保存数据
    :return:
    """
    print('开始爬取······')
    baseurl = 'https://www.douban.com/group/558444/discussion?start='
    # 1.爬取网页    2、逐一解析网页数据
    pagenum = 10
    datalist = getData(baseurl, pagenum)

    # 3.保存数据
    # 将数据保存在Excel中
    savepath = '豆瓣租房.xls'
    saveData(datalist, pagenum, savepath)
    # 将数据保存在数据库中
    dbpath = '豆瓣租房.db'
    saveData2DB(datalist, dbpath)
    # askURL('https://www.douban.com/group/558444/discussion?start=0')  # 测试askURL
    print('爬取完毕!')


def getData(baseurl, pagenum):
    datalist = []
    # 注意：正则表达式无法匹配空格，需用.*匹配或\s
    findTitle = re.compile(r'title="(.*?)"', re.S)              # 找到帖子名，有的帖子名带有\n
    findLink = re.compile(r'href="(.*?)"')                      # 找到帖子详情链接
    findRCount = re.compile(r'<.*class="r-count".*>(.*?)</td>') # 找到回帖数
    findRTime = re.compile(r'<.*class="time".*">(.*?)</td>')    # 找到最后回帖时间

    # 调用获取页面信息的函数pagenum次
    for i in range(0, pagenum):
        url = baseurl + str(i * 25)
        html = askURL(url)                              # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)                                   # 测试html是否能被解析
        for item in soup.find_all('tr', class_=''):     # 找到每一个帖子选项（查找符合要求的字符串，形成列表）
            # print(item)                               # 测试：查看item全部信息
            data = []
            item = str(item)                            # 转换成字符串
            # print(item)

            # 帖子名
            title = re.findall(findTitle, item)[0]
            # print(title)                              # 测试：查看title
            data.append(title)                          # 添加帖子名

            # 帖子详情链接
            link = re.findall(findLink, item)
            # print(link)                               # 测试：查看link信息
            if (len(link) == 2):
                data.append(link[0])                    # 添加详情链接
                # 作者链接
                # alink = re.findall(findLink, item)[1]
                # print(alink)                          # 测试：查看link信息
                data.append(link[1])                    # 添加发帖人主页链接
            else:
                data.append(link[0])
                data.append(' ')                        # 留空

            # 回帖数
            rcount = re.findall(findRCount, item)[0]
            # print(rcount)                             # 测试：查看回帖数
            if rcount == '':
                # print(0)                              # 测试：查看回帖数
                data.append(0)                     # 添加回帖数
            else:
                # print(rcount)                         # 测试：查看回帖数
                data.append(int(rcount))                     # 添加回帖数

            # 最后回帖时间
            rtime = re.findall(findRTime, item)[0]
            # print(rtime)
            data.append(rtime)                          # 添加最后回帖时间
            # otitle = titles[1].replace('/', '')       # 去掉无关符号，或re.sub()

            datalist.append(data)                       # 把处理好的一部电影信息放入datalist
    # print(datalist)                                   # 测试
    return datalist


# 得到指定一个URL的网页信息
def askURL(url):
    head = {    # 模拟浏览器头部信息，向豆瓣服务器发送消息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
    }   # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)   # 发送请求
    html = ''
    try:
        response = urllib.request.urlopen(request)  # 取得响应
        html = response.read().decode('utf-8')  # 获取网页内容
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def saveData(datalist, pagenum, savepath):
    # print('saving...')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣租房信息', cell_overwrite_ok=True)
    col = ('序号', '帖子名', '帖子详情链接', '发帖人主页链接', '回帖数', '最后回帖时间')
    for i in range(0, 6):
        sheet.write(0, i, col[i])   # 列名
    for i in range(0, pagenum*25):
        # print('第%d条' % (i+1))
        data = datalist[i]
        sheet.write(i+1, 0, i+1)
        for j in range(0, 5):
            sheet.write(i+1, j+1, data[j])  # 数据
    book.save(savepath)     # 保存
    # print('Successful!')


def saveData2DB(datalist, dbpath):
    init_DB(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index != 3:
                data[index] = '"'+data[index]+'"'   # 每项的字符串需要加上双引号或单引号
        sql = '''
            insert into renting(
            title, title_link, person_link, re_count, re_time)
            values(%s)''' % ",".join(str(v) for v in data)
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_DB(dbpath):
    # create table renting  # 不加if not exists每次运行程序需要先删除database，否则不用先删除，但无法更新sql里的格式
    sql = '''
        create table if not exists renting
        (
        id integer primary key autoincrement,
        title text,
        title_link text,
        person_link text,
        re_count numeric,
        re_time text
        )
    '''    # 创建数据表
    conn = sqlite3.connect(dbpath)  # 创建或连接数据库
    cursor = conn.cursor()          # 获取游标
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_DB('租房.db')  #测试db
