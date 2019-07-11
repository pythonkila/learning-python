# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:54:58 2018

@author: Oluseyi.Oshin
"""

def gcdrecur(a, b):
    '''
    This is a recursive calculation of the highest common denominator
    '''
   
    if b == 0 :
        return a
    else :
        return gcdrecur (b, a%b )
    
        