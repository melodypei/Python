# -*- coding: UTF-8 -*-

'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

def mySum(n):
    a = 1
    b = 1
    sum = 0
    for i in range(n):
        sum += (a+b)/b
        a,b = b ,a+b
    return sum

print(mySum(20))
