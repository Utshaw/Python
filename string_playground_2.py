# curly braces are replaced by arguments in format method.

person = {'name': 'Utshaw', 'roll': 1505105}

print('I am {} & my roll is {}'.format(person['name'], person['roll']))

print('I am {0[name]} & my roll is {0[roll]}'.format(person))

my_list = ['Utshaw', 1505105]

print('I am {0[0]} & my roll is {0[1]}'.format(my_list))


print('I am {name} & my roll is {roll}'.format(name = 'Utshaw', roll = 1505105))



class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

p1 = Person('Utshaw', 1505105)
print('I am {0.name} & my roll is {0.roll}'.format(p1))


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}<{0}>'.format(tag, text)

print(sentence) # <h1>This is a headline<h1>


# left padded with 3 digits
for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = 'My pi is {:.3f}'.format(pi) # rounding upto 3 decimal places
print(sentence) # 3.142

# using comma to represent large numbers
sentence = '1 MB is equal to {:,} bytes'.format(1024**2)
print(sentence)

# using comma to represent large numbers & upto 2 decimal places
sentence = '1 MB is equal to {:,.2f} bytes'.format(1024**2)
print(sentence)



