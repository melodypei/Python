# -*- coding: utf-8 -*-


import time
import datetime

def func(arg):
    time.sleep(arg)


def timeIt(func):
    def warp(arg):
        start = datetime.datetime.now()
        func(arg)
        end = datetime.datetime.now()
        cost = end - start
        print( 'execute %s spend %s'  % (func.__name__,cost.total_seconds()))
    return warp


new_func = timeIt(func) #这里会返回一个新的函数

new_func(3) #调用新的函数，并传值进去
     
    
    
