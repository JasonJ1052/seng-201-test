---
title: Structuring test code
description: Organizing the test code has benefits, just like organizing program code.
weight: 15
---
## Class video
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mDY9NTtOApU?si=GVyWEI-l8Qjt9d0N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Limitations to the current approach

In [the previous lab](../unit-test/), we gathered our `assert` statements into a test file that can be run. If the test file runs to completion, our tests have passed. If it fails with an `AssertionError`, we know that a test has failed and something is wrong (either with the program code or the test code itself). We have the beginnings of ***automated unit testing***.

### Our current goal
What we have so far is a good start, but we have two things to improve upon:
1. Currently, we can only fail one `assert` the test file at a time because a failed assertion throws an exception and halts the program. Ideally, we would like to run *all* tests and identify which individual ones are failing.
1. We would like to collect our test results in a human-friendly format. I run the test, I get a summary of passes and fails. 

We can accomplish these both these things. First, we need to *organize* our test cases in our test file. Second, we will need help from developer tools.

### Current state

Here is our `sample.py` file:
{{< card code=true header="`sample.py`" lang="python" >}}
def palindrome_check(s):
    cleaned_str = ''.join(s.lower()) 
    return cleaned_str == cleaned_str[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]
{{< /card >}}


And here is the test code:

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

Remember, we use the ***naming convention*** `test_<file>.py` to identify the unit test for `<file>.py`. 

## Organizing test code into *test cases*
To meet [our goal](#our-current-goal), we will first organize our `assert` statements into ***test cases***, which has a conceptual and a literal definition:
1. ***test case (concept)***: inputs and expected results developed for a particular objective, such as to exercise **a particular program path** or verify that **a particular requirement is met**. [Adapted from [ISO/IEC/IEEE 24765](https://www.iso.org/standard/71952.html)].
1. ***test case (literal)***: a test function within a test file.

Let's start simple. Let's move the `assert` statements that test each function into their own functions in the test file like so:

{{< card code=true header="`test_sample.py`" lang="python" >}}
import sample  # We import the filename without the .py

def test_palindrome():
    assert sample.palindrome_check("kayak")  # the function should return True, giving "assert True"
    assert sample.palindrome_check("Kayak")
    assert sample.palindrome_check("moose") is False  # the function should return False, giving "assert False is False", which is True

def test_is_prime():
    assert sample.is_prime(1) is False
    assert sample.is_prime(2)
    assert sample.is_prime(8) is False

def test_reverse():
    assert sample.reverse_string("press") == "sserp"  # checking result for equality with expected
    assert sample.reverse_string("alice") == "ecila"
    assert sample.reverse_string("") == ""

# run the test cases when executing the file
if __name__ == "__main__": 
    test_palindrome()
    test_is_prime()
    test_reverse()

{{< /card >}}  


We say now that each of `test_palindrome()`, `test_is_prime()`, and `test_reverse()` is a ***test case***. We have three (3) test cases in one (1) unit test file.

Note the **naming convention**: all the test case functions begin with the string `test_`. This is a requirement of the developer tool in the next lab that will help us run multiple test cases even if one of them fails.

The block beginning with `if __name__ == "__main__":` allows us to run the tests by running the file. You *should not* see any output when you run the unit test because all of these `assert` statements should evaluate to True.

## Diversifying our test cases
One ***test case*** for each function in your program code is where you should start. However, we often want more than one test case per program code function. Why?

Consider why we have multiple simple `assert` statements. Suppose we have the following valid assertion: `assert sample.is_prime(1) is False and sample.is_prime(2)`. Now, suppose this assertion failed due to a bug in our program code. The bug could either be with the logic of dealing with the input `1` or `2`. We put our checks in separate `assert` statements so we know *precisely* which input caused an error in the program code.

The same strategy applies when unit testing program code. 

### Program paths
A ***program path*** is a sequence of instructions (lines of code) that may be performed in the execution of a computer program. [[ISO/IEC/IEEE 24765](https://www.iso.org/standard/71952.html)] Take a look at `is_prime()` in `sample.py`:

```python {linenos=true, linenostart=5}
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```


`is_prime()` has three unique program paths:
1. Giving the input `1` executes lines 5, 6 and **7**.  This path (5,6,7) deals with special cases where our input is ≤ 1. One (1) itself is not prime, and neither are 0 or negative numbers by definition.
1. Giving the input `4` executes lines 5, 6, **8, 9, and 10**. This path (5,6,8,9,10) accounts for numbers > 1 that *are not* prime.
1. Giving the input `5` will execute lines 5, 6, **8, 9 and 11**. This path (5,6,8,9,11) accounts for numbers > 1 that *are* prime. The input `3` is a special case of this that does not include line 8.


### Path testing
Let's group `assert` statements that test "a particular program path" or "a particular requirement" (see the [test case definition](#organizing-test-code-into-test-cases)) into separate test cases. Change `test_is_prime()` to the following:


{{< card code=true header="`test_sample.py`" lang="python" >}}
def test_is_prime():
    assert sample.is_prime(2)
    assert sample.is_prime(8) is False
    assert sample.is_prime(2719)
    assert sample.is_prime(2720) is False

def test_is_prime_special_cases():
    assert sample.is_prime(1) is False
    assert sample.is_prime(0) is False
    assert sample.is_prime(-1) is False
{{< /card >}}

These test cases both verify `is_prime()` but examine different *program paths*. 

`test_is_prime_special_cases()` tests path #1 (previous subsection). We know something is wrong with the part of our algorithm that handles the special case of integers ≤ 1.

`test_is_prime()` tests paths #2 and #3. WE know something is with the part of the algorithm that checks if the input is divisible by a potential factor if that test case fails. 

The ability to pinpoint *where* the algorithm is failing is very useful to the developer when they go to debug. Especially when you have many test cases and hundreds of lines of program code.

Some functions only have one program path, and so one test case may be sufficient.

## Your testing strategy
Writing separate test cases for each program path or requirement is a testing strategy. But, it can be hard to know *how much* to identify the program paths or to know how many tests are "enough".

For now, **start with one test case per program function.**

Then ask yourself, "are there *sets* of input where the program behaves differently than for other inputs?" If so, divide your test case to separate those input sets. In `is_prime()`, the program behaves differently if you give it inputs ≤ 1 vs. inputs > 1 that are prime vs. inputs > 1 that are not prime.

We will discuss how to analyze a program to create a good test strategy in future lessons, as well as quantify *how good* our tests are.

### Exercise
Our `test_is_prime()` has lumped together the program paths where the number *is* prime and the number *is not*. Reorganize this test into two test cases: one for each program path. Write one test case asserting only prime numbers ≥ 1, and the other only non-prime numbers ≥ 1.

## Knowledge check
- Question: In test code, a single function is called what?
- Question: How many **program paths** will a function with a single `if-else` statement have?
- Question: What is a **program path**?
- Question: Conceptually, what is a ***test case***?
- Question: Besides generally being more organized, why do software developers want to split up their tests into multiple test cases?
- Question: Suppose you have a program file that defines the functions `foo()` and `bar()`. How many test cases should you have at a minimum in your test code? What should they be named?
