# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:52:36 2019

@author: Acer
"""

from matplotlib import pyplot as plt

Total = 300
origS = 280
origI = 20
origR = 0
a = 0.03
p = 0.07
b = 0.3
days = 60
day = [x for x in range(days)]

S = [0] * days
I = [0] * days
R = [0] * days
S[0] = origS
I[0] = origI
R[0] = origR  
    
def trans(cS,cI,cR):
    dS = int(-a * p * cS * cI)
    dR = int(b * cI)
    dI = -dS - dR
    return cS + dS, cI + dI, cR + dR

for i in range(1,days):
    S[i], I[i], R[i] = trans(S[i-1],I[i-1],R[i-1])

plt.figure(figsize = (5, 4))
plt.plot(day, S, label = 'S prob. = ' + str(p))
plt.plot(day, I, label = 'I', color='black')
plt.plot(day, R, label = 'R', color='red')
plt.ylabel('S, I, R')
plt.xlabel('Days')
plt.legend()
plt.show()