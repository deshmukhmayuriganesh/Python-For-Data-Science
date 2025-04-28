# -*- coding: utf-8 -*-

'''
Set
-contains only unique elements
-mutable
-unordered
-unindexable
'''
my_set = {9, 7, 7, 1, 8, 9, 7, 5, 1}
# No dupicate elements
print(my_set)
#o/p-{1, 5, 7, 8, 9}

# No matter how many times you add same element, it will be available only once...
my_set.add(99)
print(my_set)
#o/p-{1, 99, 5, 7, 8, 9}

my_set.add(99)
print(my_set)
#o/p-{1, 99, 5, 7, 8, 9}

# remove element from set
my_set.remove(8)
print(my_set)
#o/p-{1, 99, 5, 7, 9}

#Remove Duplicate Numbers from List
lst = [1,5,6,9,8,7,4,6,3,5,1,2,5,6,4,5,2,1,0,2,1,6,3,5,9,7,8]
new_s = set(lst) # set constructor
new_s
#o/p-{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

new_l = list(new_s)
new_l
#o/p-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 