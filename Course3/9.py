"""The program will use urllib to read the HTML from the data files below, 
extract the href= values from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, 
repeat the process a number of times, and report the last name you find."""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(
    ' http://py4e-data.dr-chuck.net/known_by_Dexter.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for i in range(6):
    url = tags[17].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
print(tags[17].get('href', None))
