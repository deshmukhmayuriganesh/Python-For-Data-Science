# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:41:18 2025

@author: Harish
"""


my_list = [99,88,8,4,3,2]
print(my_list)
#o/p-[99, 88, 8, 4, 3, 2]

# creating a new list of squares of each element
new_list = []
for ele in my_list:
    new_list.append(ele**2)
print(new_list)    
#o/p-[9801, 7744, 64, 16, 9, 4]

# List Comprehension
new_list2 = [ele ** 2 for ele in my_list]
print(new_list2)
#o/p-[9801, 7744, 64, 16, 9, 4]

# Eg of heterogenous list
my_list_2 = [4,True,98.4,[9,6,3],"Python",100]
print(my_list_2)
#o/p-[4, True, 98.4, [9, 6, 3], 'Python', 100]

len(my_list_2)
#o/p-6

list_2d = [[1,2,3], [4,5,6], [7,8,9]]
print(list_2d)
#o/p-[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list_2d[1])
#o/p-[4, 5, 6]

# accessing an element in 2d list
print(list_2d[1][0])
#o/p-4

lst = [4,5,6,3,2,7]
lst.sort()
lst.reverse()
print(lst[1])
#o/p-6

l = [1,4.5,8,9,5,6]
l.sort()
print(l[-2])    
#o/p-8
 