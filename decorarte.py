# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:08:22 2021

@author: yaser
"""
from time import time

def forker(n):
    if n == 0:
        return 1
    else:
        return n*forker(n-1)
     
def doci(func):
    def mul_five(n):# func(*args,**kawrgs) hadi dirha when u don't know how many parameters u need in the functoin
        print("/////")
        print(func(n)*5)
        print("/////")
    return mul_five

def perf(fn):
    def wrapper(*args,**kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(f"took {t2-t1}s")
        return result
    return wrapper
  
@perf
def count():
    for i in range(100000000):
        i*5

count()
      
        

# @doci
# def number(n):
#     return n


    