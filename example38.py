# -*- coding: UTF-8 -*-

'''
求一个3*3矩阵主对角线元素之和
'''


a = []
sum = 0

for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(input("请输入整数："))

for i in range(3):
    sum += int(a[i][i])

print(sum)
