#! /usr/bin/python3.7
# mapIt.py - script will use command line arguments otherwise use clipboard if no arguments given
# in order to open the web browser to that specific area
# Usage: ./mapit.py Street, City, State Zip code
# Usage: ./mapit.py

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get the address from the terminal
    address = ' '.join(sys.argv[1:]) # First arg is mapit.py, then join everything after as the address
    print(address)
# TODO: Get the address from the clipboard

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)