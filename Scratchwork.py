#libraries used
import numpy as np
import pandas as pd

#convert things to vectors with these to run cosine similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#import API decider, or API that can decide where to stream movies

#grab data from files
movies = pd.read_csv("movies.csv")
ratings_data = pd.read_csv("C:\Users\emwo1\Downloads\SampleData1\ratings.csv")
ratings_data.head()

movie_names = pd.read_csv("E:\Datasets\ml-latest-small\\movies.csv")
movie_names.head()

categories = ['keywords',  'genres', ]
for feature in categories:
    df[feature] = df[feature].fillna('')

#data pull

#combining features (multiple categories into 1 field) from the tutorial on cosine//
def combined_categories(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
df["combined_categories"] = df.apply(combined_categories, axis =1)

#sorting by titles
movie_data = pd.merge(ratings_data, movie_names, on='movieId')

movie_data.head()

movie_data.groupby('title')['rating'].mean().head()
movie_data.groupby('genre')['rating'].mean().head()
movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()

movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()

# recall from list of hosts, are they necessary? 
hostname = [Kinetic, John, Vanessa, Dan]
Kinetic = [ "action" , " cult" , "monster" , "animation", "b-movie"]
John = ["documentary" , "food", "action" , "cult" , "animation"]
Dan = ["horror", "documentary",  "animation",  "b-movie",  "martial-arts"]
Vanessa = ["horror", "action", "cult", "drama", "animation", "b-movie"] 
-----
#data validation for hosts
hostlist = {
"Vanessa":  ["horror", "action", "cult", "drama", "animation", "b-movie"],
"Kinetic":  [ "action" , " cult" , "monster" , "animation", "b-movie"],
"John":  ["documentary" , "food", "action" , "cult" , "animation"],
"Dan": ["horror", "documentary",  "animation",  "b-movie",  "martial-arts"]
}


print ("Who is hosting?")
host = input()


if (hostlist.get(host) is None ):
    print("There is no valid host")
else :
    print("Welcome back (" + host + ")!")
	other module.get 
print("You should watch " (Title1) + " or " + (Title2)"
	-------

print ("Who is hosting?") 
input(host)
// asking for the value of host , if no, returns bad data 
if (host.get(host) == null): 
    print("There is no valid host")

Host = 
Print  ("You can watch" /n  )
