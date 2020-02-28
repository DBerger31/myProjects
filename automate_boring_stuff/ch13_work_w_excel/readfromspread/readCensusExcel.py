#! /usr/bin/python3.7
# readCensusExcel.py -
'''
1. reads the data
2. Counts the number of census tracts in each country
3. Counts the total population of each county
4. Prints the results
'''

import openpyxl, pprint

data = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = data['Population by Census Tract']
countyData = {}

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # make sure the key for this state exists
    countyData.setdefault(state, {})
    #make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # each row represents one census tract, so inc by 1
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of CountyData to it.

print('Writing results...')

resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')