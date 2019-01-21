# -*- coding: UTF-8 -*-

'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''


def insertNum(a,n):
    l = len(a)
    if n>=a[-1]:
        a.append(n)    
    else:
        a.append(0)
        for i in range(l):
            if n < a[i]:
                temp1 = a[i]
                a[i] = n
                for j in range(i+1,l+1):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    return a

a = [1,4,6,9,13,16,19,28,40,100]
print(insertNum(a,100))
