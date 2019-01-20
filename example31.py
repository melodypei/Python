# -*- coding: UTF-8 -*-

'''
请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
'''

#Monday Tuesday Wednesday Thursday Friday Saturday Sunday

while True:
    
    l1 = input("请输入第一个字母：")

    if l1 == 'M' or l1 == 'm':
        print("Monday")
    elif l1 == 'W' or l1 == 'w':
        print("Wednesday")
    elif l1 == 'F' or l1 == 'f':
        print("Friday")
    elif l1 == 'T' or l1 == 't':
        l2 = input("输入第二个字母：")
        if l2 == 'u':
            print("Tuesday")
        elif l2 == 'h':
            print("Thursday")
        else:
            print("error")
            break
    elif l1 == 'S' or l1 == "s":
        l2 = input("输入第二个字母：")
        if l2 == 'a':
            print("Saturday")
        elif l2 == 'u':
            print("Sunday")
        else:
            print("error")
            break
    else:
        print("error")
        break
