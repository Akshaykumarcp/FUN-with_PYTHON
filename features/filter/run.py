# ------ Example -----------

# Function to check if a number is even
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

# Convert filter object to a list
print(list(b)) # [2, 4, 6]

# Using filter() with lambda

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)

print(list(b)) # [2, 4, 6]

# Combining filter() with Other Functions

a = [1, 2, 3, 4, 5, 6]

# First, filter even numbers
b = filter(lambda x: x % 2 == 0, a)

# Then, double the filtered numbers
c = map(lambda x: x * 2, b)

print(list(c)) # [4, 8, 12]

# https://www.geeksforgeeks.org/filter-in-python/