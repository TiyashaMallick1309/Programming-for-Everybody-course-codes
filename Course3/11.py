"""The program will prompt for a URL, 
read the JSON data from that URL using urllib 
and then parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file."""

import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

h = urllib.request.urlopen(
    'http://py4e-data.dr-chuck.net/comments_1567350.json', context=ctx).read()
info = json.loads(h)
c = 0
sum = 0
for item in info['comments']:
    c += 1
    sum += (int(item['count']))
print(c, "\n", sum)
