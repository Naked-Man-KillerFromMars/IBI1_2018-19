# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:18:49 2019

@author: 11601
"""
#Running a Copasi model from within Python
import os
os.system('C:/Program Files/copasi.org/COPASI 4.24.197/bin/CopasiSE.exe predator-pre.cps')
#Reading and plotting simulation results
import numpy as np
import re
import matplotlib.pyplot as plt

with open('modelResults.csv', 'r') as xfile:
    xfile = xfile.readlines()
L = []
names = []
n = 0
for line in xfile:
    if n == 0:
        names = re.split(r',+',line)
        n = 1
    else:
        l = re.split(r',+',line)
        del(l[0])
        L.append(l)
result = np.array(L)
result = result.astype(np.float)

pred, = plt.plot(result[:,0])
prey, = plt.plot(result[:,1])
pred.set_label('Predator (b=0.02 d=0.4)')
prey.set_label('Prey (b=0.1 d=0.02)')

plt.title("Time course") 
plt.xlabel("time") 
plt.ylabel("population size")

plt.legend()
plt.show()

plt.plot(result[:,0],result[:,1])
plt.xlabel('Predator')
plt.ylabel('Prey')
plt.title('Limit cycle')
plt.show()