"""We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, 
the number of retweets of that tweet, and the number of replies to that tweet.
We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score 
(which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet."""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(st):
    s=""
    st=str(st)
    for i in st:
        if i in punctuation_chars:
            st=st.replace(i,"")
        else:
            continue
    return st

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sen):
    sen=str(sen)
    sen=sen.lower()
    sen=sen.strip().split()
    c=0
    for i in sen:
        i=strip_punctuation(i)
        if i in positive_words:
            c+=1
    return c
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sen):
    sen=str(sen)
    sen=sen.lower()
    sen=sen.strip().split()
    c=0
    for i in sen:
        i=strip_punctuation(i)
        if i in negative_words:
            c+=1
    return c

tdata=open("project_twitter_data.csv","r")
tdata=tdata.readlines()

rdata=open("resulting_data.csv","w")
rdata.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

rt=0
rp=0
p=0
n=0
net=0
for i in tdata[1:]:        
    i=i.strip().split()
    for j in i[-1:]:
        j=j.split(",")        
        rt=j[-2]
        rp=j[-1]    
    i=strip_punctuation(i)  
    p=get_pos(i)
    n=get_neg(i)
    net=p-n
    rdata.write("{}, {}, {}, {}, {}".format(rt,rp,p,n,net))
    rdata.write("\n")
rdata.close()
                
