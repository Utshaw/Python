
# https://www.youtube.com/watch?v=K8L6KVGG-7o

import re

import time

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
bat
utshaw105@gmail.com
'''

sentence = 'Start a sentence and then bring it to an end'

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)', re.IGNORECASE) # ignorecase for same pattern
matches = pattern.finditer(urls)

# back reference - reference captured groups shorthand for accessing for group indices

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)


print('------------------------------------------------------------------------------------------------')


for match in matches:
    print(match.group(0)) # finding a group using group() method using index as parameter

print('------------------------------------------------------------------------------------------------')

