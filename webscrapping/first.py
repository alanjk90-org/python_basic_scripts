import urllib2
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
#print soup.prettify()

#print list(soup.children)
print [type(item) for item in list(soup.children)]