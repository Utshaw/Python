# list is mutable
# Create list and iterate

l = [[1, 2, 3], 99, 'Utshaw']


for elem in l:
    if isinstance(elem, list):
        print(elem)
    else:
        print(elem)

# append vs extend
first_list = [1,2,3,4,5]
second_list = [6,7]
first_list.extend(second_list) # extend extends the list by appending second list's elements
print(first_list) # [1, 2, 3, 4, 5, 6, 7]
first_list.append(second_list)  # 'append' appends more element @ at the end of the list doesn't care about what the second element is
print(first_list) # [1, 2, 3, 4, 5, 6, 7, [6, 7]]



# reverse list
first_list.pop() # popping the inner list now [1, 2, 3, 4, 5, 6, 7]
first_list.reverse() # after reversing -->  [7, 6, 5, 4, 3, 2, 1]
print(first_list) # [7, 6, 5, 4, 3, 2, 1]

# printing in reverse order
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print(my_list[-2:1:-1]) # negative step size means reverse order iterating output-> '[8, 7, 6, 5, 4, 3, 2]'

# sort a list (ascending order/descending order)
first_list.sort() # after sorting --> [1, 2, 3, 4, 5, 6, 7]
print(first_list)
first_list.sort(reverse=True) # in decencing order after descending sort --> [7, 6, 5, 4, 3, 2, 1]
print(first_list)


# sort without altering the original one
altered_list = sorted(first_list) # here first_list doesn't get changed
print(altered_list) # [1, 2, 3, 4, 5, 6, 7]
print(first_list) # [7, 6, 5, 4, 3, 2, 1]


# min, max, sum of a list
print(min(first_list)) # 1
print(max(first_list)) # 7
print(sum(first_list)) # 28


# index of an element using index() method [ValueError occurs for not matching value]
try:
    first_list.index(899987)
except ValueError:
    print('Not Found in the list')

# search for the element in the list returns True/ False
print(900 in first_list) # False


# join() method for string version of the list containing strings
string_list = ['Physics', 'Math', 'Chemistry']
joined_list = '-'.join(string_list)
print(joined_list) # Physics-Math-Chemistry




# remove , pop ,  add element to a list
l = [1, 2, 3, 4, 5]
del l[0:2] # deleting using index
l.remove(5) # delete using element here last element will be deleted
print(str(l)) # [3, 4]
popped_item = l.pop() # last element will be popped here returns 4
print(l) # [3]



l = l + [100]
l.append(100) # adding 100 at the end of the list

l = l + ["BCD"]
l = l + list("BCD") # each of the characters will be converted to list element

print(l)

#inserting to an index

A = [1, 2, 3, 4, 5, 6, 7]
A.insert(2, 100)
print(A) # [1, 2, 100, 3, 4, 5, 6, 7]


# using enumerate()
arr = [2, 4, 6, 8, 10]
for i , element in enumerate(arr):
    print(i, element) # is is an index for each of the element


# note: append, insert method returns empty value don't assign list.append to list the list will be NoneType
# list is mutable. No need of assigning



known_users = ['Salman', 'Sadman', 'Sakib', 'Shakhawat', 'Samsul']

while True:
    print('This is security space.')
    name = input('What is your name? ').strip().capitalize()

    if name in known_users:
        print('Hello {}'.format(name))
        remove = input('Would you want to be removed? (y/n)').strip().lower()

        if remove == 'y':
            known_users.remove(name) # remove the first occurrence of name from known_users



    else:
        print("""I don't think I have met you yet{}""".format(name))
        add_me = input('Do you want to be added? (y/n)').strip().lower()
        if add_me == 'y':
            known_users.append(name)



