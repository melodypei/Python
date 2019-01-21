# -*- coding: UTF-8 -*-

'''
求输入数字的平方，如果平方运算后小于 50 则退出
'''

print ('如果输入的数字小于 50，程序将停止运行')
while True:
    a = int(input("请输入数字："))
    print(a ** 2)
    if a ** 2 < 50:
        break
