alphabet = []
for i in range(26):
    alphabet.append(chr(97 + i))

input_keys = input('Please press any keys in keyboard:')

for letter in input_keys:
    if letter in input_keys:
        alphabet.remove(letter)

print('No pressed letters are',alphabet)