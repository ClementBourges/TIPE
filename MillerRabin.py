# -*- coding: utf-8 -*-
"""
Éditeur de Spyder"""

import random

def témoin(a, n):
    
    # trouver s et d tel que n-1=(2**s)*d
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        d= d//2
        s += 1       
    if (a**d)%n== 1:
        return False        #a n'est pas témoin de miller
    
    for r in range(0,s):    
        if (a**d)%n== n-1:
            return False    #a n'est pas témoin de miller
        d *= 2 
    
    return True             # a est témoin de miller

def millerRabin(n,k):
    if n==2:
        return True     
    elif n %2 == 0:         # On élimine le cas où n est pair    
        return False
 
    for i in range(0, k):   # On teste avec k nombre s'ils sont témoins de miller   
        a = random.randint(1, n-1)  # on prend un nombre au hasard entre 1 et n-1
        
        if témoin(a, n)==True: # si ce nombre est témoin de miller
            return False    
    
    return True # parmi les k nombres testés aucun n'était témoin de miller








def premier(a):
    r=int(a**(0.5))+1
    resultat=True
    i=1
    if a==1:
        resultat=False
    elif a==2:
        return True
    while 2*i+1 <r+1 and resultat==True :
        if a%(2*i+1)==0:
            resultat=False
        i=i+1
    return(resultat)





















