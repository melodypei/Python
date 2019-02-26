# -*- coding: UTF-8 -*-


def collatz(number):
    if number%2 == 0:
        print(number//2)
        return (number//2)
    else:
        print(3*number+1)
        return(3*number+1)

while True:
    try:
        num = int(input("请输入一个整数："))
        break
    except ValueError:
        print("不是整数，请重新输入")
    
while True:
    if num <= 0:
        print("必须是正整数")
        break
    else:
        num = collatz(num)
        if num == 1:
            break
