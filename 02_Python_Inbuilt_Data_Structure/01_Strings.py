# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:24:17 2025

@author: Harish
"""


'''STRINGS'''
#Strings in python are the sequence of unicode characters.
my_str = "Welcome to the Course"
print(my_str)
#o/p-Welcome to the Course

type(my_str)
#o/p-str

print(type(my_str))
#o/p-<class 'str'>

'''Indexing a StringAccessing one character based on the position'''
print(my_str[0])
print(my_str[1])
#o/p-W
#o/p-e

# Total number characters in a string
len(my_str)
#o/p-21

# Accessing last element of String
print(my_str[len(my_str) - 1])
#o/p-e

my_str[len(my_str) - 1]
#o/p-'e'

'''Negative Indexing
-writting len(my_str) is optional.
-That's how Python give rise to negative indexing'''

my_str[-1] # Last character
#o/p-'e'
my_str[-5] # 5th last character
#o/p-'o'

'''String Slicing
-extracting multiple characters from a string (sub string)
-Syntax: str[start_idx : end_idx + 1}'''
my_str[2:7]
#o/p-'lcome'

print(my_str[:])
#o/p-Welcome to the Course

# All the character expect last 2
print(my_str[:-2])
#o/p-Welcome to the Cour
 