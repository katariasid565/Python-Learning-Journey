#Write a function to calculate area that return the area of a rectangle.
def calculate_area(length, width):
	area = length * width
	if length == width:
		print("This is a square.")
	return area


# Write a function that returns true is number is even else return false.
def is_even(num):
	if num % 2 == 0:
		return True
	return False

print(calculate_area(40,20))
print(calculate_area(30,30))
print(is_even(56))
print(is_even(23))

