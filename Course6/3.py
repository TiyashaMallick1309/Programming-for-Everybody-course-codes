"""Below, we have provided a list of lists named L. 
Use nested iteration to save every string containing “b” into a new list named b_strings."""

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for i in L:
    for j in i:
        if "b" in j:
            b_strings+=[j]
