#! /usr/bin/python3.7
# create2020stats.py - should create an excel of per game stats of the 2020 season

import openpyxl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL page we will be scraping
url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'
# this is the HTML form the given url
html = urlopen(url)
# stores source html code in soup
soup = BeautifulSoup(html, 'html.parser')
# use findALL () to get the column header
#soup.findAll('tr', limit=2)

def getHeader():
    headers = [] # list for storing headers
    # use getText() to extract the text we need into a list
    for text in soup.findAll('tr')[0].findAll('th'):
        headers.append(text.getText())
    headers = headers[1:]
    return headers

def getStats():
    rowsOfPlayers = soup.findAll('tr')[1:]
    # creates a 2d list of all the players and their stats
    player_stats = [[stats.getText() for stats in rowsOfPlayers[i].findAll('td')] for i in range(len(rowsOfPlayers))]
    return player_stats

#def CreateWorkbook():
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'PerGame'

for header in getHeader():
    sheet.row_values(1, header)

#wb.save('nba19to20.xlsx')


