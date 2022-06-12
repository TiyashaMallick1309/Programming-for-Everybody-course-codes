import urllib.request
import urllib.parse
import urllib.error
f = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in f:
    print(line.decode().strip())
