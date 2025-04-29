# -*- coding: utf-8 -*-


'''
Functions
-helps to achieve reusability of code, avoid repetition of code
-more organised and modular code
-Built-in functions
-User-Defined functions

Syntax
-def fun_name (params): statements....
'''
# function definition
def greetings(name):
    print("Good Morning", name)
print(greetings)
#O/P:<function greetings at 0x0000017B7B1BDCA0>

type(greetings)
#o/p-function

print(type(greetings))
#o/p-<class 'function'>

# function calling
greetings("Mayuri")
#o/p-Good Morning Mayuri

greetings("MSD")
#o/p-Good Morning MSD


def add(a,b):
    
    """
    this is a doc string.
    
    return sum of 2 numbers
    
    """
    return (a+b)
# it is not printing, it's a return value
add(5,3)
#o/p:8

# you can recieve return value into a variable
c = add(7,5)
print(c)
#o/p:12

def product(lst):
    s = 1
    for i in lst:
        s *= i
    return s    
sumofP = product([1,2,3,4,5])
print(sumofP)
#o/p:120

def calculator(a,b):
    return(a+b, a-b, a*b, a/b)
calculator(4,2)
#o/p:(6, 2, 8, 2.0)
 