#! /usr/bin/python3.7

#downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'https://xkcd.com/' # Staring URL
os.makedirs('xkcd', exist_ok = True) #store comics in ./xkcd

while not url.endswith('#'):
    #Downloads page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # HTML CODE in soup var

    ComicElem = soup.select('#comic > img')
    if ComicElem == []: #if there is no comic
        print("Could not find comic image.")
    else:
        try:
            ComicUrl = 'https:' + ComicElem[0].get('src')
            print('Downloading page %s...' % ComicUrl)
            res = requests.get(ComicUrl)
            res.raise_for_status()

# open/creates a a file called the last part of comic url (os.path.basename returns just the last part) in xkcd folder
        except requests.exceptions.MissingSchema:
            #skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue # returns to the begging of the while loop

    imageFile = open(os.path.join('xkcd', os.path.basename(ComicUrl)), 'wb')  # write binary to save it
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
