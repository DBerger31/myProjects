#!/usr/bin/python3.7

# Mad Lib Game
# madlib.py - user enters their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

print("Please enter a file name for the mad libbing!")

filename = input()
madlibs = open(filename)

text = madlibs.read()
madlibs.close()

adjective = re.compile(r'ADJECTIVE*')
noun = re.compile(r'NOUN*')
adverb = re.compile(r'ADVERB*')
verb = re.compile(r'VERB*')

#TODO: Fix issue with not being able to replace additional
# occurences of adjectives ,verbs, etc.

for word in text.split():
    if adjective.search(word):
        madword = input("Enter an ADJECTIVE: ")
        text = re.sub(r"ADJECTIVE", madword, text, count = 1)
    elif noun.search(word):
        madword = input("Enter an NOUN: ")
        text = re.sub(r"NOUN", madword, text, count = 1)
    elif adverb.search(word):
        madword = input("Enter an ADVERB: ")
        text = re.sub(r"ADVERB", madword, text, count = 1)
    elif verb.search(word):
        madword = input("Enter an VERB: ")
        text = re.sub(r"VERB", madword, text, count = 1)

print('\n' + text)


filename = "new" + filename
newfile = open(filename, "w+")
newfile.write(text)
newfile.close()

