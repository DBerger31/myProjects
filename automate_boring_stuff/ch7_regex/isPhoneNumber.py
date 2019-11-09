

'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 718-555-0112'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

'''

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print('Done, What\'s next?')
print()

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))

areaCode, mainNumber = mo.groups()

print(mainNumber)

print('What if we have parentheses in our text?\n')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')

print(mo.group(1))
print(mo.group(2))

print('\nMatching Multiple groups with the Pipe:\n')

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# If we want to match optional string we use (string here)?

# If we want to match zero or more we use ()*

# If we want to match one or more we use ()+

# For specific repitions use (string){3} --> will match 3 of the thing
# (string)(3,5) --> will match 3 4 or 5 of it

# greedy vs non greedy matching

# findall

# making your own character class and negative character classes

# starts with (r'^startswith')

# ends with (r'endswith$')

# ignore case by adding re.I as second argument to re.compile

# sub method
