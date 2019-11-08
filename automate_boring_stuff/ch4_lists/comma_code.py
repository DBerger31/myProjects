
#list of values

spam = ['apples', 'bananas', 'cherries', 'donuts']

def ConvertList(somelist):
    for i in range(len(somelist)):
        if i == len(somelist) - 1:
            print (' and ' + somelist[i].capitalize(), end='')
        else:
            print (somelist[i].capitalize() + ', ', end='')


ConvertList(spam)