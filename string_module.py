

import string


a = 'cemvhny'
b = '       '


x = str.maketrans('','', a)

s = 'The cow jumped over the moon'

print(a)
print(b)
print()
print(s.translate(x))




