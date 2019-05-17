# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:24:16 2019

@author: 11601
"""
#reverse split and sort a string 
lyrics = input('Please give me a string of words: ')

M = lyrics[:]

M = M[-1::-1]

splitM = M.split(' ')

splitM.sort()
splitM.reverse()

print(splitM)
