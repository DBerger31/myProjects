#! /usr/bin/python3.7

import bs4, requests

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.espn.com/fantasy/basketball/')

browser.implicitly_wait(10)

element = browser.find_element_by_xpath("//*[@id='global-user-trigger'']")
'''
url = requests.get('https://fantasy.espn.com/basketball/boxscore?leagueId=33123&matchupPeriodId=16&scoringPeriodId=105&seasonId=2020&teamId=8')

res = requests.get(url)
res.raise_for_status()
'''