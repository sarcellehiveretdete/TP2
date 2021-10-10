# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:24:04 2021

@author: Siméon
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Task 1
"""
def f_random_number():
    x=np.random.randint(0,10**x)
    print(x/10**x)
 f_random_number(10)   
 """
def f_random_number(x):
   liste=[np.random.uniform(0,1) for i in range (x)]
   return (liste)
#Task 2
Liste1=f_random_number(10)

def graph (liste):
    X1=[0 for i in range (len(liste))]
    X2=[0 for i in range (len(liste))]
    Y1=[0 for i in range (len(liste))]
    Y2=[0 for i in range (len(liste))]
    for i in range (len(liste)):
        X1[i]=i+1
        Y1[i]=liste[i]
        X2[i]=liste[i]
    for i in range (len(liste)-1):
        Y2[i]=liste[i+1]
#plt.scatter=point, plt.plot= courbe
    plt.subplot (1,3,1)            
    plt.scatter(X1,Y1)
    plt.subplot (1,3,2)
    plt.scatter(X2,Y2)
    plt.subplot (1,3,3)
    plt.hist(liste)
    plt.show()

print (graph(Liste1))
#Task 3
"""
if __name__=="__main__":
    N=int(sys.argv[1])
    x=rand_seq(N)
    pretty_plot(x)
"""
# Task 4 // PAs satisfait afficher une "supperposition de graphes"="somme de graphes"

def time (x,a):
    liste=[]
    for i in range (x):
        liste+= f_random_number(a)
    return(graph (liste))
    
print (time(100,10)) 