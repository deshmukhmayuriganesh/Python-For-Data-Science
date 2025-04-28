# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:30:36 2025

@author: Harish
"""


'''Important methods related to strings'''

my_str = "Welcome to the Course"
my_str.lower()
#op-'welcome to the course'

my_str.upper()
#o/p-'WELCOME TO THE COURSE'

my_str.title()
#o/p-'Welcome To The Course'

my_str.find("Course")
#o/p-15

my_str.find("python")
#o/p:-1

my_str.split()
['Welcome', 'to', 'the', 'Course']

'''Few Operations on String'''

"abc " + "pqr"
#o/p-'abc pqr'

"abc" + 1
#TypeError: can only concatenate str (not "int") to str

"abc " + str(1)
#o/p-'abc 1'
"hello " * 4
#o/p-'hello hello hello hello '

# Check if string is palindrome string or not
s = input()
if(s == s[::-1]):
 print("true")
else:
    print("false")
#o/p-abba
#o/p-true

# Count vowels in String
s = input()
count = 0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
     count += 1
if count == 0:
    print("No vowels found")
else:
    print(str(count))
#o/p-mayuri
#o/p-3
 