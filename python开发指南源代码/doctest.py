# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1

x=[]
x=map(format_name, ['adam', 'LISA', 'barT'])
for i in x:
    print(i)

y=[]

y=[j**2 for j in [1,2,3,4]]
for i in y:
    print(i)
    
z = []
z =list(filter(lambda x: x>0,[1,-2,3,-4]))

for i in z:
    print(i)

def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)