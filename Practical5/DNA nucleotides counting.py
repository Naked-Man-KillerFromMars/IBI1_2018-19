## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#""


#counting AGTC
sequence = input('Please give me sequence of DNA:')
sequence = list(sequence)

myDict = {}
for word in sequence:
 if word in myDict:
  myDict[word] += 1
 else:
  myDict[word] = 1
myDict

print(myDict)

#plotting
import matplotlib.pyplot as plt
labels = 'A','T','G','C'
a = int(myDict['A'])
g = int(myDict['G'])
t = int(myDict['T'])
c = int(myDict['C'])
sizes = [a, g, t, c]
explode = (0.05, 0.05, 0.05, 0.05)
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
plt.title('pie of the four DNA nucleotides')
plt.axis('equal')
plt.show()