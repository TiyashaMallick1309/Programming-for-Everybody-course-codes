"""Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. 
(i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) 
If you want to make this even more of a challenge, do this without slicing."""

def beginning(l):
    i=0
    j=1
    lst=[]
    while i<len(l):        
        if l[i]=="bye":
            break
        if j<=10:
            lst.append(l[i])
            j=j+1
        i+=1
    return lst
a=[]
for i in a:
    i=input()
beginning(a)
