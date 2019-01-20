# -*- coding: UTF-8 -*-

'''
求1+2!+3!+...+20!的和
'''


mul = 1
a = []
sum = 0
for i in range(1,21):
    mul = mul * i
    a.append(mul)
for i in a:
    sum += i

print(sum)
