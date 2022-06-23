import requests_with_caching
import json

"""Your first task will be to fetch data from TasteDive.The documentation for the API is at https://tastedive.com/read/api.
Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. 
The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. 
It will be a python dictionary with just one key, ‘Similar’. 
HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. 
If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. 
Remember, you will not need an api key in order to complete the project, because all data will be found in the cache."""


def get_movies_from_tastedive(movie):
    p={"q":movie,"type":"movies","limit":5}
    base="https://tastedive.com/api/similar"
    res=requests_with_caching.get(base,params=p)
    print(res.url)
    d=res.json()
    return d

"""Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. 
Call it extract_movie_titles."""

def extract_movie_titles(d):
    #print (d)
    j=[]
    for i in d['Similar']['Results']:
        #print(i)
        j+=[i['Name']]
    return j

"""Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. 
It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. 
Don’t include the same movie twice."""

def get_related_titles(l):
    a=list(map(get_movies_from_tastedive,l))
    b=list(map(extract_movie_titles,a))
    c=[]
    for i in b:
        for k in i:
            if k not in c:
                c.append(k)
    return c

"""Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. 
The function should return a dictionary with information about that movie.
Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. 
You will need to provide the following keys: t and r. 
As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache."""

def get_movie_data(m):
    p={"t":m,"r":"json"}
    base="http://www.omdbapi.com/"
    s=requests_with_caching.get(base,params=p)
    #print(s.url)
    s=s.json()
    return s

"""Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. 
For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0."""

def get_movie_rating(s):
    t=s['Ratings']
    for i in t:
        if i['Source']=="Rotten Tomatoes":
            y=int(i['Value'][:-1])
            return(y)
    return 0

"""Define a function get_sorted_recommendations. It takes a list of movie titles as an input. 
It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. 
Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’."""

def get_sorted_recommendations(lst):
    e=get_related_titles(lst)
    f=sorted(e,key=lambda w:(get_movie_rating(get_movie_data(w)),w),reverse=True)
    return f
