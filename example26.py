# -*- coding: UTF-8 -*-

'''
利用递归方法求5!
'''

def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)

print(f(4))
