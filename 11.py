"""Write a function called stop_at_four that iterates through a list of numbers. 
Using a while loop, append each number to a new list until the number 4 appears. 
The function should return the new list."""

def stop_at_four(l):
    lst=[]
    i=0
    while i<len(l):
        if l[i]==4:
            break
        lst+=[l[i]]
        i+=1
    return lst
l=[]
for i in l:
    i=int(input())
stop_at_four(l)
