# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:00:31 2021

@author: hp
"""


str=input("Enter String:")
length=len(str)
for i in range(length):
    for j in range(length-i):
        print(str[i],end=" ")
    print()