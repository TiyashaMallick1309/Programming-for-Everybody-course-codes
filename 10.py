"""Below, we’ve provided a for loop that sums all the elements of list1. 
Write code that accomplishes the same task, but instead uses a while loop.
Assign the accumulator variable to the name accum."""

list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem
accum=0
i=0
while i<len(list1):
    accum+=list1[i]
    i+=1
