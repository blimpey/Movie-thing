import numpy as np
import pandas as pd

ratings_data = pd.read_csv("C:\Users\emwo1\Downloads\Movies\ratings.csv")

movie_names = pd.read_csv("E:\Datasets\ml-latest-small\\movies.csv")


// recall from list of hosts, are they necessary? 
hosts = [Kinetic, John, Vanessa, Dan]
Kinetic = [ "action" , " cult" , "monster" , "animation", "b-movie"]
John = ["documentary" , "food", "action" , "cult" , "animation"]
Dan = ["horror", "documentary",  "animation",  "b-movie",  "martial-arts"]
Vanessa = ["horror", "action", "cult", "drama", "animation", "b-movie"] 

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
    
movie_names.head()

movie_data = pd.merge(ratings_data, movie_names, on='movieId')

movie_data.head()

movie_data.groupby('title')['rating'].mean().head()

movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()

movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()
ratings_data.head()
input("Who is hosting?)
?

#give two options
Print("You can watch" /n  )