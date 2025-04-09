"""
There are found main python keywords involved in exceptions handling.
try   except   finally   raise


Errors(exceptions) happen when something goes wrong,
like dividing by zero or trying to open a missing file.

Instead of letting our program crash, we can handle exceptions gracefully.

<-----------try-except (Basic Error Handling---------->

try:
	x = 10/0 # this will cause an error.
except ZeroDivisionError:
	print("Error: You cannot divide by zero!")

# IF and error occurs inside try, python jumps to except instead of crashing.

<------------Handling Multiple Exceptions----------------->

try:
	num = int(input("Enter a number: ")) # Might fails if user enters a letter.
	result = 10/num #Might fails if entered number is zero.
except ValueError:
	print("Invalid input! Please enter a number.")

except ZeroDivisionError:
	print("Error: Cannot Be divide by zero.")

# We can catch mutiple errors seperately.

<---------Using 'finally' (Code that always run)------------>


try:
	file = open("example.txt", "r") # Might fails if file doesn't exists.
	content = file.read()
	print(content)

except FileNotFoundError:
	print("Error: File not found!")

finally:
	print("This will always run.")

#'finally' always run wheather an error occurs or not.


<-----------------Raising Custom Errors------------->

age = int(input("Enter your Age: "))

if age < 0:
	raise ValueError("Age cannot be negative.")
else:
	print(f"Your age is {age}")

# 'raise' manually triggers an error if needed.

"""
# Write a program that asks for two numbers and divides them.

try:
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	result = num1/num2

except ValueError:
	print("Error: Please enter a valid number.")

except ZeroDivisionError:
	print("Error: Cannot be divide by Zero")


# Write a program and try opening a file named data.txt. If it doesn't exist, catch error.

try:
	file = open("data.txt", "r")
	data = file.read()
	print(data)
except FileNotFoundError:
	print("Error: File not found")

finally:
	print("Program will execute completely...")









