# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 23:53:11 2021

@author: hp
"""


str=input("Enter String:")
length=len(str)
for i in range(length):
    for j in range(i+1):
        print(str[j],end=" ")
    print()