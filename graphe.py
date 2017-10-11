# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:41:59 2016

@author: Clément
"""
import math
import random
import matplotlib.pyplot as plt
import time
import itertools as IT
import numpy as NP
import fractions

def premier(a):
    #Fonction booleenne qui dit si un nombre est premier ou non
    y=[]
    r=int(a**(0.5))+1
    resultat=True
    i=2
    if a==1:
        return False
    elif a==2:
        return True
        #un nombre premier est un nombre qui admet exactement deux
        #diviseurs, 1 n'est pas premier
        #Si 2 ne divise pas a alors aucun nombre pair ne divisera a
    while i <r+1 and resultat==True :
        #Si un nombre a n'est pas premier alors:
        #il existe un diviseur de a dans [2,racine(a)]
        if a%i==0:
            #On ne teste que pour les impairs cf plus haut
            resultat=False
        i=i+1
    return(resultat)

def témoin(a, n):
    
    # trouver s et d tel que n-1=(2**s)*d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d= d//2
        s += 1       
    if (a**d)%n== 1:
        return False    #a n'est pas témoin de miller
 
    for r in range(0,s):    
        if (a**d)%n== n-1:
            return False    #a n'est pas témoin de miller
        d *= 2 
    return True             # a est témoin de miller

def millerRabin(n,k):
    
    # On élimine le cas où n est pair
    if n==2:
        return True
    elif n %2 == 0:
        return False
 
    # On teste avec k nombre s'ils sont témoins de miller
    for i in range(0, k):
        # on prend un nombre au hasard entre 1 et n-1 
        a = random.randint(1, n-1)
        
        # si ce nombre est témoin de miller
        if témoin(a, n)==True:
            return False    
    # parmi les k nombres testés aucun n'était témoin de miller
    return True

def ordr(r, n):
    for k in IT.count(3):
        if pow(n, k, r) == 1:
            return k
             
def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y
         
def mmultn(a, b, r, n):
    """ Dividing by X^r - 1 is equivalent to shifting the amplitude from
        position k to k - r
        a and b are vectors of length r maximum
        convolve them (equivalent to polynomial mult) and add all amplitudes
        with exp k of r and higher to exp k - r
        After the multiplication all amplitudes are taken %n
    """
    res = NP.zeros(2 * r, dtype=NP.int64)
    res[:len(a)+len(b)-1] = NP.convolve(a, b)
    res = res[:-r] + res[-r:]
    return res % n
 
def powmodn(pn, n, r, m):
    res = [1]
    while n:
        if n & 1:
            res = mmultn(res, pn, r, m)
        n //= 2
        if n:
            pn = mmultn(pn, pn, r, m)
    return res
 
def testan(a, n, r):
    pp = powmodn([a, 1], n, r, n)
    pp[n%r] = (pp[n%r] - 1 ) % n # subtract X^n 
    pp[0] = (pp[0] - a) % n      # subtract a
    return not any(pp)
      
def phi(n):
    return sum(fractions.gcd(i, n) == 1 for i in range(1, n))
         
def aks(n):
    if n==1:
        return False
    for a in range(2, isqrt(n) + 1):
        for b in range(2, n):
            t = a ** b
            if t == n:
                return False
            if t > n:
                break
    logn = math.log(n, 2)
    logn2 = logn ** 2
    for r in IT.count(3):
        if fractions.gcd(r, n) == 1 and ordr(r, n) >= logn2: 
            break
    for a in range(2, r + 1):
        if 1 < fractions.gcd(a, n) < n:
            return False
    if n <= r:
        return True
    for a in range(1, int(math.sqrt(phi(r)) * logn)):
        if not testan(a, n, r):
            return False
    return True
    
        
def temps1(n):
    t1=time.clock()
    millerRabin(n,5)
    t2=time.clock()
    return (t2-t1)

def temps2(n):
    t1=time.clock()
    aks(n)
    t2=time.clock()
    return (t2-t1)
p=[]
for k in range(1,400):
    if premier(k)==True:
        p+=[k]
    """n est le nombre de chiffre à tester"""
    y1=[]
    y2=[]
    x=[]
    f=0
    for f in range(len(p)):
        y1+=[temps1(p[f])]
        y2+=[temps2(p[f])]
        x+=[p[f]]
        
    plt.ylabel("Temps en sec")
    plt.xlabel("Nombres premiers")
    p1=plt.plot(x,y1,"g",label="Miller-Rabin",marker="*")
    p2=plt.plot(x,y2,"b",label="AKS",marker="*")
    plt.legend()
    plt.show()


def grand(n):
        for k in range (1,10000):
            if premier(k):
                return k


def erreur(n):
    """Nombre de composés déclarés comme premiers de parmi les nombres de 1 à n"""
    nbpremiers=0
    for k in range(1,n+1):
        if premier(k):
            nbpremiers+=1
    
    nombrestrouvé=[(-nbpremiers) for i in range(7)]
    for i in range(0,7):
        for k in range(2,n+1):
            if millerRabin(k,i+1):
                nombrestrouvé[i]+=1
    y=[k for k in range(1,8)]
    plt.ylabel("Erreurs")
    plt.xlabel("Témoins de Miller")
    p1=plt.plot(y,nombrestrouvé,"o b",markersize=25)
    print("end2")
    plt.show()
    return nombrestrouvé
    
    







    