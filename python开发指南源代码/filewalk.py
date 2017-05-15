# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:22:25 2016

@author: 嫖一会
"""

import os
import os.path

rootdir = "G:/c++test/ConsoleApplication1"

for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        print("parent is :"+ parent)
        print("full path:" + dirname)
    for filename in filenames:
        print("p:" + parent)
        print("sd:" + os.path.join(parent,filename))