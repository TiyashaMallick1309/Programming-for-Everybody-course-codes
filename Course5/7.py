"""The variable sentence stores a string. 
Write code to determine how many words in sentence start and end with the same letter, 
including one-letter words. Store the result in the variable same_letter_count."""

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
c=sentence.split()
same_letter_count=0
for i in c:
    if (i[0]==i[-1]):
        same_letter_count+=1
