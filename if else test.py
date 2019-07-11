# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:28:12 2018

@author: Oluseyi.Oshin
"""
s= 'aaaaaajjjjjmmmdndbga'
n = 0
for var in s:
        if n < 11:
            n += 3
            print (n)
        else :
            if n >= 11:
                print ('the value of n is : ' + str(n))
                n -=8
                
        
        