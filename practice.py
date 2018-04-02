


word = input().strip().lower()

counter = 0

for letter in word:
    if letter in 'aeiou':
        break
    counter += 1

print(word[counter:] + word[:counter].capitalize() + 'ay')
