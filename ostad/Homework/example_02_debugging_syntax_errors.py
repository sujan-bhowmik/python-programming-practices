"""
Example 02: Debugging Syntax Errors
Live Class 03 - Practice Session

Goal: Learn to READ a SyntaxError/IndentationError traceback and fix it.
A SyntaxError happens BEFORE the program runs at all - Python cannot even
start, because the code does not follow Python's grammar rules yet.

NOTE: Broken code cannot literally sit inside a runnable .py file (the
whole file would fail to parse). So below, each bug is shown as a comment
(the WRONG line + the EXACT error Python 3.14 gives for it - verified by
actually running it), followed by the CORRECTED line that really executes.
"""

# ---------------------------------------------------------------------
# Bug 1: Unterminated string literal (a missing closing quote)
# ---------------------------------------------------------------------
# WRONG:
#   name = input("Enter your name: )
#
# Error:
#   SyntaxError: unterminated string literal (detected at line 1)
#
# FIX: close the quote.
name = input("Enter your name: ")

# ---------------------------------------------------------------------
# Bug 2: Unclosed parenthesis (a missing closing bracket)
# ---------------------------------------------------------------------
# WRONG:
#   age = int(input("Enter your age: ")
#
# Error:
#   SyntaxError: '(' was never closed
#
# FIX: count your open "(" against your close ")" - here int(...) needs
# its OWN closing bracket, separate from input(...)'s.
age = int(input("Enter your age: "))

# ---------------------------------------------------------------------
# Bug 3: Missing comma between print() arguments
# ---------------------------------------------------------------------
# WRONG:
#   print("Age" age)
#
# Error:
#   SyntaxError: invalid syntax. Perhaps you forgot a comma?
#
# FIX: separate arguments with a comma.
print("Age", age)

# ---------------------------------------------------------------------
# Bug 4: Unexpected indent (extra spaces before a line that should not
# be indented - this class hasn't reached if/for/def yet, so EVERY line
# must start at column 0)
# ---------------------------------------------------------------------
# WRONG:
#   total = 100
#      print(total)
#
# Error:
#   IndentationError: unexpected indent
#
# FIX: remove the extra leading spaces.
total = 100
print(total)

# ---------------------------------------------------------------------
# Bug 5: Unclosed f-string brace (a missing closing "}")
# ---------------------------------------------------------------------
# WRONG:
#   print(f"Total: {total")
#
# Error:
#   SyntaxError: f-string: expecting '}'
#
# FIX: close the curly brace.
print(f"Total: {total}")

# ---------------------------------------------------------------------
# Golden Rule: read the LAST line of the traceback first (the error type
# and message), then look at the "^" marker to see exactly where Python
# got confused.
# ---------------------------------------------------------------------

# Expected Output (example):
# Enter your name: Tahmid
# Enter your age: 25
# Age 25
# 100
# Total: 100
