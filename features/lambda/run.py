calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20)) # Even number

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101")) 
# filter_nums(): Geeks

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))
# do_exclaim(): I am tired!

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))
# find_sum(): 2


## --------------------------

# The lambda function gets more helpful when used inside a function

l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), l)))

# https://www.geeksforgeeks.org/python-lambda/