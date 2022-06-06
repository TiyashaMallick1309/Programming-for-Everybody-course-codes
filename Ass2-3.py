"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
You should use input to read a string and float() to convert the string to a number."""

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate per hour:"))
Pay=hrs*rate
print("Pay:",Pay)
