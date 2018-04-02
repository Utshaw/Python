
# behind the scene 'is' operator is same as id(a) == id(b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # value of a & b is same
print(a is b) # a & b are not the same object

# a & b are two different objects in memory
print(id(a))
print(id(b))

