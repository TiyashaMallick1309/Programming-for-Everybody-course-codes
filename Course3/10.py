"""The program will prompt for a URL, read the XML data from that URL using urllib and 
then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file."""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(
    'http://py4e-data.dr-chuck.net/comments_1567349.xml', context=ctx).read()
sum = 0
c = 0
s = et.fromstring(html)
l = s.findall('.//count')
for i in l:
    c += 1
    sum += int(i.text)
print(c, "\n", sum)
