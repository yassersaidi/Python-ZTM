# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:43:17 2021

@author: yaser
"""
# from time import time

# t1 = time()
# print(list(range(1000000)))
# print(time()-t1)


def generat():
    for i in range(100):
        return i*2
        
g = generat()
print(g)
