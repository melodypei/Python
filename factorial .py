# -*- coding: utf-8 -*-

def fact(n):
    if n <= 1:
        return n
    return fact(n-1) * n
f = fact (10)
print(f)



def fact2(n):
    ret = 1
    for x in range(n,1,-1):
        ret *= x
    return ret
print(fact2(995))

