import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

"""#File One
for index, item in enumerate(data):
    print(f"{index}:{item["title"]}")


#File Two
x= int(input("Year after")) 
for index, item in enumerate(data):
    if item["year"] > x :
        print(f"{index}:{item["title"]}, {item["year"]}")


#File Three
x= int(input("Year after")) 
for index, item in enumerate(data):
    if item["year"] > x :
        print(f"{index}:{item["title"]}, {item["year"]}")


y= int(input("Year before")) 
for index, item in enumerate(data):
    if item["year"] < y :
        print(f"{index}:{item["title"]}, {item["year"]}")


#File 4
z= int(input("Same Year")) 
for index, item in enumerate(data):
    if item["year"] == z :
        print(f"{index}:{item["title"]}, {item["year"]}")

#File 5
t = input("Type in a Movie") 
for index, item in enumerate(data):
    if item["title"] == t :
        print(f"{index}:{item["title"]}")"""

#File 6
g = input("Type in a Genre") 
for index, item in enumerate(data):
    if g in item["genres"]:
        print(f"{index}:{item["title"]}")  













































        