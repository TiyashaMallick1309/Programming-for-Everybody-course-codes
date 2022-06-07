import re
t = open("regex_sum_1567345.txt")
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
