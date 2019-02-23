# -*- coding: UTF-8 -*-


def twoSum(ll, target):
    result = []
    for i in range(len(ll)-1):
        for j in range(i + 1, len(ll)):
            if (ll[i] + ll[j]) == target:
                    result.append((ll[i],ll[j]))
                    break
    return result

l = [2,3,5,7,5,0,9]
print(twoSum(l,7))
