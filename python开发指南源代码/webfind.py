# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:58:25 2017

@author: 卜云辉

"""

from __future__ import division
 
class DivisionException(Exception):
      def __init__(self, x, y):
            Exception.__init__ (self, x, y)       #ַԃܹ`ք__init__޸ѐԵʼۯ
            self.x = x
            self.y = y
 
if __name__ == "__main__":
    try:
        x = 3
        y = 2      
        if x % y > 0: 
            print(x/y)
            raise DivisionException(x, y)
    except DivisionException as div:                     #div ҭʾDivisionExceptionքʵ}הг
          print("DivisionExcetion: x/y = %.2f" % (div.x/div.y))

