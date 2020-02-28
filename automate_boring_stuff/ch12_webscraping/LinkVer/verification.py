#! /bin/usr/python3.7
# verification.py - given the URL of a web page , will attempt to download every link on the page
# If there are any broken links it should flag them and print it out

#NOT DONE YET

import selenium, requests, bs4, os

Wiki = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soupWiki = bs4.BeautifulSoup(Wiki.text, 'html.parser')

url = "https://en.wikipedia.org"

# <a> tag defines hyper link, href is the actual hyperlink

for link in soupWiki.select('a[href]'):
    pageUrl = url + str(link.get('href'))
    try:
        requests.get(pageUrl)
        print(pageUrl)
    except Exception as exc:
        print('404 not found')

'''
for link in soupWiki.find_all('a'):
    pageUrl = url + str(link.get('href')) # contains the hyper link
    print("Downloading page %s ..." % pageUrl)
    try:
        res = requests.get(pageUrl)  # request the new URL
        # create a folder called name of url
        pageFile = open(os.path.join(url.strip('cmowz.'), os.path.basename(pageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            pageFile.write(chunk)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
    except requests.exceptions.Timeout:
        continue
'''


