# LEGB
# Local, Enclosing, Gloabl, Built-in
# This defines the order a variable is assigned to
# First python checks local then enclosing then gloabl then built-in
# Local - defined within the function
# Enclosing -
# Gloabl -
# Built-in =

x = 'global x' # gloabl to this module


def test():
    y = 'local y' # local to test() function
    x = 'local x' # just creates a local 'x' variable that just lives inside this function
    print(y) # local y
    print(x) # local x

test()
print(x) # global x

def globalChanger():

    global x # now this function works with global 'x' instead of local 'x'
    x = 'changed to local x'

globalChanger()
print(x) # output -> 'changed to local x'

# print(y) # NameError as y is not in any LEGB scope

# overriding the builtins
# this min() override built-in min() function
# def min():
#     pass


def outer():  # Enclosing function of inner()
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) # 'inner x'

    inner()
    print(x) # 'outer x'

outer()


def outer2():
    x = 'outer x'

    def inner2():
        nonlocal x # local variable of enclosing function
        x = 'inner x'
        print(x)  # 'inner x'

    inner2()
    print(x)  # 'inner x'

outer2()