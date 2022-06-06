"""Write a function, length, that takes in a list as the input. 
If the length of the list is greater than or equal to 5, return “Longer than 5”.
If the length is less than 5, return “Less than 5”."""

def length(l):
    a=0
    for i in l:
        a+=1
    if a>=5:
        return "Longer than 5"
    elif a<5:
        return "Less than 5"
lst=[]
for i in lst:
    i=int(input())
