#! usr/bin/python3.7

import openpyxl

wb = openpyxl.Workbook('example.xlsx') # Creates a blank workbook
wb.sheetnames # It starts with one sheet ( >> ['Sheet'] )
sheet = wb.active
sheet.title # >> 'Sheet'
sheet.title = 'Spam Bacon Eggs Sheet' #Changes title

# Warning: Modifications will only be made once you call the save() workbook method

wb.save('example_copy.xlsx')

