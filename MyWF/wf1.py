#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys
import re
import collections
import operator
import glob
file_name='F:\\研究生\\研究生作业\\构建之法作业\\第二次\\text.txt'
total=0
file=open(file_name,"r")  #open函数打开文件，str为文件名，'r'代表只读
for line in file.readlines():#读取行
    w = line.split(' ')     #空格为分隔符分割每行的单词，并返回字符串列表
    total=total + len(w)    #计算单词总数
 
print ("total ",total," words")       #总数结果打印
print('\n')
#相同单词出现次数
patt = re.compile("\w+")   #正则表达式
counter = collections.Counter(patt.findall(
    open(file_name,'rt').read()
    ))
for word, show in counter.most_common():  #用word变量记录单词，用show变量记录单词出现的频数，返回一个topn列表，其中不对counter.most_common(n)的n指定参数，返回所有元素

         print (word.ljust(20),":", show)