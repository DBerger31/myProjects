#! /usr/bin/python3.7

#downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'https://xkcd.com/' # Staring URL
os.makedirs('xkcd', exist_ok = True) #store comics in ./xkcd

while not url.endswith('#')
    #Downloads page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser') # HTML CODE in soup var

#TODO: FIND THE URL OF THE COMIC IMAGE
linkElems = soup.select('#bottom > a')
print(linkElems)

#TODO: DOWNLOAD THE IMAGE

#TODO: SAVE THE IMAGE TO ./xkcd

#TODO: GET THE PREV BUTTON'S URL