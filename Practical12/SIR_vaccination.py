# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:44:11 2019

@author: 11601
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
    
plt.figure(figsize=(6,4),dpi=150)
plt.title("SIR model with vaccination rate") 
plt.xlabel("time") 
plt.ylabel("number of people")

beta = 0.3
gamma = 0.05

for i in range(0,10):
    sus = 9999 - i*1000
    time = 0
    inf = 1
    rec = 0
    record_inf = [1]
    
    while time <= 999:
        time = time + 1
        new_inf = np.random.choice(range(2),sus,p = [1-beta*(inf/10000),beta*(inf/10000)])
        new_inf = sum(new_inf)
        new_rec = np.random.choice(range(2),inf,p = [1-gamma,gamma])
        new_rec = sum(new_rec)
        sus = sus - new_inf
        inf = inf + new_inf - new_rec
        rec = rec + new_rec
        record_inf.append(inf)
    
    P_inf, = plt.plot(record_inf, color=cm.viridis(i*30))
    P_inf.set_label(str(i*10) + '%')
    
    plt.legend()

plt.savefig("C:/Users/11601/Desktop/IBI/IBI1_2018-19/Practical12/SIR_vaccination",type="png")
plt.show()