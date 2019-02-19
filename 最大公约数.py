# -*- coding: UTF-8 -*-


def myNum(a,b):
    if (a < b):
        a, b = b,a
    if (a % b) == 0:
        return b
    while(a % b)>0:
        a = a % b
        if (a < b):
            a, b = b, a
        if (a % b) == 0:
            return b

print(myNum(4,24))
