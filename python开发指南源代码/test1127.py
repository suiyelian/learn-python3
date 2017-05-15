#encoding=utf-8

def sum(a,b):
    return a+b


spath = "test.txt"

f = open(spath,"w+")
f.write(" sdas\n")
f.writelines("asdasdsdas2")
f.close()

f = open(spath,"r")
for line in f:
    print("asdas%s" %line)
f.close()
