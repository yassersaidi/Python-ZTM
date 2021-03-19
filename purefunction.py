# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:42:24 2021

@author: yaser
"""



def add_n(item):
    return item+2

list = [1,2,3,4,5]
n = 2

new_list = list(map(add_n,list))
print(new_list) 