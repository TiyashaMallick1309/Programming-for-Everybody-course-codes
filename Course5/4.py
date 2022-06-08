"""Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
and assign the answer to a variable num_words_list. 
(You should use the len function)."""

num_words_list=[]
original_str = "The quick brown rhino jumped over the extremely lazy fox"
str=original_str.split()
for i in str:
    num_words_list=num_words_list+[len(i)]
    
