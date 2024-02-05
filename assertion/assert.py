""" CREDITS: https://realpython.com/python-assert-statement/ """

number = 42
assert number > 0

number = -42
assert number > 0
""" Traceback (most recent call last):
    ...
AssertionError """

# provide more information to developers

number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"
""" Traceback (most recent call last):
    ...
AssertionError: number greater than 0 expected, got: -42 """

# ASSERT MULTI LINE STATEMENT

number = 42

assert number > 0 and isinstance(number, int), \
    f"number greater than 0 expected, got: {number}"

# ASSERTION FORMATS

# 1. Comparison assertions
assert 3 > 2
assert 3 == 2
""" Traceback (most recent call last):
    ...
AssertionError """

assert 3 > 2 and 5 < 10
assert 3 == 2 or 5 > 10
""" Traceback (most recent call last):
    ...
AssertionError """

# 2. Membership assertions
numbers = [1, 2, 3, 4, 5]
assert 4 in numbers
assert 10 in numbers
""" Traceback (most recent call last):
    ...
AssertionError """

# 3. Identity assertions
x = 1
y = x
null = None

assert x is y
assert x is not y
""" Traceback (most recent call last):
    ...
AssertionError
 """

assert null is None
assert null is not None

""" Traceback (most recent call last):
    ...
AssertionError """

# 4. Type check assertions
number = 42
assert isinstance(number, int)

number = 42.0
assert isinstance(number, int)
""" Traceback (most recent call last):
    ...
AssertionError """

# Documenting Your Code With Assertions

def get_response(server, ports=(443, 80)):
    # The ports argument expects a non-empty tuple
    for port in ports:
        if server.connect(port):
            return server.get()
    return None

# alert developers about this
def get_response(server, ports=(443, 80)):
    assert len(ports) > 0, f"ports expected a non-empty tuple, got {ports}"
    for port in ports:
        if server.connect(port):
            return server.get()
    return None

# Debugging Your Code With Assertions

# circle.py

import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def area(self):
        assert self.radius >= 0, "positive radius expected"
        return math.pi * self.radius ** 2

# suppose another team members adds a new function to class

class Circle:
    # ...

    # while computing radius coefficient, there is no validation and there can be bug (negative coefficent is possible)
    def correct_radius(self, correction_coefficient):
        self.radius *= correction_coefficient

from circle import Circle

tire = Circle(42)
tire.area()
# 5541.769440932395

tire.correct_radius(-1.02)
tire.radius
# -42.84

tire.area()
""" Traceback (most recent call last):
    ...
AssertionError: positive radius expected """

# Disabling Assertions in Production for Performance

# To activate optimized mode and disable your assertions, you can either start up the Python interpreter
# with the –O or -OO option, or set the system variable PYTHONOPTIMIZE to an appropriate value.

# C:\> set PYTHONOPTIMIZE=1  # Equivalent to python -O

# C:\> set PYTHONOPTIMIZE=2  # Equivalent to python -OO

# assertion using pytest
# python -m pip install pytest

# test cases

# test_samples.py

def test_sum():
    assert sum([1, 2, 3]) == 6

def test_len():
    assert len([1, 2, 3]) > 0

def test_reversed():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]

def test_membership():
    assert 3 in [1, 2, 3]

def test_isinstance():
    assert isinstance([1, 2, 3], list)

def test_all():
    assert all([True, True, True])

def test_any():
    assert any([False, True, False])

def test_always_fail():
    assert pow(10, 2) == 42

# run in command line
# pytest test_samples.py

# store.py

# use assert for dev, for prod use as below
# Code in production

def price_with_discount(product, discount):
    if 0 < discount < 1:
        new_price = int(product["price"] * (1 - discount))
        return new_price
    raise ValueError("discount expects a value between 0 and 1")



