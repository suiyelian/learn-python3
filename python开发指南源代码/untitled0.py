# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:48:50 2017

@author: 卜云辉

"""
import sys

def p(nt=0):
    while True:
        re = (yield nt)
        if re is None:
            nt += 0.25
        else:
            nt =re
     

res = []
ge = p()

print(ge.__next__())

while len(res)<5:
    x = next(ge)
    if abs(x-0.5)<sys.float_info.epsilon:
        x = ge.send(1.0)
    res.append(x)
print(res)

