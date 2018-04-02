########################################################################################

# For Loop

r = range(1, 100) # range iterable

print(type(r))


for number in range(1, 10):
    print(number)


for letter in 'ABCDEF':
    print(letter)

for element in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(element)


for element in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(element)

d = {'name': 'Utshaw', 'id': 1505105, 'location': 'Bangladesh'}

for key in d:
    print(key + '-->' + str(d[key]))


for key in d.keys():
    print(d[key])


my_str = 'Hello Village'

vowels = 0

for letter in my_str:
    if letter.lower() in 'aeiou':
        vowels += 1

print('Total ' + str(vowels) + ' vowels & ' + str(len(my_str) - vowels) + ' consonants')


