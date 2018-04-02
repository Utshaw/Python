
from random import choice
# while loop

# while condition:
#     statements

# runs over and over again while the condition is True

condition = True

while condition:
    print('Loop executed')
    condition = False


names = []

while len(names) < 3:
    new_name = input('Enter your name: ').strip().capitalize()
    names.append(new_name)

print('Sorry list is full')
print(names)


questions = ['Why the sky is blue', 'How big is earth', 'How far is the sun']

question = choice(questions)

answer = input(question).strip().lower()

while answer != 'just because':
    answer = input('why?').strip().lower()




