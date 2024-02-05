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
