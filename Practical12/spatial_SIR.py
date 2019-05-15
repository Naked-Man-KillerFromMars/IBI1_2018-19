# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:58:41 2019

@author: 11601
"""

import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))

outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]= 1

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

beta = 0.3
gamma = 0.05
time = 1

while time <= 99:    
    infIndex = np.where(population == 1)
    for i in range(len(infIndex[0])):
        x = infIndex[0][i]
        y = infIndex[1][i]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
        for xN in range(x-1,x+2):
            for yN in range(y-1,y+2):
                if (xN,yN) != (x,y) and xN != -1 and yN != -1 and xN != 100 and yN != 100:
                    if population[xN,yN] == 0:
                        population[xN,yN]=np.random.choice(range(2),1,p=[1-beta,beta])
    time = time + 1
    if time == 10 or time == 50 or time == 100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')

