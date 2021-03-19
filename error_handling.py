# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:15:21 2021

@author: yaser
"""


# def print_smth(*args,**kawrgs):
#     try:
#         print(*args)
#     except TypeError():
#             print("can't print what you want")
        

   

# print_smth("yasst" , 4+"ss")

while True:
    num = int(input("enter number"))
    raise ValueError("test hhh")
    try:
        print(5/num)
    except ZeroDivisionError:
        print("Can't devied by 0 try again")
    else:
        print("Done!")
        break
    finally:
        print("Done with everything")
