

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(somelist):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for word in tableData[i]:
            if colWidths[i] < len(word):git
                colWidths[i] = len(word)
    for x in range(len(tableData)):
        for y in range(len(tableData[x])):
            ''.join(tableData[x])
            print(tableData[x])

printTable(tableData)



'''
our code will first have to find the longest string in each of the inner lists
so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number of inner lists in tableData.
That way, colWidths[0] can store the width of the longest string in tableData[0], colWidths[1]
can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method.
'''