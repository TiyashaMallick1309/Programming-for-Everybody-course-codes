"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40, and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value.  
You should use input to read a string and float() to convert the string to a number."""

def computepay():
    if (h<=40):
        pay=h*r
    elif(h>40):
        pay=(40*r)+((h-40)*r*1.5)
    return pay
h = float(input("Enter Hours: "))
r = float(input("Enter Rate per hour: "))
p = computepay()
print("Pay", p)
