---
title: Testing for exceptions
description: How to test for *expected* exceptions.
weight: 25
---


## Before you start
If necessary, fix up your `sample.py` so that all your test cases pass.

## Testing for exceptions
Sometimes, the expected behavior of a function is that it throws an exception. How do we test for *expected* exceptions given an input? 

Suppose we want `reverse_string()` to work only for strings containing the letters [a&ndash;z] and to throw an exception if the string contains any other characters. Change `reverse_string()` in `sample.py` to the following:
```python {linenos=true,linenostart=13}
def reverse_string(s):
    if not s.isalpha():
        raise ValueError('letters a-z only')
    return s[::-1]
```
This is appropriate given the requirements of `reverse_string()`. It returns a reversed `str` input under normal circumstances, but raises an exception under abnormal circumstances, a.k.a., *exceptional conditions* from our *problem statement* structure. 

"Raising" and "throwing" an exception are the same thing. You will hear both terms in practice. The keyword in Python is `raise`, and exceptions in Python always end with the string `Error`, e.g., `ValueError` or `IndexError`.

<!-- Returning an error message would *not* be appropriate because the output format is the reversed string, not a message! `raise` and `return` are different. Figuring out when to throw and catch exceptions can be tricky. We will cover low-level design and throwing/catching exceptions later in the course. -->

### Exercise
1. Define a new test case in `test_sample.py` named `test_reverse_exception` and add a call to `sample.reverse_string` with an input that will trigger the exception.
1. Run `pytest`. You should see a test summary similar to the following:
```bash
================================= short test summary info =================================
FAILED test_sample.py::test_reverse - ValueError: letters a-z only
FAILED test_sample.py::test_reverse_exception - ValueError: letters a-z only
=============================== 2 failed, 2 passed in 0.06s ===============================
```
I have two test failures: the new test case I created, and the original `test_reverse`. This is because `test_reverse` in my code contains the call `assert sample.reverse_string('')`. The empty string does not consist of the letters [a&ndash;z], so an exception is correctly raised.

**This is an important lesson**: as program code evolves, so too might the test code. Move the `assert sample.reverse_string('')` to the `test_reverse_exception` test case where it logically belongs.


Your test cases for `reverse_string` should now look something like this:
```python {linenos=true,linenostart=13}
def test_reverse():
    assert sample.reverse_string("press") == "sserp"  # checking result for equality with expected
    assert sample.reverse_string("alice") == "ecila"

def test_reverse_exception():
    sample.reverse_string("abc123")
    sample.reverse_string("")
```


## Verifying expected exceptions with `pytest`

Our `assert` statements only check the return values of functions. `pytest` provides a convenient helper function to check if an exception was raised.

First, add the line `import pytest` to the top of your test code file `test_sample.py`.

Second, change `test_reverse_exception` to the following:
```python {linenos=true, linenostart=18}
def test_reverse_exception():
    with pytest.raises(ValueError):   # the pytest.raises comes from the imported pytest module
        sample.reverse_string("abc123")
    
    with pytest.raises(ValueError) as err:  # we can optionally capture the exception in a variable
        sample.reverse_string("")
    assert str(err.value) == "letters a-z only"  # convert the exception to a str and verify the error message
```
A few things of note:
- `pytest.raises(...)` *requires* that you specify the **type** of exception. In our case, we expect a `ValueError` to be raised.
- We can *optionally* capture the exception itself. That's what `as err` does on line 22. `err` is a variable (name it whatever you want) that captures the exception.
- On line 24, we can call `str(err)` to convert the exception to a string. That error message should be `"letters a-z only"`, which comes from the line `raise ValueError('letters a-z only')` in `sample.py`.

This test case would fail if `reverse_string()` ***did not*** raise an exception

### Exercise
1. Comment out the if-statement and exception raising lines in `reverse_string()` and rerun `pytest`. How does the pytest output for an expected exception differ from a failed `assert`?

## Checking exception values
Checking the exception message is useful because we may want our function to raise `ValueError`s under different circumstances. For example, maybe we want to raise a ValueError for the empty string that says 'string cannot be empty', and a different ValueError for `letters a-z only`. 

Why would you want to raise two different ValueErrors? Because it tells the caller of `reverse_string()` what they did wrong and how to fix it. It's similar rationale to why we split our `assert` statements and our test cases into multiple instances to get more precise info.

### Exercise
1. Put the if-statement and exception raising back in `reverse_string()`. Add an if-statement **at the beginning of the function** to check if the input parameter is the empty string. If so, raise `ValueError('string must not be empty')`. Re-run `pytest`. What happens?
1. Modify your `test_reverse_string` so that both `with pytest.raises(...)` calls capture the error as in line 22. Add/modify `assert` statements to verify that the appropriate error message is in the exception.






## Recap
We accomplished a couple significant things in this lab:
1. We installed the `pytest` package using `pip`. Again, you only need to do this once.
2. We ran `pytest`, which scans for files and functions named `test_*` and runs them.
3. `pytest` collects test case successes and failures independently from one another, allowing us to get more information with each run of our test code.
4. `pytest` displays a summary of the results in human-friendly format.


## Knowledge check
- Question: (True/False) Raising and throwing exceptions are two different things.
- Question: Why should you not exception logic in the same test case where you test "normal" logic?
- Write a code block using `pytest` that checks that the `determine_priority(str)` function correctly throws a `TypeError` when passed anything other than a string.
- Question: What happens when running `pytest` and the program code raises an exception that you **do not** expect?
