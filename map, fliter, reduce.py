# map-take a list & function and apply that function to each individual items in the list

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

print(list(map(square, numbers)))


print(list(map(lambda x: x**2, numbers)))

def uppercase(string):
    return string.upper()


values = ['abc', 'def', 'ghi']

print(list(map(uppercase, values)))

# filtering values from list
print(list(filter(lambda x: x > 3, numbers)))







