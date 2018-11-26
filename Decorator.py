# -*- coding: utf-8 -*-


import time
import datetime
import functools


def timeIt(func):
    @functools.wraps(func)
    def wrap(arg):
        start = datetime.datetime.now()
        func(arg)
        end = datetime.datetime.now()
        cost = end - start
        print( 'execute %s spend %s'  % (func.__name__,cost.total_seconds()))
    return wrap

@timeIt
def func2(arg):
    '''this is in func2'''
    time.sleep(arg)


func2(3)
print (func2.__name__)
print (func2.__doc__)
print (func2.__module__)

    
    
