# -*- coding: utf-8 -*-
'''
arbitary arguments: it can receive, any number of arguments
'''

def random_fun(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i**2)
random_fun(15,5,3,9,6)
'''
OUTPUT:
(15, 5, 3, 9, 6)
<class 'tuple'>
225
25
9
81
36
'''
#keyword arguments: it also takes any number of arguments and stores in form of dictionary. Parameter name is mandatory while calling function

def introduction(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for k,v in kwargs.items():
        print(k, ":", v)
introduction(name = "Mayuri", age = 19, hobby=['coding','cricket'],nationality='Indian')
'''
OUTPUT:
{'name': 'Mayuri', 'age': 19, 'hobby': ['coding', 'cricket'], 'nationality': 'Indian'}
<class 'dict'>
name : Mayuri
age : 19
hobby : ['coding', 'cricket']
nationality : Indian
'''
introduction(name = "Sundar", age = 40, company = "Google")
'''
OUTPUT:
{'name': 'Sundar', 'age': 40, 'company': 'Google'}
<class 'dict'>
name : Sundar
age : 40
company : Google
'''
 