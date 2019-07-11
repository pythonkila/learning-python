# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:31:12 2018

@author: Oluseyi.Oshin
"""

def isin (char, aStr):
    
    '''
    find char in aStr 
    '''
    x = len(aStr)
    if x <= 1 :
        return False
    y = int(x/2)
    
    if char == aStr [y]:
        return char == aStr [y]
    elif char > aStr [y] :
        return isin(char, aStr[y:])
    elif char < aStr[y]:
        return isin(char, aStr[:y])
    
    
             
    