"""Write a function, sublist, that takes in a list of strings as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the string “STOP” 
(it should not contain the string “STOP”)."""

def sublist(l):
    i=0
    lst=[]
    while i<len(l):        
        if l[i]=="STOP":
            break
        lst+=[l[i]]
        i+=1
    return lst
a=[]
for i in a:
    i=intput()
sublist(a)
