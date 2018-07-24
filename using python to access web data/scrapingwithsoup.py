import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

page = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_108127.html").read()
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))