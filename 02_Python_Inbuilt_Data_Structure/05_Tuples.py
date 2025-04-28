# -*- coding: utf-8 -*-

'''
TUPLES
-Similar to lists (read only)
-Ordered, collection of items
-indexable
-immutable
'''
t = (8, 9, "Hello", 88)
print(t)
#o/p-(8, 9, 'Hello', 88)
type(t)
#o/p-tuple
print(t[0])
#o/p-8
print(t[-1])
#o/p-88
print(t[:-1])
#o/p-(8, 9, 'Hello')
t[0] = 1 # This is not possible because of immutability
print(t)

for ele in t:
    print(ele)
'''o/p:
8
9
Hello
88
'''
'''Tuple are faster than List'''
 