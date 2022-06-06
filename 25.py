"""Sort the list ids by the last four digits of each id. 
Do this using lambda and not using a defined function. 
Save this sorted list in the variable sorted_id."""

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
ids=[str(i) for i in ids]
sorted_id=sorted(ids,key=lambda k:k[-4:])
sorted_id=[int(i) for i in sorted_id]
