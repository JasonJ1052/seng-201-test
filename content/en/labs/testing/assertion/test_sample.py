# Format: assert <boolean expression>
# assert True -> None. Continue execution normally.
# assert False -> AssertionError. An exception is thrown.

# assert True
# # assert False
# print("Made it to line 3.")

# x = 2**5
# assert x == 32
# assert type("Bob") == str
# y = 16
# assert x-y==16 and type("Bob") == str and int("25") == 25
# print("Made it to the bottom.")

# The right-hand side of assert can be any expression, but it must evaluate to True or False

# Assertions are the basis of automated testing.

# We are going to create test code for sample.py
# 1. import the file you want to test
# 2. Call the sample.py functions and check their return values. 
# 3. Are the return values what is expected? Use an assertion to check.


import sample  # We import the filename without the .py

assert sample.palindrome_check("kayak")  # the function should return True, giving "assert True"
assert sample.palindrome_check("Kayak")
assert sample.palindrome_check("moose") is False  # the function should return False, giving "assert False is False", which is True

# Create three tests for is_prime().
assert sample.is_prime(1) is False
assert sample.is_prime(2)
assert sample.is_prime(8) is False

assert sample.reverse_string("press") == "sserp"  # checking result for equality with expected
assert sample.reverse_string("alice") == "ecila"
assert sample.reverse_string("") == ""
print("All assertions passed!")

# Now, let's change our source code. Bob comes in an makes a mistake or a change.
# Define a function named power() that takes two parameterd, x and y, and returns the computed result.
# Then add assert statements.