# -*- coding = utf-8 -*-
# @Time: 2020/6/1 15:35
# @Author: Yudong Zhong
# @File: testXwlt.py
# @Software: PyCharm

import xlwt

# book = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
# sheet = book.add_sheet('sheet1')        # 创建工作表
# sheet.write(0, 0, 'hello')              # 写入数据：第一个参数“行”，第二个参数“列”，第三个参数“内容”
# book.save('testXwlt.xls')               # 保存数据表

# 9x9乘法表
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('乘法表')
for i in range(1, 10):
    for j in range(i, 10):
        # sheet.write(i-1, j-1, str(i)+'x'+str(j)+'='+str(i*j))
        sheet.write(i-1, j-1, '{} x {} = {}'.format(i, j, i*j))
        pass
    pass
book.save('testXwlt.xls')
