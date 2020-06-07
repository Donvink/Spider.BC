# -*- coding = utf-8 -*-
# @Time: 2020/5/31 22:18
# @Author: Yudong Zhong
# @File: testRe.py
# @Software: PyCharm

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re

# 创建模式对象
# pat = re.compile('AA')  # 此处的 AA 是正则表达式，用来验证其他的字符串
# m = pat.search('CAAFBAAD')  # search字符串被校验的内容，返回匹配的第一个位置Match对象
# m = re.search('asd', 'Aasd')    # 前面的字符串是规则（正则表达式），后面的字符串是被校验的对象
# m = re.findall('a', 'HINsaDakK')    # 前面的字符串是规则（正则表达式），后面的字符串是被校验的对象
# m = re.findall('[A-Z]+', 'HINsaDakK')    # 前面的字符串是规则（正则表达式），后面的字符串是被校验的对象
# print(m)

# sub
m = re.sub('a', 'A', 'abcsainags')    # 找到a，用A替换
print(m)

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r'\adfe\sdf\-'
print(a)
