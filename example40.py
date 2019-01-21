# -*- coding: UTF-8 -*-

'''
将一个数组逆序输出。
'''

def verseList(a):
    for i in range(len(a)//2):
        a[i],a[-i-1] = a[-i-1],a[i]
    return a

a = [9, 6, 5, 7, 7, 4, 1, 3]
print(verseList(a))
