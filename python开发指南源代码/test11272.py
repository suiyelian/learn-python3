# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:08:51 2016

@author: 嫖一会
"""

class Base:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
        
class child(Base):
    def plus(self,a,b):
        return a+b

mychild = child()

mychild.add("sad")

print(mychild.data)

print(mychild.plus(2,3))
