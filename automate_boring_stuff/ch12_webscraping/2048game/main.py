#! /usr/bin/python3.7
# main.py - Will continuously play 2048 game, if game over then it retries..


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
browser = webdriver.Chrome()
browser.get('https://play2048.co/')


def playGame():
    browser.find_element_by_css_selector('body').send_keys(Keys.ARROW_UP)
    time.sleep(0.1)
    browser.find_element_by_css_selector('body').send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.1)
    browser.find_element_by_css_selector('body').send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
    browser.find_element_by_css_selector('body').send_keys(Keys.ARROW_LEFT)
    time.sleep(0.1)

GameOn = True
while GameOn:
    playGame()
    try:
        browser.find_element_by_xpath("//div[@class='game-message game-over']")
        GameOn = False
        if not(GameOn):
            retry = browser.find_element_by_xpath("/html/body/div[3]/div[4]/div[1]/div/a[2]")
            retry.click()
            GameOn = True
    except NoSuchElementException:
        GameOn = True


