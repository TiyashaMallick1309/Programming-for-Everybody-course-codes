"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 & 1.5 times the hourly rate for all hours worked above 40 hours. 
You should use input to read a string and float() to convert the string to a number."""

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour:")
r = float(rate)
if (h<=40):
	Pay=h*r
elif (h>40):
    Pay=(40*r)+((h-40)*r*1.5)
print(Pay)
