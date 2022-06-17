"""Below, we have provided a list of lists that contain information about people. 
Write code to create a new list that contains every person’s last name, and save that list as last_names."""

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names=[]
k=""
for i in info:
    for j in i:
        k=i[1]
        break
    last_names+=[k]
