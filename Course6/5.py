"""Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst."""

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=list(map(lambda a:2*a,lst))
