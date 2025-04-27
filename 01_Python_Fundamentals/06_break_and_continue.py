# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 22:47:13 2025

@author: Harish
"""


for i in range(1,10):
    if(i == 5):
        break
    print(i)    
'''o/p:
1
2
3
4
'''

for i in range(1,10):
    if(i == 5):
        continue
    print(i)    
'''o/p:
1
2
3
4
6
7
8
9
'''

# Faulty Calculator - - >
a = int(input())
b = int(input())
o = input("Enter operator :")
if(o == '+'):
    if(a == 56 and b == 9):
        print(a,"+",b,"=",77)
    else:
        print(a,"+",b,"=",a+b)
elif(o == '-'):
    print(a,"-",b,"=",a-b)
elif(o == '*'):
    if(a == 45 and b == 3):
        print(a,"*",b,"=",555)
    else:
        print(a,"*",b,"=",a*b)
elif(o == '/'):
    if(a == 56 and b == 6):
        print(a,"/",b,"=",4)
    else:
        print(a,"/",b,"=",a/b)
else:
    print("Invalid operator...")
'''o/p:
75
75
Enter operator :+
75 + 75 = 150
'''