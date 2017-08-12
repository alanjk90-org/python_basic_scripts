import requests
from bs4 import BeautifulSoup

with requests.Session() as c:
	url = 'https://www.linkedin.com/uas/login'
	notification_link = 'https://www.linkedin.com/notifications/'
	email = 'chijumelveettil@gmail.com'
	password = '9567076828'
	c.get(url)
	csrftoken=c.cookies['csrftoken']
	login_data = dict(csrfmiddlewaretoken=csrftoken, username=email, password=password)
	c.post(url, data=login_data)
	page = c.get(notification_link)
	print page.content




 
 