import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    p={"q":movie,"type":"movies","limit":5}
    base="https://tastedive.com/api/similar"
    res=requests_with_caching.get(base,params=p)
    print(res.url)
    d=res.json()
    return d

def extract_movie_titles(d):
    #print (d)
    j=[]
    for i in d['Similar']['Results']:
        #print(i)
        j+=[i['Name']]
    return j

def get_related_titles(l):
    a=list(map(get_movies_from_tastedive,l))
    b=list(map(extract_movie_titles,a))
    c=[]
    for i in b:
        for k in i:
            if k not in c:
                c.append(k)
    return c

def get_movie_data(m):
    p={"t":m,"r":"json"}
    base="http://www.omdbapi.com/"
    s=requests_with_caching.get(base,params=p)
    print(s.url)
    s=s.json()
    return s
