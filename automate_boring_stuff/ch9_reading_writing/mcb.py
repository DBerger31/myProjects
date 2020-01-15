# Updatable Multi-clipboard project
# mcb.py - Saves and loads pieces of text to the clipboard
# Usage:
# py.exe mcb.py save <keyword> - Saves clipboard to keyword
# py.exe mcb.py <keyword> - Loads keyword to clipboard
# py.exe mcb.py list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content

#TODO: List keywords and load content