"""
What is keywords ?
- keywords are reserved words. Ex: if, continue, for, etc.

why keywords ?
keywords are the building blocks of python programming language.
Ex: 
- to check if 2 is greater than 1
    if 2 > 1: ("if" is the reserved word in python)
        print('Yes')

"""

# how ?
import keyword

# print all the keywords that are present in python
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print("Total number of keywords: ",len(keyword.kwlist))
# Total number of keywords:  35