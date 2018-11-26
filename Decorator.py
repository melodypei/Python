# -*- coding: utf-8 -*-


import time
import datetime


def timeIt(func):
    def warp(arg):
        start = datetime.datetime.now()
        func(arg)
        end = datetime.datetime.now()
        cost = end - start
        print( 'execute %s spend %s'  % (func.__name__,cost.total_seconds()))
    return warp

@timeIt
def func(arg):
    time.sleep(arg)


func(3)

    
    
