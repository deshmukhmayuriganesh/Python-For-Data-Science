# -*- coding: utf-8 -*-
'''
Built In Function
print()
abs()
round()
Aggregation Functions: sum(), max(), min()
filter()
map()
'''
abs(-4.5)
#O/P:4.5

round(5.6786,2)
#O/P:5.68

round(5.96564782,1)
#O/P:6.0

lst = [1,2,3,4,5]
sum(lst)
#O/P:15

max(lst)
#O/P:5

min(lst)
#O/P:1

'''Map'''

def add_one(x):
    return x + 1
add_one(15)
#O/P:16

new_lst = []
for i in lst:
    new_lst.append(i + 1)
print(new_lst)    
#O/P:[2, 3, 4, 5, 6]

map_ele = map(add_one, lst)
print(map_ele)
#O/P:<map object at 0x000001BD9430D370>

print(list(map_ele))
#O/P:[2, 3, 4, 5, 6]

'''Filter'''

def is_even(x):
    return x % 2 == 0
is_even(5)
#O/P:False

filter_ele = filter(is_even, lst)
print(filter_ele)
#O/P:<filter object at 0x000001BD9430D340>

print(list(filter_ele))
#O/P:[2, 4]
 