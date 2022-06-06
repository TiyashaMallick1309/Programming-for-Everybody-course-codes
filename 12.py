"""Write a function, sublist, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5)."""

def sublist(l):
    i=0
    lst=[]
    while i<len(l):
        if l[i]==5:
            break
        lst+=[l[i]]
        i+=1
    return lst
a=[]
for i in a:
    i=int(intput())
sublist(a)
