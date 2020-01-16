#!/usr/bin/python3.7

# Mad Lib Game
# madlib.py - user enters their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

print("Please enter a file name for the mad libbing!")

filename = input()
madlibs = open(filename)

text = madlibs.read()
madlibs.close()

#TODO: print the text and look for what to replace (prompt user to pick words for replacement)