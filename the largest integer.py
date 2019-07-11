# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:01:14 2018

@author: Oluseyi.Oshin
"""

def gcdInter (a, b) :
    
    '''
    kbkkjbkjkkjbkljkkjkj
    
    '''
    # My rattle code.
    x = 0
    if a <= b :
        x = a
    elif b <= a:
        x = b
    
    while a%x  or b%x != 0:
        x -=1
        
    return (x)    