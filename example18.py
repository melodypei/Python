# -*- coding: UTF-8 -*-

from functools import reduce

'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

m= 0
n = []
a = int(input("qingshuru:"))
b = int(input("qingshuru:"))

for i in range(a):
    m += b
    b = b * 10
    n.append(m)
    print(n[i])
    
print(reduce(lambda x,y:x+y,n))



a = input("数字为：")
b = int(input("个数为："))
s=''
c= []
sum = 0
for j in range(b):
    s += a
    c.append(s)
print(c)

for k in c:
    sum+=int(k)
print(sum)






    


            
    
    


