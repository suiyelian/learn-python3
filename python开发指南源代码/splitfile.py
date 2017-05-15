# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:30:27 2016

@author: 嫖一会
"""
import os.path

spath = "G:/c++test/ConsoleApplication1"

f,p = os.path.split(spath)
print("dir is :" + p)
print("file is:" + f)

drv,left = os.path.splitdrive(spath)
print("dir is :" + drv)
print("file is:" + left)

f,txt = os.path.splitext(spath)
print("dir is :" + f)
print("file is:" + txt)

try:
    fh = open("tes.txt", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print ("关闭文件")
        fh.close()
except IOError:
    print( "Error: 没有找到文件或读取文件失败")