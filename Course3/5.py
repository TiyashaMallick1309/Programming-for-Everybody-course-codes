import urllib.request
import urllib.parse
import urllib.error
f = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
c = {}
for line in f:
    print(line.decode().strip())
    w = line.decode().split()
    for i in w:
        c[i] = c.get(i, 0)+1
print(c)
