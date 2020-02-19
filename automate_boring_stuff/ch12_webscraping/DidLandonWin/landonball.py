#! /usr/bin/python3.7

import bs4, requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('https://www.espn.com/fantasy/basketball/')

browser.implicitly_wait(10)

hoverElem = browser.find_element_by_xpath("/html/body/div[6]/div[2]/header/div[2]/ul/li[2]/a")
hoverElem.click()
loginElem = browser.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/ul[1]/li[5]/a")
loginElem.click()

userElemWait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/section/section/form/section/div[1]/div/label/span[2]/input")))
userElem = browser.find_element_by_xpath("/html/body/div/div/div/section/section/form/section/div[1]/div/label/span[2]/input")
userElem.send_keys("username")
time.sleep(1)
passwElem = browser.find_element_by_xpath("/html/body/div/div/div/section/section/form/section/div[2]/div/label/span[2]/input")
passwElem.send_keys("passw")
'''
url = requests.get('https://fantasy.espn.com/basketball/boxscore?leagueId=33123&matchupPeriodId=16&scoringPeriodId=105&seasonId=2020&teamId=8')

res = requests.get(url)
res.raise_for_status()
'''
