#! /usr/bin/python3
# bulletPointAdder.py - adds bullet points to the start of each line

import pyperclip

text = pyperclip.paste()

#seperates lines and adds stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines) #since .copy() expects a single string we must join the list lines by \n

pyperclip.copy(text)
