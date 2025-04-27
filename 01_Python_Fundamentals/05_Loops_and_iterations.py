# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:41:34 2025

@author: Harish
"""

'''
Control Flow: Iterations Loop
while loop
for loop
'''
i = 1
while(i <= 20):
    if(i % 2 == 0):
        print(i)
    i = i + 1    
'''
o/p:
2
4
6
8
10
12
14
16
18
20
'''
i = 1
while(i <= 20):
    if(i % 2 == 0):
        print(i, end = ", ")
    i = i + 1    
#o/p- 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 

for ele in range(1,21):
    if(ele % 2 == 0):
        print(ele, end = " ")
#o/p- 2 4 6 8 10 12 14 16 18 20 

for i in range(2,21,2):
    print(i, end = " ")
#o/p-2 4 6 8 10 12 14 16 18 20 

n = 5
for i in range (1,11):
    print(n, "x", i, "=", n*i)
'''
output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''
