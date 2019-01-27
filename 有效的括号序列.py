# -*- coding: UTF-8 -*-

'''
有效的括号序列：给定一个字符串所表示的括号序列，
包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列
'''

def isValidParentheses(s):
    st = []
    if (s[0] == ')') or (s[0] == ']') or (s[0] == '}'):
        return False
    for i in s:
        if (i == '(') or (i == '[') or (i == '{'):
            st.append(i)
        elif not check(i,st):#检查成功就继续循环，不成功就返回false
            return False
    if len(st) == 0:
        return True
    else:
        return False

def check(c,st):
    if st is None:
        return False
    elif ((c == ')' and st[-1] == '(')  or \
          (c == ']' and st[-1] == '[')  or \
          (c == '}' and st[-1] == '{')):
        st.pop()
        return True
    else:
        return False


print(isValidParentheses('([{}])'))      
print(isValidParentheses('([}])'))             
print(isValidParentheses('([{'))
print(isValidParentheses('{)]}'))
print(isValidParentheses(')]}')) 
