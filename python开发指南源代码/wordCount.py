# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:58:25 2017

@author: 卜云辉

"""

# 打印文件中的web站点 存在严重bug
import sys
import os
num = {name:os.path.getsize(name) for name in os.listdir(".")}
print(num)
sites = {}
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
          
            if i > -1:
                i += len("http://")
               
                for j in range(i, len(line)):
                    # isalnum 检查字符串是否由数字或字母组成
                    if not (line[j].isalnum() or line[j] in ".-"):
                        print(line[j])
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    print("sa",site)
                    sites.setdefault(site, set()).add(filename)
                i = j
            else:
                break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))
