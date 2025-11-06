---
title: Unit testing
description: Using assertions to test a file.
weight: 10
---

## Class video

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ki3Ei-3M-ZE?si=pJ8HU1gWwM90GFfx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Testing `sample.py`

***Assertions*** are the basis of modern automated testing. Developers write ***test code*** in source files that are separate from the main program code. We have our program code in `sample.py` and the test code will be in `test_sample.py`. This is a common naming convention. 

Now, let's use our `assert` to test the correctness of the functions in `sample.py`.
1. Comment out all the code in `test_sample.py`
2. Add the line `import sample`. In Python, this makes the content of `sample.py` accessible to code in `test_sample.py`.[^1]
3. Now let's convert those `print(...)` statements from `sample.py` into `assert` statements in `test_sample.py`. `test_sample.py` should now have the following:
    {{< card code=true header="`test_sample.py`" lang="python" >}}
import sample  # We import the filename without the .py

assert sample.palindrome_check("kayak")  # the function should return True, giving "assert True"
assert sample.palindrome_check("Kayak")
assert sample.palindrome_check("moose") is False  # the function should return False, giving "assert False is False", which is True

assert sample.is_prime(1) is False
assert sample.is_prime(2)
assert sample.is_prime(8) is False

assert sample.reverse_string("press") == "sserp"  # checking result for equality with expected
assert sample.reverse_string("alice") == "ecila"
assert sample.reverse_string("") == ""
print("All assertions passed!")
{{< /card >}}

**Point 1:** We access the functions in `sample.py` by calling, e.g., `sample.palindrome_check(...)`. The prefix `sample.X` tells Python "go into the `sample` module and call the function named X." We would get an error if we called only `sample.palindrome(...)` because Python would be looking in the *current running file*, which has no such function defined in it.

**Point 2:** In Python, you *should* check if a value is `True` or `False` using `is`. The `is` operator returns a boolean. You could also type `x == True` or `x == False`. Either form will work, but `is` is preferred[^2].

**Point 3:** Remember that `palindrome_check()` and `is_prime()` return True/False themselves. We are simply verifying that they are returning the correct value. `reserve_string()` returns a string value, so we need to compare using `==` to an expected value.

**Point 4:** The program will crash with an `AssertionError` if any of the `assert` statements are `False`. Mess up one of the assertions to verify this.

### Exercise
1. Go to `sample.py` and define a function named `power()` that takes two parameters, `x` and `y`, and returns the computed result of `xʸ`. 
2. Add `assert` statements to `test_sample.py` to verify your function behaves correctly.

## Unit tests

The file `test_sample.py` is what software engineers call an ***automated unit test***. A ***unit test*** is a group of test code (usually one file) that verifies a single class or source file[^3]. Unit tests are usually written by the same developer who wrote the program code. 

Our automated unit test now calls functions and use `assert` statements to verify that they are returning the expected results. If an assertion fails, the test fails. 

**What does it mean if a test fails?** One of two things:
1. Either there is something wrong in the program code. Maybe there is a logic error.
2. The test code itself has a mistake in its logic.

Regardless, if a test fails, you need to figure out why. A ***good*** unit test will systematically exercise all the logic of the function or module under test. This can help uncover flaws in the program code. We will discuss strategies to do this in subsequent lessons.


We also need a way to run the test code and accumulate the results in a useful way. We will do this in the next lab.


## Knowledge check
- Question: Suppose you wanted to test a function named `get_patient_priority(str)` in `hospital.py`. What would you have to do to call the function from your test code?
- Question: The right hand side of an `assert` statement can be *any* expression (simple or complex) as long as it evaluates to _____ or _____.
- Question: Who writes unit tests?
- Question: The name for a test that tests an individual module is a ______ test.
- Question: Why do you think we write separate `assert` statements for each function input, rather than one `assert` statement that calls the function multiple times with different inputs? That is, why not do `assert sample.reverse_string("alice") == "ecila" and sample.reverse_string("") == ""`?


[^1]: In Python parlance, a single file is called a ***module***. You can create complicated modules that are collections of multiple source files. This is how many popular Python libraries like `random` work, as do third party libraries like `pytorch` and `keras` used for machine learning. It is a way to bundle functions and *classes* for convenient use in source code.

[^2]: If you are dying to know the difference between `x is False` and `x == False`, it's because many other values are equivalent to True and False when using `==`. Empty values, such as `0` or `[]` are `== False` (try it). But only `False is False`. Similarly, only `True is True`, but `1 == True`.

[^3]: The *unit* is usually a single class. However, in our case, there is no class, but a collection of functions in a file. Some people treat a file as a unit. But a file can have multiple classes in it. The definition of a *unit* is a bit fuzzy, but usually refers to either a class or a single file.