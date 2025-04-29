# -*- coding: utf-8 -*
'''
Function Arguments
--Arguments VS Parameters
-default arguments
-arbitary arguments (args)
-keyword arguments (kwargs)
-default parameters: parameters that have some default values. They are optional parameters
'''
def intro(name, nationality = "Indian"):
    print("Hello", name)
    print("I'm", nationality)
intro("Mayuri")
#o/p:Hello Mayuri
#o/p:I'm Indian

intro("Alia", "American")
#o/p:Hello Alia
#o/p:I'm American