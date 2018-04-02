# strings are immutable in python


name = 'Farhan Utshaw'

# use triple(3) quotes for multiline string
message = """This is a multiline 
sentence"""
print(message)

# replace string
message = 'Hello World'
message = message.replace('World', 'Universe') # replace 'World' with 'Universe'
print(message)


# concatenation
message = 'Hello'
message += ' World'
print(message)


#count number of words/characters in a string
print(name.count('Utshaw'))  #1


#lower, upper, title, capitalize
print(name.lower())          #farhan utshaw

print(name.upper())          #FARHAN UTSHAW

print(name.title())

print(name.capitalize())     #Farhan utshaw


#islower, isupper, istitle, iscapitalize ?
print(name.islower()) # False
print(name.isupper()) # False
print(name.istitle()) # True
print(name.isalpha()) # False


# isdigit?
no = '123'
print(no.isdigit()) # True



# isalnum
alphanum = 'ThisIsText123'

print(alphanum.isalnum()) # True

nonalphanum = 'This is some'

print(nonalphanum.isalnum()) # False as space is not alpha numeric



# index of sucstring
name = 'Farhan Tanvir Utshaw'
print(name.index('Utshaw')) # 14

#print(name.index('utshaw')) # gives error

print(name.find('utshaw')) # -1 , if the substring has found returns the index else -1



# strip certain character from front and end
# if argument to strip is skipped then it assumes that to be ' '(whitespace)
name = '0000000000Farhan 00 Utshaw0000000000'
print(name.strip('0')) # Farhan 00 Utshaw
print(name.lstrip('0')) # Farhan 00 Utshaw0000000000
print(name.rstrip('0')) # 0000000000Farhan 00 Utshaw


# use strip to remove unnecessary leading and traling whitespaces from input
# name = input('Enter name: ').strip()
# print(len(name))





# strings are iterable in Python



word = 'thisisalonglonglongword'



print(word[word.find('s')])


# slicing variable[start:end:step] starting from start , up to (not including) end
# step will be positive for left to right movement
# step will be negative for right to left movement
print(word[7:19:1])
print(word[-4::1])
print(word[:: -1]) # reverses the order of left to right















