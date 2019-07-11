# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:20:15 2018

@author: Oluseyi.Oshin
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    count = exp
    x = 1
    while count > 0 :
       x *= base
       count -= 1    
    return x