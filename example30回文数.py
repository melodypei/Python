# -*- coding: UTF-8 -*-

'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

def isNum(n):
    flag = True
    for i in range(len(str(n))//2):
        if str(n)[i] != str(n)[-i-1]:
            flag = False
            break
    return flag
        
            

print(isNum(1356531))
