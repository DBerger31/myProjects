#! usr/bin/python3.7

from selenium import webdriver

browser = webdriver.Chrome()
#browser.get('https://inventwithpython.com')

# looks for image element by a class\
'''
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
'''

#clicks a link on a website
'''
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()
'''

browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('bigboy223')
passElem = browser.find_element_by_id('user_pass')
passElem.send_keys('popofdpofsd')
passElem.submit()