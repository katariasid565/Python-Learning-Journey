# Ask for a user's age and prints if they are a minor, adult or senior citizen
age = int(input())
if age >50:
	print("Senior Citizen")
elif age>21:
	print("Adult")
else :
	print("Minor")

# print the numbers from 1 to 10 but skips number 5 using continue.
for num in range(1,11):
	if num == 5:
		continue
	print(num,"\n")

# using a while loop to print numbers from 10 to 1 in reverse.

x = 10

while x >= 1:
	print("Iteration: ", x)
	x -= 1

