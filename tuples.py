
# tuples -> iterable data type
# immutable


t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 is t2) # False t1 , t2 are not same/identical object

print(t1 == t2) # True as both of them are equal (identical value)

my_tuples = (1, 2, 3)

print(isinstance(my_tuples, tuple)) # True



my_tuples2 = my_tuples

print(my_tuples2 is my_tuples) # True my_tuples and my_tuples2 are now pointing to the same object

my_tuples2 = (4, 5, 6)


print(my_tuples2 is my_tuples) # False as Tuples is immutable now my_tuples & my_tuples2 are different


print('--------------------------------------------------------------')

#creating tuple from other iterable interfaces

l = [1, 2, 300] # list is iterable

new_tuple = tuple(l)
print(new_tuple)

print(isinstance(new_tuple, tuple)) # True


my_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # str is iterable

print(isinstance(tuple(my_str), tuple)) # True



A, B, C = (100, 200, 300)

print(A) # 100

print(B) # 200

print(C) # 300




