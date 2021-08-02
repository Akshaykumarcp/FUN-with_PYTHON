"""
What is Identifiers ?
- Identifiers are the name given to for variables, functions, classes, etc.

Why Identifiers ?
- variables are used to store values
- functions are used to organise and re-use code
- classes are used to structure Object Oriented Programming (OOPS)
- Each names for the usage of variables, functions and classes must be unique and differentiable.

Rules for Identifiers:
- Identifiers can contain a to z, A to Z, 0 to 9 and _ (underscore)
- Cannot begin with digits. Ex: 1dog --> invalid. dog1 --> valid
- Python keywords are not used as identifiers
- Cannot use special char such as !, @, #, $, %, etc in identifiers
"""

# how ?

tickets = 2 # tickets is the variable

# identifier cannot use reserved words
global = 3
""" File "<stdin>", line 1
    global = 3
           ^
SyntaxError: invalid syntax """

