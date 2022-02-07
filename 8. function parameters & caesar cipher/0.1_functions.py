""" function defination and call function """

# function defination
def greet():
    print("Hi")
    print("How are you")
    print("who are you")

# call function
greet()
""" 
Hi
How are you
who are you """

""" Functions that allows input """

def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How are you {name}")

greet_with_name("akshay")
""" 
Hi akshay
How are you akshay """

""" 
what is parameter and argument ?
- name is known as parameter
- value passed to the name i,e "akshay" is known as argument """

""" function with more than 1 input """
def greet_with(name,location):
    print(f"Hi {name}")
    print(f"How is it living in {location}")

# way 1
greet_with("akshay","bengaluru") # positional argument, 1st value to 1st parameter, 2nd value to 2nd parameter
""" 
Hi akshay
How is it living in bengaluru """

# way 2
greet_with(location="bengaluru",name="akshay") # keyword argument, based on parameter maps values
""" 
Hi akshay
How is it living in bengaluru """

""" exercise 1 """

'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height X wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 X 4) ÷ 5
                     = 1.6
                     = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
'''

import math

test_h = int(input("Height of wall: ")) # 7
test_w = int(input("Width of wall: ")) # 13
coverage = 5

def paint_calc(height,width,cover):
    return print(f"You'll need {math.ceil((height*width)/cover)} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)
""" You'll need 19 cans of paint. """

""" Exercise 2 """
'''
prime numbers are numbers that can only be cleanly divided by itself and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
'''

def prime_checker(number):
    is_prime = True
    for i in range(2,number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(4)
# 4 is not a prime number

prime_checker(2)
# 2 is a prime number