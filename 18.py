"""You will be sorting the following list by each element’s second letter, a to z. 
Create a function to use when sorting, called second_let. 
It will take a string as input and return the second letter of that string. 
Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. 
Do not use lambda."""

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(a):
    for i in a:
        return a[1]
sorted_by_second_let=sorted(ex_lst,key=second_let)
