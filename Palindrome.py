# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:04:21 2020

@author: user
"""

# This function identify if provided string/number is palindrome or not

string=input("Enter any name or number:")
length=len(string)
rev=""
for i in range(0,length):
    rev=rev+string[length-1]
    length=length-1

if(string==rev):
    print(string,"is a Palindrome")
else :
    print(string,"is not a Palindrome")
    
    
        