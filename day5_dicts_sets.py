print("Day 5: Dictionaries and Sets.............")
print("*" *20)
print("Dictionaries (Key-Value Pairs)")
print("A dictionary stores data as key-value pairs, allowing for fast lookups.")
print("<-----Creating a dictionary----->\n")

student = {

 "name": "Alice",
 "age": 21,
 "course" : "Computer Science"

}

print(student["name"])

print("<------Adding & Modifying Data-------->\n")

student["age"] = 22
student["city"] = "New York" # Add new pair.

print("<-------------Removing Data-------->\n")

del student["city"]

age = student.pop("age") # Removes and return the value.

print(student)

print("\n Looping through the Dictionary\n")

for key,value in student.items():
	print(key," : ",value)


print("\n<----------Sets--------->\n")

print("Creating a set\n")

numbers = {1,2,3,4,4,5} # duplicated 4 removes.
print(numbers) # {1,2,3,4,5}
print("Adding and removing Elements.....\n")

numbers.add(6)
numbers.remove(3)
print(numbers)

print("Set Operations.....")

A = {1,2,3}
B = {3,4,5}

print(A|B) # Union: {1,2,3,4,5}
print(A&B) # intersection: {3}
print(A-B) # Difference: {1,2}

print("\n\n<--------------Exercise---------->\n\n")

# Write a dictionary for a book with title, author and year.

books = {

	"title": "The Great Gastby",
	"author": "F. Scott Fitzgerald",
	"year": 1925

}

print(books)

# Add a new key value pair and remove year
books["genre"] = "Romance, Thriller"
print("\n",books)

year = books.pop("year")
del books["genre"]

print(books)

# Create a set of 5 colors and add one more color.
colors = {"red","yellow", "blue", "green", "white", "red"}
print(colors)
colors.add("voilet")

print(colors)

num1 = {1,2,3,4}
num2 = {3,4,5,6}

print(num1 & num2)




















