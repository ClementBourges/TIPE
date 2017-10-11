# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:48:34 2016

@author: Clément
"""

import math
import itertools as IT
import numpy as NP
import fractions
 
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
    
