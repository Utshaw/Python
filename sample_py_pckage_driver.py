
# sample python package importing
# importing the full module or any member(variable, function) of that module will call all of the print function of that module too
# when we import a module it checks for that module in multiple location that are in sys.path

import sample_py_package.demo as d

from sample_py_package.subpackage.demo import printHelloWorld as subPrinter

import sys

d.printHelloWorld()

subPrinter()


print(sys.path) # python looks for module in these paths when we import a module


