"""For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). 
Save these past tense words to a list called past_wrds."""

past_wrds=[]
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
for i in wrds:
    past_wrds+=[i+"ed"]
