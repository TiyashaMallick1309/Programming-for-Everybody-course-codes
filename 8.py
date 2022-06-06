"""You will need to write two functions for this problem. 
The first function, divide that takes in any number and returns that same number divided by 2. 
The second function called sum should take any number, divide it by 2, and add 6. 
It should return this new number. You should call the divide function within the sum function."""

def divide(a):
    a=a/2
    return a
def sum(r):
    r=(divide(r))+6
    return r
