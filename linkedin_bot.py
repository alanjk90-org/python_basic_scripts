import os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def viewBot(browser):
	notifications = []
	link = 'https://www.linkedin.com/notifications/'
	page = BeautifulSoup(link)
	print(page.prettify())


def Main():
	email = 'chijumelveettil@gmail.com'
	password = '9567076828'

	browser = webdriver.Firefox()
	browser.get('https://www.linkedin.com/uas/login')

	emailElement = browser.find_element_by_id('session_key-login')
	emailElement.send_keys(email)
	passElement = browser.find_element_by_id('session_password-login')
	passElement.send_keys(password)
	passElement.submit()

	os.system('clear')
	print "[+] Success! Logged In, Bot Starting!"
	viewBot(browser)
	browser.close()

if __name__ == "__main__":
	Main() 