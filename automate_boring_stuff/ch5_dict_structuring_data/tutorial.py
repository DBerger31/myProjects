'''
spam = {'color': "blue", 'age': 24}

for v in spam.values():
    print(v)

bag = {'apples': 6, 'tissues': 50}

print('I have ' + str(bag.get('apples', 0)) + ' apples')
print('I have ' + str(bag.get('grenades', 'zero')) +' grenades')

#set default

spam = {'name': 'Daniel', 'age': 24}
if 'color' not in spam:
    spam['color'] = 'black'

for v in spam.values():
    print(v)

spam = {'name': 'Daniel', 'age': 24}
spam.setdefault('color', 'green')

'''

spam = {'color': "blue", 'age': 24}

for v in spam.values():
    print(v)


'''
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

#print(count)

import pprint

pprint.pprint(count)
# ?? print(pprint.pformat('2'))

'''