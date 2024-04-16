# FUN-with_PYTHON
Python for data science

![alt text](https://github.com/Akshaykumarcp/FUN-with_PYTHON/blob/main/mind_mapping_python.jpg)

### Python REPL
- Default Python REPL
- PTPYTHON (https://github.com/prompt-toolkit/ptpython)

### Python Assert

- automatically detect errors in your Python programs.
- make your programs more reliable and easier to debug.
- If assert condition is true, program continues
- If assert condition is false, AssertionError exception is raised.
- Can't we use if statement along with exception?
  - proper use of assertions is to inform developers about unrecoverable errors in a program.
  - assertions are not for regular error handling such as file not found.
  - Assertions are for internal self checks of program. Assertions work by declaring some conditions as impossible in code. If one of these conditions doesn't hold, there's a bug in program
  - Not for handling run time errors.
  - Goal: developers know likely root cause of bug quickly

Assertion syntax:
```
assert_stmt ::= "assert" expression1 ["," expression2]
```

Common pitfalls with using asserts:
- Don't use assert for data validation
  - if asserts are disabled, validations will be missed out
- Asserts that never fail

### Underscores, Dunders, and More

- Single Leading Underscore: _var
  - say another programmer that a variable or method is intended for internal use.
  - Convention defined in PEP8.
  - Convention isn't enforced by the python interpreter.
- Single Trailing Underscore: var_
  - Sometimes the most fitting name for a variable is already taken by a keyword in the Python language.
  - Example class or def cannot be used as variable names in Python.
  - In this case, you can append a single underscore to break the naming conflict.
  - Used by convention to avoid naming conflicts with Python keywords.
- Double Leading Underscore: __var
  - A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.
  - This is also called name mangling—the interpreter changes the name of the variable in a way that makes it harder to create collisions when the class is extended later.
  - Also called as name mangling. Look at a example for more understanding.
  - Triggers name mangling when used in a class context.
  - Enforced by the Python interpreter.
- Double Leading and Trailing Underscore: __var__
  - A.K.A dunders or double underscores or magic methods
  - example: __init__ as pronounced as "dunder init"
  - Core feature in python.
  - Indicates special methods defined by the Python language.
  - Avoid this naming scheme for your own attributes.
  - Can overside as needed.
- Single Underscore: _
  - Used as a name to indicate that a variable is temporary or insignificant.
  - Use single underscores in unpacking expressions as a “don’t care” variable to ignore particular values.

### Python tools for dev

- Code format: [Black](https://github.com/psf/black)
- Code lint and formatter: [ruff](https://github.com/astral-sh/ruff)
- Python packaging:
  - [Python packaging](https://packaging.python.org/en/latest/overview/)
  - [TOML](https://toml.io/en/)
    - Libs: [tomllib](https://docs.python.org/3/library/tomllib.html), [tomlkit](https://github.com/python-poetry/tomlkit), [tomli](https://github.com/hukkin/tomli), [all other](https://github.com/toml-lang/toml/wiki)
- Lint (Style and quality): [flake8](https://github.com/PyCQA/flake8)
