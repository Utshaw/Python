# creating dictionary
# dictionary is mutable
# dictionary stores using key->value system
# dictionary keys must be hashable (mostly immutable types such as str, tuples, int, float)
# dict doesn't maintain order

student_utshaw = {"name": 'Utshaw', 'roll': 1505105}

print(student_utshaw)


d = {}

t1 = (1, 2, 3)

t2 = (4, 5, 6)


d[t1] = 100

d[t2] = 55

print(d)

# accessing element try-exception way
try:
    print(student_utshaw['Name'])
except KeyError:
    print('Not Found!!')

# accessing elements - better way returns None by default if key not exists
print(student_utshaw.get('Name', 'Utshaws Not Found')) # Utshaws Not Found (second argument specfies what to return if key not found)

# updating values
student_utshaw.update({'name': 'UTSHAW'}) # {'name': 'UTSHAW', 'roll': 1505105}
print(student_utshaw)

# deleting, popping key-values
st = {'name': 'Selim', 'age': 25}
age = st.pop('age') # returns value of 'age' key
print(st) # {'name': 'Selim'} 'age' is gone
del st['name']


# getting key list
keyList = list(d.keys())
print(keyList)

#getting valueList
valueList = list(d.values())
print(valueList)

# getting item
print(list(d.items())) # [((4, 5, 6), 55), ((1, 2, 3), 100)]


# loop through dictionary
for key, value in d.items():
    print(str(key) + '---->' + str(value) )


# removing an dictionary entry
del  d[t1]

print('After deleting' + str(d))

# nested dict
students = {
    'Utshaw': {'id': 1505105, 'section': 'B'},
    'Foysal': {'id': 159999, 'section': 'A'}
}

print(students)

print(students['Utshaw']['id'], students['Utshaw']['section'])







 









