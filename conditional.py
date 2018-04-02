

logged_in = False

if logged_in:
    print('True!!')
else:
    print('False --> False')

# None evaluates to False
logged_in = None

if logged_in:
    print('True!!')
else:
    print('None --> False')


# 0 evaluates to False
logged_in = 0

if logged_in:
    print('True!!')
else:
    print('0 --> False')


# any number other than 0 evaluates to True
logged_in = -100

if logged_in:
    print('-100 --> True!!')
else:
    print('False')


# empty string, empty list,empty tuple, empty dictionary evaluates to False
logged_in = ''

if logged_in:
    print('True!!')
else:
    print('<Empty String> --> False')


logged_in = {}

if logged_in:
    print('True!!')
else:
    print('<Empty Dictionary> --> False')

