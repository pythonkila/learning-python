# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:40:43 2021

@author: ooshin
"""

# import the random module
# import random
from random import randint

lotto = []

# generate a random number
while len(lotto) < 6:
    x = randint(1, 61)
    
# check if the number already exist in the lotto list, add not if not present
    if x not in lotto:
        lotto.append(x)   
# print message if the generated number is in the list
    else:
        print('Generated number',x,'already exit in the list!')
# print the recommended lotto numbers
print('Your lotto numbers are :', lotto)
    
    