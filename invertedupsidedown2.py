# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:04:37 2021

@author: hp
"""


str=input("Enter String:")
length=len(str)
for i in range(length):
    for j in range(i):
        print(" ",end=" ")
    for j in range(length-i):
        print(str[i],end=" ")
    print()