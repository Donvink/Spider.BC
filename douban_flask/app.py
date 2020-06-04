from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

# Edit Configurations -> FLASK_DEBUG √


# 主页
@app.route('/')
def index():
    return render_template('index.html')


# 首页
@app.route('/index')
def home():
    # return render_template('index.html')
    return index()


# 帖子详情
@app.route('/title')
def title():
    datalist = []
    con = sqlite3.connect('douban_renting.db')  # 连接数据库
    cur = con.cursor()                          # 获取游标
    sql = "select * from renting"               # 数据库操作
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()                                 # 关闭游标
    con.close()                                 # 关闭数据库连接
    return render_template('title.html', renting=datalist)  # 将datalist传递给网页


# 团队
@app.route('/person')
def person():
    return render_template('person.html')


# 词云
@app.route('/word')
def count():
    return render_template('word.html')


# 详细信息
@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run()
