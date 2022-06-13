"""The program will use urllib to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file."""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum = 0
html = urllib.request.urlopen(
    ' http://py4e-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
print('Sum:', sum)
