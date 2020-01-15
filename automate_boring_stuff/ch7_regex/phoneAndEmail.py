#!/usr/bin/python

import re, pyperclip

# create a regex for phone numbers
phoneRegex= re.compile(r'''
# 415-550-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext., x

(((\d\d\d)|(\(\d\d\d\)))?           # area code (optional)
(/s|-)                              # first seperator
\d\d\d                              # 3 digit number
(/s|-)                              # second seperator 
\d\d\d\d                            # 4 digit number
(((ext(\.)?(\s)?) | x)              # extension word part (optional) 
(\d{2,5}))?)                        # extension number part (optional)
''', re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(/w{2,5}).com

[a-zA-Z0-9_.+]+  # name part
@                # symbol
[a-zA-Z0-9_.+]+  # domain name
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for numbers in extractedPhone:
    allPhoneNumbers.append(numbers[0])

# copy the extracted text to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(results)

fh = open('contacts.txt', 'w')
fh.write(pyperclip.paste())

