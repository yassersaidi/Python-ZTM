# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:22:40 2021

@author: yaser
"""
from time import time
def feb(num):
    t1 = time()
    s = 0 
    x = 1
    for i in range(num):
        f = s
        s = x
        x = f + x
        print(f"{i} => {f}")
    t2 = time()
    return f"Tooks {t2-t1}s"

