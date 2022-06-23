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
