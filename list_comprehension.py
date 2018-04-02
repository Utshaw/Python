
# list comprehension

even_numbers = [x for x in range(1, 101, 1) if x % 2 == 0]

print(even_numbers)


odd_numbers = [x for x in range(1,101, 1) if x % 2 == 1]
print(odd_numbers)

words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)


l_n_pair = [(letter, number) for letter in 'abcd' for number in range(4)]

print(l_n_pair)


# dictionary comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heros)}

print(my_dict)

# set comprehension

my_set = [n for n in range(10)]

print(my_set)







