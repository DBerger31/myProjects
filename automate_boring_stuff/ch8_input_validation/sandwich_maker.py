#prompts user what kind of sandwich he wants then
#calculates total of sandwich

import pyinputplus as pyip
import random, time

breadType = pyip.inputMenu(['Whole-Wheat', 'Rye', 'White', 'Brown'], lettered=True)
meatType = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], lettered=True)

cheeseResponse = pyip.inputYesNo('Would you like cheese with that?')
if cheeseResponse == 'yes':
    cheeseType =pyip.inputMenu(['Mutz', 'Swiss', 'Smoked', 'Smelly'], lettered=True)
else:
    cheeseType = 'No cheese'

mayoResponse = pyip.inputYesNo('Would you like mayo with that?')
if mayoResponse == 'yes':
    mayoType = 'mayo'
else:
    mayoType = 'No mayo'

tomResponse = pyip.inputYesNo('Would you like tomato with that?')
if tomResponse == 'yes':
    tomType = 'tomato'
else:
    tomType = 'No tomato'

mustardResponse = pyip.inputYesNo('Would you like mustard with that?')
if mustardResponse == 'yes':
    mustardType = 'mustard'
else:
    mustardType = 'No mustard'

lettuceResponse = pyip.inputYesNo('Would you like lettuce with that?')
if lettuceResponse == 'yes':
    lettuceType = 'lettuce'
else:
   lettuceType = 'No lettuce'

quantity_sandwich = pyip.inputInt('How many sandwiches would you like to purchase? ', min = 1)

sandwich = [breadType, meatType, cheeseType, mayoType, tomType, mustardType, lettuceType]

print()
print('You ordered %s sandwich with ' % (quantity_sandwich))
for stuff in sandwich:
    print(stuff, end=', ')

prices = {'Chicken': 3.50, 'Turkey': 4.00, 'Ham': 4.25, 'Tofu': 3.00, 'Cheese': 1.00, 'Condoments': 0.50}

total = 2.00
for item in sandwich:
    if item in prices.keys():
        total = total + prices[item]
    elif item == 'Mutz' or item == 'Swiss' or item == 'Smoked' or item == 'Smelly':
        total = total + prices['Cheese']
    elif item == 'lettuce' or item == 'mayo' or item == 'mustard' or item == 'tomato':
        total = total + prices['Condoments']

orderTotal = total * quantity_sandwich
print('\nYour total is ', end = ' ')
print(orderTotal, end =' ')
