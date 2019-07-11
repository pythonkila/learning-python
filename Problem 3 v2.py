# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:00:41 2018

@author: Oluseyi.Oshin
"""
s = 'xxxntaabcjjjjjddddddaaaameeeeeeabbbbbbbbb'
word = s0 = s1  = store = store0 = ''
for pos in s:
            if pos >= s0:
                word += pos
                s0 = pos
            elif pos < s0:
                store0 = word
                word = ''
                word += pos
                s0= pos
                if len(store0) > len(store):
                        store = store0
            elif pos > s0:
                word += pos
                s0 = pos
            elif pos < s0:
                store0 = word
                word = ''
                word += pos
                s0= pos
                if len(store0) > len(store):
                        store = store0
            elif pos > s0:
                word += pos
                s0 = pos
            elif pos < s0:
                store0 = word
                word = ''
                word += pos
                s0= pos
                if len(store0) > len(store):
                        store = store0
            elif pos > s0:
                word += pos
                s0 = pos
            elif pos < s0:
                store0 = word
                word = ''
                word += pos
                s0= pos
                if len(store0) > len(store):
                        store = store0
            elif pos > s0:
                word += pos
                s0 = pos
            elif pos < s0:
                store0 = word
                word = ''
                word += pos
                s0= pos
                if len(store0) > len(store):
                        store = store0
if len(word) > len(store):
    store = word
                	
print ('Longest substring in alphabetical order is: ' + store)
