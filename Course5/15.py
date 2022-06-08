"""Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, 
how much is in stock, and how much it costs. 
Print out each item in the list with the same formatting, using the .format method (not string concatenation). 
For example, the first print statment should read The store has 12 shoes, each for 29.99 USD."""

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for i in inventory:
    i=i.split(",")
    str1="The store has{} {}, each for{} USD."
    str2=str1.format(i[1],i[0],i[2])
    print(str2)
