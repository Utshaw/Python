
# Function is used for DRY - [Don't repear yourself]

# A block of organized and reusable code

# Here x , y are function parameters & the values we use for calling the function are arguments

def add(x, y):
    return x + y



sum = add(100, 200)

print(type(sum))


# Variable Scope

# Global Scope
# Local Scope

# Functions create local scope but loops and if statements don't'
# Everything inside local scope is accessible from that scope only

if True:
    y = 100
    z = 300
    a = 1*2
    a = 2*3
    a = 5*6
    x = 100

print(x) # possible

a = 10

def f1():
    a = 100
    print(a)


def f2():
    a = 50
    print(a)

f1()
f2()
print(a)

# overriding global value from inside a function
def f3():
    global a
    a = 999
    print(a) # 999


def f4():
    global utshaw # global variable. If exists, then use that otherwise create a new global variable (can be accessed outside of this function) with that name
    utshaw = 7789

f3()
f4()
print(utshaw) # 7789
print(a) # 999



ll = [1, 2, 3]


def f5():
    ll[0] = 99900

f5()

print(ll) # [99900, 2, 3]

# sample function with default parameters
#default values must go to the end

def about(name, age, likes = 'Java'):
    sentence = "Meet {} {} years old. Likes {}".format(name, age, likes)
    return sentence


sen = about('Utshaw', 21, 'Python')
print(sen)

sen = about('Utshaw', 21)
print(sen)


# keyword arguments
def about(name, age, like):
    print('Meet {}. He is {} years old and likes {}'.format(name, age, like))

about(name = 'Utshaw', age = 21, like = 'Python' ) # kwargs
about(age = 21, name = 'Utshaw', like  = 'Python') # same as above


# *args and **kwargs can be used to hold any number of arguments as tuple & dictionary respectively
def tester(*args, **kwargs):
    print(args) # packed in tuple
    print(kwargs) # packed in dictionary


tester(10, 20, 'Utshaw', name = 'FARHAN', id = 1505105) # positional arguments goes to args and keyword arguments goes to kwargs

# lambda expressions
# lambda arguments : expression

power = lambda a, b : a**b

print(power(10, 2)) # 100

