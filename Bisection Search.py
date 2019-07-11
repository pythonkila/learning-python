# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:20:14 2018

@author: Oluseyi.Oshin
"""

"""  
#Used for a -ve cube value.

x = -27
dif = 0.1
low = 1
high = x
Guess_count = 0
ans = (high + low)/2

while abs(ans**3 - x) >= dif:
    print ('Low = ' + str(low) + ' ,  High = ' + str(high) + ' , Ans = ' + str(ans))
    if ans**3 > x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    Guess_count +=1
print ('Guess count is : ' + str(Guess_count))
print (str(ans) + ' is close to the  cube root of ' + str(x ))

"""

# Used for +ve value.
x = 9
dif = 0.01
low = 0
high = x
Guess_count = 0
ans = (high + low)/2

while abs(ans**2 - x) >= dif:
    print ('Low = ' + str(low) + ' ,  High = ' + str(high) + ' , Ans = ' + str(ans))
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    Guess_count +=1
print ('Guess count is : ' + str(Guess_count))
print (str(ans) + ' is close to the  cube root of ' + str(x ))
