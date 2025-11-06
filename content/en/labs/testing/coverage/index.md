---
title: Test coverage
description: Computing an objective measure of test quality.
weight: 30
---

## Before you start
You must have completed the lab on [Testing for exceptions](../test-exceptions/).

## Motivation
Software engineers need some measure of the *quality* of the tests they write. This is not a simple question to answer.
- Does a good test find bugs? Hopefully, but also, we should be writing our code to not have bugs!
- Do we count how many lines of test code we have? Is it more than source code? Maybe, but that doesn't mean we are testing the right things. 
- Do our tests check independent things in the code? How can we determine that automatically if so?

*Measuring* test case quality is not straightforward, but there is one generally agreed-upon measure used as a baseline: *test coverage*.


## Test coverage
***Test coverage*** is a measure of how much of source code is executed when the tests run. There are three measures of "how much":
1. ***Line coverage*** or ***statement coverage*** is the percentage of source lines of code executed by your test cases. We do not include test code lines when counting the percentage of code.
2. ***Branch coverage*** is the percentage of program paths executed by your test cases.
3. ***Conditional coverage*** is the percentage of Boolean conditions executed by your test cases.


Consider the following (very poorly designed and implemented) code snippet:
```python{linenos=true}
def authorize(is_authenticated, user_id, caller):
    if is_authenticated is True or (user_id.startswith('admin') and caller == "privileged"):
        return True
```
Now consider the following test case:
```python
def test_authorize():
    assert my_module.authorize(True, "bob", "privileged") is True
```

- This test case has 100% line coverage because all lines of code are executed.
- This test case has 50% branch coverage because only one program path is executed: the path where the `if-statement` evaluates to True. 
- This test case has 33% conditional coverage because only one boolean conditional is checked (`is_authenticated is True`), but the other expressions `user_id.startswith('admin')` and `caller == privileged` are not.
 
**Line coverage** is the least precise, and **conditional coverage** is the most precise. 

Test coverage is computed over the union of all source lines, branches, and conditions executed by our test cases. So we can easily write additional test cases that, collectively, reach 100% statement, branch, and condition coverage.

You want to target 100% condition coverage, but achieving 100% of any coverage can be challenging in a real system. Exception handling and user interface code in complex systems can be hard to test for a variety of reasons. 

In practice, most organizations aim for 100% line coverage as a target.

## Using `pytest-cov` to compute test coverage
Most test frameworks, like `pytest` and `Junit` (for Java), also have tools for computing test coverage. Manually computing these measures would be too tedious. These tools compute line coverage, but not always branch coverage, and almost never condition coverage because of the technical challenges of automating that calculation.

We installed the `pytest-cov` tool when we installed `pytest`. Refer to [the instructions for installing pytest and pytest-cov](../pytest/#installing-pytest-with-pip)
Open a Terminal in the directory where you were working on your unit testing examples. Run the following:

### Running `pytest-cov`
Run the following command from your Terminal in the directory with `sample.py` and `test_sample.py` from the previous labs.

`pytest --cov .` - This tells pytest to run tests in the current directory, `.`, and generate the coverage report. You should see something similar to the following:
```bash
============================================================= test session starts ==============================================================
platform darwin -- Python 3.12.2, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/laymanl/git/uncw-seng201/content/en/labs/testing/coverage
plugins: cov-5.0.0
collected 4 items                                                                                                                              

test_sample.py ....                                                                                                                      [100%]

---------- coverage: platform darwin, python 3.12.2-final-0 ----------
Name             Stmts   Miss  Cover
------------------------------------
sample.py           23      6    74%
test_sample.py      23      3    87%
------------------------------------
TOTAL               46      9    80%


============================================================== 4 passed in 0.03s ===============================================================
```

`pytest` executes your tests as well, so you will see test failures outputted to the screen. Note that failing tests can lower your test coverage!

- The general format for the command is `pytest --cov <target_directory>`
- To get **branch coverage**, run the command `pytest --cov --cov-branch <target-directory>`

### Generating a coverage report
You can also generate an HTML report with `pytest --cov --cov-branch --cov-report=html <target-directory>`. This will create a folder named `htmlcov/` in the working directory. Open the `htmlcov/index.html` file in a web browser, and you will see an interactive report that shows you which lines are and are not covered.

{{< figure src="coverage_report.png" alt="A sample coverage report viewable in a web browser" width="640">}}


## Knowledge check
- Test coverage is a measure of how much _________________ is executed when the __________________ runs.
- Explain the difference between ***branch coverage*** and ***conditional coverage***. 
- Give an example of a function and a test case where you have 100% **branch coverage** but <100% **conditional coverage**.
- (True/False) Branch coverage is more precise than statement coverage.
