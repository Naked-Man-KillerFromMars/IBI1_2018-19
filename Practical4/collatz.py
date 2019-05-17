# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:46:40 2019

@author: 11601
"""
#get random number, so we don't need to alter the n every time
from random import randint
n = randint(1,101) #these two steps are to assign one random integer to n and print it
print(n)
while n!=1: #keep doing the following collatz calculation until the n equals to 1
  if n%2==0:#if the n can be divided by 2, then divide it by 2 and print the outcome as integer
     n=n/2
     print(int(n))
  else:#if it can not be divided by 2, multiply it by 3 and add 1 to it, also print outcome as integer
     n=3*n+1
     print(int(n))
