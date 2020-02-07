#! /usr/bin/python3.7

import bs4, requests, webbrowser, sys, google

try:
    from googlesearch import search
except ImportError:
    print("No module named google found")

keyword = sys.argv[1]

for link in search(keyword, tld ='co.in', num = 5, stop = 1, pause = 2):
    print(link)