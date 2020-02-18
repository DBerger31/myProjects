#! /usr/bin/python3.7
# emailer.py - takes an email address and a string of text on the command line and then logs in and emails to the provided email

from selenium import webdriver
import os, bs4

browser = webdriver.Chrome()
browser.get('hh0dHBqWTc4Y2tWa1BBVXY5bXMzIn0sMTU4MTcyMTQxNiwibGsteWVONEFBS3FYNkVERU5QcWVLU1VNeG5YdmhsM2RQZmFJMG9mMG5iWSJd%26nonce%3D90yxWGRfmqjxCsZFjY78ckVkPAUv9ms3%26response_type%3Dcode%26approval_prompt%3Dauto%26client_id%3Ddj0yJmk9N3dWZW1TTWNhY0o0JmQ9WVdrOWMxbDVlVEo2TmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lMA--%26redirect_uri%3Dhttps%253A%252F%252Fwww.aol.com%252Fcallback%26intl%3Dus%26lang%3Den-us%26src%3Dfp-us&src=fp-us&crumb=5OsMIrg4d8p&redirect_uri=https%3A%2F%2Fwww.aol.com%2Fcallback&intl=us&client_id=dj0yJmk9N3dWZW1TTWNhY0o0JmQ9WVdrOWMxbDVlVEo2TmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lMA--&lang=en-us')
email = ''   #input('Enter your email: ')
passw = ''   #input('Enter your pass: ')

emailElem = browser.find_element_by_name('username')
emailElem.send_keys(email)
emailElem.submit()

browser.get('https://login.aol.com/account/challenge/password?done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Frequest_auth%3Fstate%3DWyJJSm1pdUhROVFnQ1NoQ2lGazZuUzBzcDllS3RBMTEzNGVkLXJONFZhUk5RIix7InJlZGlyZWN0X3VyaSI6Imh0dHBzOlwvXC93d3cuYW9sLmNvbSIsImFsbG93ZWRfcXVlcnlfcGFyYW1zIjp7ImludGwiOiJ1cyIsImxhbmciOiJlbi11cyIsInNyYyI6ImZwLXVzIn0sImp0aSI6IjkweXhXR1JmbXFqeENzWkZqWTc4Y2tWa1BBVXY5bXMzIn0sMTU4MTcyMTQxNiwibGsteWVONEFBS3FYNkVERU5QcWVLU1VNeG5YdmhsM2RQZmFJMG9mMG5iWSJd%26nonce%3D90yxWGRfmqjxCsZFjY78ckVkPAUv9ms3%26response_type%3Dcode%26approval_prompt%3Dauto%26client_id%3Ddj0yJmk9N3dWZW1TTWNhY0o0JmQ9WVdrOWMxbDVlVEo2TmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lMA--%26redirect_uri%3Dhttps%253A%252F%252Fwww.aol.com%252Fcallback%26intl%3Dus%26lang%3Den-us%26src%3Dfp-us&src=fp-us&redirect_uri=https%3A%2F%2Fwww.aol.com%2Fcallback&intl=us&client_id=dj0yJmk9N3dWZW1TTWNhY0o0JmQ9WVdrOWMxbDVlVEo2TmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lMA--&lang=en-us&authMechanism=primary&display=login&sessionIndex=QQ--&acrumb=pzSQ8eac')
passwElem = browser.find_element_by_name('password')
passwElem.send_keys(passw)

passwElem.submit()