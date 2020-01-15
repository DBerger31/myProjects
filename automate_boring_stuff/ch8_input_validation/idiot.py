# just an annoying file that requests for input

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

