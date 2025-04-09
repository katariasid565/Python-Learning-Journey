"""
File handling (Reading and Writing Files)

Python allows us to read from and write to files, which is essential for storing and retrieving data.

##Reading a File####

with open('example.txt', "r") as file:
	content = file.read()
	print(content)

open('filename', "r") open file in reading mode.
with  automatically closes the file when done.

######Writing to a file#######

with open("example.txt", "w") as file:
	file.write("Hello, This is a new file!")

'w' mode overwrites the file if it exists.

#### Appending to a file(Adding Data) #####

with open('example.txt', 'a') as file:
	file.write("\nThis is a new line in the file.")

'a' : mode adds content instead of replacing it.

#### reading a file line by line #####

with open("example.txt", "r") as file:
	for line in file:
		print(line.strip()) # strip function removes the extra spaces.

#### Working with csv files #####

csv (Comma-Seperated Values) files arecommonly used for data storage.

-> writing to a csv file

import csv

with open("example.csv", "w", newline = "") as file:
	writer = csv.writer(file)
	writer.writerow(["Name","Age","City"])
	write.writerow(["Alice", 26,"New York"])
	write.writerow(["Zack",23,"Chicago"])
	write.writerow(["James", 31, "Ohio"])

-> Reading to a csv file

with open('example.csv', "r") as file:
	reader = csv.reader(file)
	for line in reader:
		print(line)

"""

##Exercise##

# Create a text file and write 3 line of text.

with open("day6.txt", "w") as file:
	file.write("Hello I'm the first line.")
	file.write("\nHello I'm the second line.")
	file.write("\nHello I'm the third line.\n")

# Read and print the contents of the file.

with open("day6.txt", "r") as file:
	content = file.read()
	print(content)

#Add two more lines and read it again.

with open("day6.txt", "a") as file:
	file.write("\nHello, This is the new line 1.")
	file.write("\nHello, This is the new line 2.\n")

#Reading and printing the file.
with open("day6.txt", "r") as file:
	print(file.read())
import csv
#Create a csv file and print the 3 rows of student data.

with open("day6.csv", "w", newline="") as file:
	writer = csv.writer(file)
	file.write("Students Maths marks......\n")
	writer.writerow(["Name","Roll_No","Marks"])
	writer.writerow(["Sid",21,98])
	writer.writerow(["Aditi", 22, 95])
	writer.writerow(["Preeti",7, 86])


##reading the data.

with open("day6.csv", "r") as file:
	reader = csv.reader(file)
	for line in reader:
		print(line)
