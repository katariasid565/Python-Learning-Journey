## Variable Holds the data
name = "Alice"       # string
age = 30             # integer
price = 19.99        # float
is_student = True    # boolean


#### My Examples #######################################
love = "I love coding."  # string
my_age = 26           # integer
salary = 54000.50     # float
working = True      # boolean
Love_Job = False  # boolean

### Basic Arithematic Operations
x = 10
y = 3
print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3    (floor division)
print(x % y)   # 1    (modulus)
print(x ** y)  # 1000 (exponent)


### My examples arithematic operations #####################
a = 20
b = 4
print(a+b )  # addition 24
print(a-b )  # subtraction 16
print(a*b )  # multiplication 80
print(a/b)  # division 5.0
print(a//b) # floor division 5
print(a%b)  # modulus 0
print(a**b) or print(a^b)  # exponentiation 160000

#String Operations
greeting = "Hello"
name = "Bob"
print(greeting + ", " + name + "!")    # Hello, Bob!
print(greeting * 3)

#My examples string operations
greet = "Hi"
name = "Siddhant"
print(greet + ", " + name + "!" "Welcome to this work environment")
print(greet * 5)



#Type convertion
s = "123"
num = int(s)       # convert to integer
f = float(s)       # convert to float
txt = str(456)     # convert to string

num = 45
float = float(num)
text = str(num)
integer16 = int(num)

# day1_basics.py
name = "Charlie"
age = 25
print(f"My name is {name} and I am {age} years old.")

# play with arithmetic
a = 7
b = 4
print("7 to the power of 4 is", a**b)

##Exercise

"""_summary_
1. Create variables for your first name, last name, and birth year. Print a sentence introducing yourself.

2. Calculate and print:

The area of a rectangle (width × height).

The remainder when dividing two numbers.

3. Concatenate three strings of your choice into one sentence.
    
    """
print("-x-x-x" * 10) 
print("Excercise Section")
print("-x-x-x" * 10) 
    
# 1. Create variables for your first name, last name, and birth year. Print a sentence introducing yourself.
first_name = "Siddhant"
last_name = "Singh"
birth_year = 2000
print("Hi, I'm "+ first_name + " " + last_name + " " + "and I am learning coding using AI faster than ever.")

# 2 Calculate and print:
# The area of a rectangle (width × height).
height = 10
width = 5
area_of_rectangle = height * width
print(f"The Area of the rectangle is: {area_of_rectangle}")

# The remainder when dividing two numbers.

num1 = 25
num2 = 3

reminder = num1 /num2
print(f"The reminder of the two numbers is: {reminder}")

str1 = "I love sex,"
str2 = "I love coding too, "
str3 = "I wanted to switch my career for better life."
print(str1 + str2 + str3)
