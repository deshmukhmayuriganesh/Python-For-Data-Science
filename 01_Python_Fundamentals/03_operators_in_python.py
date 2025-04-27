# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:34:25 2025

@author: Harish
"""

'''Operators'''
#Arithmetic Operators
n1 = 15
n2 = 5
add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
f_div = n1 // n2
exp = n1 ** n2
mod = n1 % n2
print("a + b = ", add)
print("a - b = ", sub)
print("a * b = ", mul)
print("a / b = ", div)
print("a // b = ",f_div)
print("a ** b = ",exp)
print("a % b = ", mod)
'''
output:
a+ b =  20
a - b =  10
a * b =  75
a / b =  3.0
a // b =  3
a ** b =  759375
a % b =  0
'''
#Comparison Operators
print("a > b = ", n1 > n2)
print("a < b = ", n1 < n2)
print("a >= b = ", n1 <= n2)
print("a >= b = ", n1 >= n2)
print("a != b = ", n1 != n2)
'''
output:
a > b =  True
a < b =  False
a >= b =  False
a >= b =  True
a != b =  True
'''

#Logical Operators
print((5 > 7) and (7 < 5))

print((89 > 12) or (54 < 96))

print(not False)
'''
output:
False
True
True
'''

#Bitwise Operators
print(5 & 7)

print(5 | 7)
'''
output
5
7
'''
#Membership (in)
"Good" in "Good Morning"
'''output:True'''
 