"""Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

fname=open('mbox-short.txt')
dic=dict()
for fn in fname:
    if fn.startswith('From '):
        fn=fn.strip().split()
        f=fn[1]
        dic[f]=dic.get(f,0)+1
maxi=None
m=None
for i,j in dic.items():
    if (maxi is None or j>maxi):
        maxi=j
        m=i
print(m,maxi)
