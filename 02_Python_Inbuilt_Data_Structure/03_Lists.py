# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:36:17 2025

@author: Harish
"""

'''
Lists
-ordered/sequence collection of elements
-indexable
-mutable
-can store heterogenous elements
'''
my_list = [6,3,2,8,4]
print(my_list)
#o/p-[6, 3, 2, 8, 4]

type(my_list)
#o/p-list

'''Indexing/Slicing of List works same way as Strings'''

print(my_list[0])
#o/p-6

print(my_list[-1])
#o/p-4

print(my_list[1:-1]) # list slicing
#o/p-[3, 2, 8]
# because of mutable property

my_list[0] = 99
print(my_list)
#o/p-[99, 3, 2, 8, 4]

'''Some important methods for lists'''
# adds the given element at the end of the list
my_list.append(33)
print(my_list)
#o/p-[99, 3, 2, 8, 4, 33]

my_list.insert(1,88)
print(my_list)
#o/p-[6, 88, 3, 2, 8, 4]

# delete the last element.
# pop function can also take index if you want to delete specific index.
my_list.pop()
#o/p-4

print(my_list)
#o/p-[8, 2, 3, 88, 6]

my_list.reverse()
print(my_list)
#o/p-[6, 88, 3, 2, 8]

my_list.sort()
print(my_list)
#o/p-[2, 3, 6, 8, 88]

# sorts in descending order
my_list.sort(reverse = True)
print(my_list)
#o/p-[88, 8, 6, 3, 2]

# in operator
8 in my_list
#o/p-True

# iterating over elements of list and taking their squares
for ele in my_list:
    print(ele**2)
'''o/p:
7744
64
36
9
4'''
 