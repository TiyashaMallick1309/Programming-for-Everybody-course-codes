"""Write code that counts the number of words in sentence that contain either an “a” or an “e”. 
Store the result in the variable num_a_or_e.
Note 1: be sure to not double-count words that contain both an a and an e.
HINT 1: Use the in operator.
HINT 2: You can either use or or elif."""

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e=0
s=sentence.split()
for i in s:
    if "a" in i:
        num_a_or_e+=1
    elif "e" in i:
        num_a_or_e+=1
