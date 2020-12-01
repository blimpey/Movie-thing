#Define Hosts and validate any input
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
