# -*- coding: UTF-8 -*-

'''
简化路径。给定一个文档(Unix-style)的完全路径，请进行路径简化。
"/home/", => "/home“
"/a/./b/../../c/", => "/c“
'''

def simplifyPath(path):
    st = []
    pp = path.split('/')
    for i in pp:
        if (i == '..') and st:
            st.pop()
        elif i and (i != '.') and (i != '..'):
            st.append(i)
    return "/"+"/".join(st)


            
print(simplifyPath("/home/"))
print(simplifyPath("/a/./b/../../../c/"))
