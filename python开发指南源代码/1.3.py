# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:58:25 2017

@author: 卜云辉
"""
import string
import sys

# 计算各个单词在所有输入文件中出现的次数
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            print(word)
            word = word.strip(strip) #移除字符串头尾参数所指定的字符
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
print(words)
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))