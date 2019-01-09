# -*- coding: UTF-8 -*-


'''
合并两个排序的整数数组A和B变成一个新的数组。
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]。
'''

def  mergeSortedArray(A,B):
    ret = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            ret.append(A[i])
            i += 1
        else:
            ret.append(B[j])
            j += 1
    for k in range(i,len(A)):
        ret.append(A[k])
    for k in range(j,len(B)):
        ret.append(B[k])
    return ret


A=[1,2,3,8]
B=[4,5,6,9]
print(mergeSortedArrey(A,B))
