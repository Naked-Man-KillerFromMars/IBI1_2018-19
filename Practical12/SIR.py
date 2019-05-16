
"""
Created on Wed May  8 11:23:03 2019

@author: 11601
"""

import numpy as np
import matplotlib.pyplot as plt

time = 0
sus = 9999
inf = 1
rec = 0
beta = 0.3
gamma = 0.05
record_sus = [9999]
record_inf = [1]
record_rec = [0]

while time <= 999:
    time = time + 1
    new_inf = np.random.choice(range(2),sus,p = [1-beta*(inf/10000),beta*(inf/10000)])
    new_inf = sum(new_inf)
    new_rec = np.random.choice(range(2),inf,p = [1-gamma,gamma])
    new_rec = sum(new_rec)
    sus = sus - new_inf
    inf = inf + new_inf - new_rec
    rec = rec + new_rec
    record_sus.append(sus)
    record_inf.append(inf)
    record_rec.append(rec)
    
plt.figure(figsize=(6,4),dpi=150)
plt.title("SIR model") 
plt.xlabel("time") 
plt.ylabel("number of people") 
P_sus, = plt.plot(record_sus)
P_sus.set_label('susceptible people')
P_inf, = plt.plot(record_inf)
P_inf.set_label('infected people')
P_rec, = plt.plot(record_rec)
P_rec.set_label('recovered people')
plt.legend()

plt.savefig("SIR",type="png")
plt.show()