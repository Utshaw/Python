

#packing unpacking using args and kwargs

# when * is used for calling the function unpacking occurs for the argument
# when * is used in the parameters list packing occurs inside the function

# * for normal arguments ** for keyword arguments

print(*"ABCD") # unpacking


# packing args, this packs all incoming arguments in one tuple
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(1,2,3,4,5,6,7,8,9,10)) # 55



# unpacking kwargs
# smaple function first
def about(name, age , like):
    print('This is {}, {} years old. Likes {}'.format(name, age, like))

about('Utshaw', 21, 'Java')


dictionary = {'name': 'Utshaw', 'age':21, 'like':'Python'}
about(**dictionary) # unpacking kwargs requires **





# packing kwargs

def foo(** kwargs):
    for key, value in kwargs.items():
        print(str(key) + '-->' + str(value))

foo(utshaw = 21, foysal = 22)






