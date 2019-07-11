# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:44:26 2018

@author: Oluseyi.Oshin
"""

high = 100
low = 0
user= ''
guess = int((high + low)/2)

print ('Please think of a number between 0 and 100! ')
while True:
    guess = int((high + low)/2)
    print ('Is your secret number '+ str(guess) + '?')
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")    
    #while user != ('c' and 'l' and 'h'):
    while (user != 'h') and (user != 'l') and (user != 'c'):
        print ('Sorry, I did not understand your input.')
        print ('Is your secret number '+ str(guess) + '?')
        user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if user == 'h':
        high = guess
       # guess = int((high + low)/2)
    elif user == 'l':
        low = guess
       # guess = int((high + low)/2)
    elif user == 'c':
        print ('Game over. Your secret number was: ' + str(guess))
        break
    
    
