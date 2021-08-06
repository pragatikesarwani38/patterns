# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:03:33 2021

@author: hp
"""


str=input("Enter String:")
length=len(str)
for i in range(length):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1):
        print(str[j],end=" ")
    print()