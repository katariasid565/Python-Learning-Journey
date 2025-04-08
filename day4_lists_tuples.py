"""

<--X----------X------List and Tuples-----X----------X---------X-----------X-------->

<-----List----------> Mutable.....

Creating a list: fruits = ["apple","banana","mango"]
print(fruits)

Accessing Elements:
print(fruits[0])
print(fruits[-1]) # from last item

modify elements
fruits[1] = 'Orange'
print(fruits) # ['apple', 'orange', 'cherry']

Adding Elements:
fruits.append("grapes") # added at the last.
fruits.insert(2,"cherry") #added at index 2.

Removing Elements:
fruits.remove("grapes") # Remove by value
fruits.pop() # removes from the last.
del fruits[1] #remove by index


Looping through the list
for i in fruits:
	print(i)

<----------------x----------------------->

<--------Tuples----------> Immutable........

Creating a tuple.

colors = ("red", "yellow", "Green")
print(colors[1])

Tuple unpacking
x,y,z = colors
print(x,y,z) # red,yellow,green

Why use tuples?

> Faster than lists
> Useful for fixed data (e.g. coordinates


"""
# Write a list of 5 favourite movies.

movies = ["Matrix","John-Wick","Inception","The great Gatsby","Dunkirk"]

#Add a movie into the list and remove some.
movies.append("Avatar")
movies.insert(2, "The dark knight")

movies.pop()
del movies[-2]

# Print all the movies using loop.

for movie in movies:
	print(movie)


#Create a tuple with 3 cities and print them using unpacking.
cities = ('New York','Bhopal','Seattle')

a,b,c = cities
print(a,b,c)








