#!/usr/bin/python
# coding:utf-8

"""
@author: David
@software: PyCharm
@file: jieba_demo.py
@time: 2018/8/29 0:04
"""

import jieba
#用户字典
jieba.load_userdict("user_dict.txt")

#全模式
#words = jieba.cut("我来自北京理工大学",cut_all=True)

#精确模式
words = jieba.cut("大鹏主演的屌丝男士上了微博热搜", cut_all=False)
print("/".join(words))


def main():
    pass


if __name__ == "__main__":
    main()
