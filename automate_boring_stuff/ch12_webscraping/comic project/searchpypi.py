#! /usr/bin/python3.7
# searchpypi.py - gets search keywords from command line args, retrieves the search results page and opens a browser tab for each result

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results links
soup = bs4.BeautifulSoup(res.text,'html.parser')
# Open a browser tab for each result
linkElems = soup.select('r')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
