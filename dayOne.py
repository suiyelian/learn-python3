# Day one  主要了解一些python 基本但关键元素
# python 解释型语言 matlab一样 不用对变量进行类型声明
# python 对变量是对对象的引用(以数据为主，新的一个数据则是新的内存)，
# 执行动态类型机制，与C++，java等高级语不同的是，言可以绑定到不同的数据类型
# eg:
a = 1
print(a)
a = 'asdfas'
print(a)

# type()return var type

print(type(a))

# 元组 列表均可存储任何类型的数据项，但元组创建后不可变，用（）即可创建，列表如C语言数组，创建方法参考用户手册

b = ()  # 空元组

c = (1, ',', "asd")

print(b, c)

# len()函数返回数据项的长度 元组，列表，字符串都是有长度的

print(len(("asdas", )))  # 1

print(len(("asdas", 0)))  # 2

print(len([1, 2, 3]))     #3

# 逻辑操作符
# 身份操作符 is is not

a = 1
d = 1
x = a is d
print(x)

# 比较操作符 <, >, ==, 以及一些组合

a = 1
e = 1

x = a is e
print(x)

x = a == e
print(x)

# 成员操作符 in not in 主要针对序列 集合等类型

p = (4, "fog", 9)
print(4 in p, 5 not in p)

# 逻辑运算符 and not or  返回决结果的操作数

five = 5
two = 2
zero = 0

x1 = five and two  # 由第二个操作数决定结果 有点无聊的设定 但又很符合实际  醉了醉了
x2 = two and five
x3 = zero and five
print(x1, x2, x3)

# 控制流语句 此处介绍python最坑也最美好的地方，使用缩进进行代码块的划分，其他主流语言使用括号
# if while    （for in） continue(引导流程到循环入口)  break(退出当前循环) 以及异常处理try
'''
    if boolean_expression1:
        suite1
    elif boolean_expression2:
        suite2
    ...
    else:
        suite_else

    while boolean_expression:
        suite

    for variable in iterable:
        suite

    try:
       try_suite
    expect exception1 as variable1:
       exception_suite1
       ......
    expect exceptionN as variableN:
       exception_suiteN
eg:
'''

for test in [1, 2, 3, 4, 5]:
    print(test)

for test in "QWERTYUIOPASDFGHJKLZXCVBNM":
    if test in "QWERT":
        print(test, "sadas")
    else:
        print(test, "qwert")

s = input("enter an integer:")
try:
    i = int(s)
    print("integer:", i)
except ValueError as err:
    print(err)

# 算数运算符 int类型为固定，创建后不变 所以进行运算时是重新开辟一内存保存新的结果，再讲变量引用上去。
# 字符串的+=（中间留有一个空格） +（直接连接两字符串）也是固定的数据类型
# eg:

print("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break

if count:
    print("count =", count, "total =", total, "mean =", total / count)

# 函数的创建使用 import 导入模块
'''
    def functionName(argsList):
        suite
'''





