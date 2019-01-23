# -*- coding: UTF-8 -*-


'''
对于一个给定的 source 字符串和一个 target 字符串，
你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
如果不存在，则返回 -1。

'''

def findString(source,target):
    if (source is None) or (target is None):
        return -1
    for i in range(len(source)-len(target)+1):
        if source[i:i+len(target)] == target:
            return i
    return -1


print(findString('source','target'))

print(findString('abcdefg','def'))
