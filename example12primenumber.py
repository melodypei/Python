# -*- coding: UTF-8 -*-


count = 0

for i in range (101,200):
    for j in range(2,i):
        if (i%j == 0):
            break
    else:
            count += 1
            print(i)
print(count)



