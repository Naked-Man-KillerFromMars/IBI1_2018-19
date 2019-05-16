#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wedn Mar 20 9:11:36 2019

@author: 11601
"""
import re
from fractions import Fraction
#test the input numbers, which must be intergers between 1 and 23
re_numtest = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
i = 1
while i:
    i = 0
    data = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numList = data.split(',')
    for number in numList:
        if re_numtest.match(number): 
            continue
        else: 
            print('The input number must be intergers from 1 to 23')
            i = 1
            break

num = list(map(int,numList)) #use map() to convert every element in numlist to interger and then list it
#to count the recursion times
count = 0 

#define a fuction to calculate 24 and recursion times
#n is how many numbers are input
def dfs(n):
    global count #make it a global variable, not just a function, to calculate the recursion time
    count = count +1
    
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    #keep looping until 24 is calculated in the last step
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            
            num[i] = a+b
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                #floats are not precise
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 
                
            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            #Backtracking  
            num[i] = a
            num[j] = b
    return 0 
#actually run the function to get 24 using input numbers
if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)
