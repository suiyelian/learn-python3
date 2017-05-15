# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:01:26 2017

@author: 卜云辉
"""

# 标识符 与 关键字参考其他高级语言 与用户手册 Python 有预定义的标识符 不要与之重复 最好定义一个明确的特性标识符
# dir() 函数可以返回一个对象的内置属性列表。不带参数时返回Python的内置属性列表
import sys
import collections

# print(dir())
# print(dir(__package__))


# integral类型 有 int bool 两个数据类型
'''
   x/y 得到浮点数
   x//y 得到整数
   % 取模  x**t x的t次幂
   ads 绝对值 divmod（x,y）返回商和余数  pow（x，y） pow(x,y,z) x**y %z round(x,n)
   创建一个对象可以使用= 或者使用数据类型进行创建
   数据类型进行创建：不使用参数调用数据类型 使用一个参数（新对象是原始对象的一个浅拷贝）
'''

# 浮点类型 float complex 标准库中的decimal.Decimal类型 均为固定类型  conjugate()改变虚数部分符号

def equal_float(a, b):
    return (a - b) <= sys.float_info.epsilon
print(equal_float(1.0, 1.0))

# 字符串使用固定不变得str数据类型表示的 可以作为数据类型进行函数调用str("ada") 字符串为一序列 可进行[]以及分片操作
# 强大的字符串格式化工具format（）方法 有点像c语言的print 有位置参数与关键字参数之分，其中关键字参数在位置参数后面

print("asda'asda'\"asdas\"asda")

'''
def extract_from(tag,line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        print(i)
        start =i + len(opener)
        print(start)
        j = line.index(closer,start)
        print(j)
        return line[start:j]
    except ValueError:
        return None

print(extract_from("red", "what a<red>rose</red>"))
'''

print("asdasd'{0}'asda".format("SB")) # 如果需要出现{} 则需要将其写成{{}}
x = 3
s = "{0}{1}{2}"
s = s.format("asda", x, "asdas")
print(s)

# locals()函数返回当前作用范围内的局部变量 是一个字典类型 用**映射字典的值

e = "sas"
n = 4
"E{n}is{e}".format(**locals())
# output: E4ise

c = False

print((not c))

#  序列类型 内置五种序列类型： bytearray bytes list str tuple  都支持成员关系操作符（in） 大小计算函数（len（））分片（[]）
#  元组tuple 使用连接操作符+ *（赋值 ） []分片 in 或者 not in 测试成员关系 元组从左到右从零开始编号 从右向左从-1开始编号
# del取消对象引用到数据的绑定

hair = "asda","asda"
print(hair[-2:])

hair = hair[:1], "asd", hair[1:]

print(hair)
# 为得到一个一元组应该使用加号进行元组连接
h = hair[:1] + ("asd",) + hair[1:]

print(h)

Sale = collections.namedtuple("Sale", "x,y,z") # 第二个参数为想要的参数列表
s = []

s.append(Sale(1, 2, 3))
s.append(Sale(1, 2, 3))
p = Sale(1, 2, 3)

print(p._asdict())
print(s)

num = [1]
for i in range(len(num)):
    num[i] += 1

print(num)

test1 = [1,2,3,4]
test1[1:2] = []
print(test1)

# 使用列表内涵可以简化代码 语法格式为：[expression for item in iterable if condition]
# 集合是0个或多个对象引用的无序组合，这些对象所引用的对象都是可哈希运算的 集合是可变的 无序的 因此不能通过下表引用 集合元素是没有重复的
# 可通过set()函数 {}创建
# 采用frozenset（）函数可以创建一个固定集合
# 字典是一种无序的组合数据类型 包含0个或多个键值对


