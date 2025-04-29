# -*- coding: utf-8 -*-


'''
Modules
-Modules refer to a file containing a Python code.
-Modules are used to break down large programs into small managable and organized files.

Inbuilt Modules
-os
-math
-random
'''
#Custom modules
import math
dir(math)
['__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'acos',
 'acosh',
 'asin',
 'asinh',
 'atan',
 'atan2',
 'atanh',
 'ceil',
 'comb',
 'copysign',
 'cos',
 'cosh',
 'degrees',
 'dist',
 'e',
 'erf',
 'erfc',
 'exp',
 'expm1',
 'fabs',
 'factorial',
 'floor',
 'fmod',
 'frexp',
 'fsum',
 'gamma',
 'gcd',
 'hypot',
 'inf',
 'isclose',
 'isfinite',
 'isinf',
 'isnan',
 'isqrt',
 'lcm',
 'ldexp',
 'lgamma',
 'log',
 'log10',
 'log1p',
 'log2',
 'modf',
 'nan',
 'nextafter',
 'perm',
 'pi',
 'pow',
 'prod',
 'radians',
 'remainder',
 'sin',
 'sinh',
 'sqrt',
 'tan',
 'tanh',
 'tau',
 'trunc',
 'ulp']
print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.factorial(5)
#O/P:120

math.ceil(9.4)
#O/P:10

math.floor(9.7)
#O/P:9

from math import gcd
gcd(30,16)
#O/P:2

import random
round(random.random()*100 + 10)
#O/P:101

random.random()*50 + 10
#O/P:16.777017525702146

import os
os.getcwd()
#O/P:'C:\\Users\\Python_For_All\\03_Python_Functions_and_Modules'

os.mkdir("newly_created")
os.listdir()
'''
OUTPUT:
  ['.ipynb_checkpoints',
 '01_Function_Introduction.ipynb',
 '02_Default_Arguments_in_Function.ipynb',
 '03_Args_and_Kwargs.ipynb',
 '04_python_modules.ipynb',
 'newly_created']
  '''
# os.remove()
# os.removedirs()
# os.rename()