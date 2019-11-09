#! python 3
#NumberAndEmail.py - Finds the phone numbers and email addresses on the clipboard

import pyperclip, re

text = pyperclip.paste()

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                    #area code
(\s|-|\.)?                              #seperator
(\d{3})                                 #first 3 digits
(\s|-|\.)?                              #seperator
(\d{4})                                 #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?          #extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
(\S)+       
(@)
([a-zA-Z0-9.-])+
(\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

matches = []    #creates an empty list for the matches

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if (len(matches) > 0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone Numbers or emails found')


