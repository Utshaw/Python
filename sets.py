

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Physics', 'Art', 'Design'}

# set doesn't care about order
print(cs_courses) # {'Physics', 'Math', 'History', 'CompSci'}


print(type(cs_courses)) # <class 'set'>

# finding an element
print('Math' in cs_courses) # True


# intersection
print(cs_courses.intersection(art_courses)) # {'Physics', 'Math', 'History'}

# difference
print(cs_courses.difference(art_courses)) # union

# union
print(cs_courses.union(art_courses)) # {'Art', 'Design', 'Physics', 'Math', 'CompSci', 'History'}
