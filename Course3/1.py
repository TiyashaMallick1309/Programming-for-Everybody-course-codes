"""You will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers."""

import re
t = open("regex_sum_42.txt")
l = []
sum = 0
for line in t:
    line = line.rstrip()
    s = re.findall('[0-9]+', line)
    if len(s) > 0:
        l.append(s)
for i in l:
    for j in i:
        sum += int(j)
print(sum)
