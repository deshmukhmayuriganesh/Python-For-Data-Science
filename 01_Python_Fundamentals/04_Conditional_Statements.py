# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:39:13 2025

@author: Harish
"""

'''
Control Flow: Conditional Statements
if
else
elif

'''
age = 14

if(age >= 18):
    print("You are eligiblie to vote.")
else:
    print("Grow up first.")
#output: Grow up first

age = 19
if(age >= 18):
    print("You can vote")
elif(age >= 15):
    print("Grow up first")
else:
    print("Go Home Kid")
#output-You can vote
 