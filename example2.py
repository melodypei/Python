# -*- coding: UTF-8 -*-



i = int(input("请输入净利润："))

money = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]

r = 0

for idx in range(0,6):
    if i > money[idx]:
        r += (i-money[idx]) * rate[idx]
        print ((i-money[idx]) * rate[idx])
        i = money[idx]

print(r) 

                
    
    
