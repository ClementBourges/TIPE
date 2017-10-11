# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:39:23 2016

@author: cbourges
"""
import math
import random
import matplotlib.pyplot as plt
import time

def premier(a):
    #Fonction booleenne qui dit si un nombre est premier ou non
    y=[]
    r=int(a**(0.5))+1
    resultat=True
    i=1
    if a==1:
        resultat=False
        #un nombre premier est un nombre qui admet exactement deux
        #diviseurs, 1 n'est pas premier
        #Si 2 ne divise pas a alors aucun nombre pair ne divisera a
    while 2*i+1 <r+1 and resultat==True :
        #Si un nombre a n'est pas premier alors:
        #il existe un diviseur de a dans [2,racine(a)]
        if a%(2*i+1)==0:
            #On ne teste que pour les impairs cf plus haut
            resultat=False
        i=i+1
    return(resultat)


def temps(n):
        t1=time.clock()
        premier(n)
        t2=time.clock()
        return (t2-t1)

def graphe(n):
    """n est le nombre de chiffre à tester"""
    y=[]
    x=[]
    for k in range (5,n):
        moyenne=0
        for i in range(100):
            a=random.randint(10**(k-1),10**(k))
            moyenne+=temps(a)
        y+=[moyenne/100]
        x+=[k]
    print("end1")
    plt.plot(x,y)
    print("end2")
    plt.show()
