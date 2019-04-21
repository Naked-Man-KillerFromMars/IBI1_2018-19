## -*- coding: utf-8 -*-
#"""
#Created on Wed Apr  3 09:13:45 2019
#
#@author: 11601
#"""

from random import randint
N = randint(1, 10)
print(N)

import random 
def Rand(start, end, N): 
    res = [] 
  
    for j in range(N): 
        res.append(random.randint(start, end)) 
    return res
start = 1
end = 23
L = Rand(start, end, N)
print(L)


#while len(L) > 1:
n = randint(0,N-1)
m = randint(0,N-2)
print(n)
a = L[n]
print(L[n])
del L[n]
print(L)
print(m)
a = L[m]
print(L[m])
del L[m]
print(L)


    box = ['+', '-', '*', '/']
    x = randint(0, 3)
    if x == 0:
        outcome = a + b
    elif x == 1:
        outcome = a - b
    elif x == 2:
        outcome = a*b
    else:
        outcome = a/b
        
print(do(a,b))