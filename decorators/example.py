# https://realpython.com/primer-on-python-decorators

# Simple Decorators

# example 1
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee) # say_whee points to wrapper()
"""
<function my_decorator.<locals>.wrapper at 0x00000196062D8CC0> """

say_whee()
"""
Something is happening before the function is called.
Whee!
Something is happening after the function is called. """

# decorators wrap a function, modifying its behavior

# example 2

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee() # Whee!

# use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()
"""
Something is happening before the function is called.
Whee!
Something is happening after the function is called. """

# Reusing Decorators

# move decorator to own module. created decorators.py file and added decorator func

from .decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()
"""
Whee!
Whee! """

# Decorating Functions With Arguments

from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

"""
say_whee()
Whee!
Whee!

greet("World")
Hello World
Hello World """

# Returning Values From Decorated Functions

from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# decorators added return

return_greeting("Adam")
""" Creating greeting
Creating greeting
'Hi Adam' """

# Who Are You, Really?

# say_whee() has gotten very confused about its identity.
# It now reports being the wrapper_do_twice() inner
# function inside the do_twice() decorator. Although
# technically true, this is not very useful information
# to fix this, decorators should use the @functools.wraps
# decorator, which will preserve information about the
#  original function. Update decorators.py

# run in terminal
say_whee
# <function say_whee at 0x7ff79a60f2f0>

say_whee.__name__
# 'say_whee'

help(say_whee)
# Help on function say_whee in module whee:

# A Few Real World Examples

# ref for boilerplate template
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

# creating a @timer decorator. It will measure the time a function takes to execute and print the duration to the console.

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1) # Finished 'waste_some_time' in 0.0053 secs
waste_some_time(999) # Finished 'waste_some_time' in 1.8348 secs

# Debugging Code
# @debug decorator will print the arguments a function is called with as well as its return value every time the function is called:

import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Benjamin")
"""
Calling make_greeting('Benjamin')
'make_greeting' returned 'Howdy Benjamin!'
'Howdy Benjamin!' """

# example calculates an approximation to the mathematical constant e

import math
from decorators import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e(5)
"""
Calling factorial(0)
'factorial' returned 1
Calling factorial(1)
'factorial' returned 1
Calling factorial(2)
'factorial' returned 2
Calling factorial(3)
'factorial' returned 6
Calling factorial(4)
'factorial' returned 24
2.708333333333333 """