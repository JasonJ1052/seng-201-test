---
title: Assignment 2 - Unit testing
weight: 10
description: Practice implementing and testing simple functions.
---


## Objective
The goal of this assignment is to gain more practice with the tools we have used so far, including implementing a unit test with `pytest`.

## Setup
1. Create a new project directory named `assn2/` or something similar.
1. Download [`grades.py`](grades.py) to the `assn2/` folder



## Instructions
The assignment is to be completed **alone**. Refer to the Syllabus for policies on what is allowed and what is not.




### Implementation
1. Put your name at the top.
1. You ***may not*** change the `main()` function in any way.
1. You ***may*** add to the `__main__` block to help test if you want.
1. Complete the functions `calculate_average()` and `determine_grade()` according to their docstring descriptions:
   - The docstring tells you what the function must do, the parameters passed to it, the type that must be returned, and any exceptions you need to raise. 
   - You ***may not*** add any parameters, change the return type, or add to or alter the exceptions required.
   - You must not call `print()` or `input()` from these functions. 


### Testing
1. Create a test file for `grades.py`.
1. Put your name at the top of your test file in a comment.
1. Write one or more test cases in your test file for `calculate_average()`.
   - The test case must invoke `calculate_average()` by providing a list, e.g., `calculate_average([1,2,6])`. Use `assert` statements to ensure the computed value is correct. You should have multiple asserts to check the calculation.
   - You must write test cases that check the *exceptional conditions* that raise value errors. Refer to the lab on [testing for exceptions](../../labs/testing/test-exceptions/).
1. Write one or more test cases in your test file for `determine_grade()`. This function does not knowingly raise exceptions, so you do not need to test for them. Test only for expected output given an input.
1. Run your test file using [pytest](../../labs/testing/pytest/).

## Rubric
- **(15 pts):** Your implementation of `calculate_average()` passes my test cases, which exercises all the details of the function's docstring.
- **(10 pts):** Your implementation of `determine_grade()` passes my test cases, which exercises all the details of the function's docstring.
- **(15 pts):** Create a control flow graph (CFG) for each of your implementations of `calculate_average()` and `determine_grade()` following the rules from class.
  - You may use an online flow chart tool such as [draw.io](https://www.draw.io), [Canva](https://www.canva.com), or [Lucidchart](https://www.lucidchart.com).
  - You may draw your CFG on paper and take a picture. Ensure it is legible.
  - In both cases, export your CFG image to a PDF to submit to Canvas. 
- **(25 pts):** Your test file can be run using `pytest`, has multiple test cases, and thoroughly tests the parameters, returns, computations, and exceptions raised of the functions as specified by their docstrings.
- Your assignment will receive a score of 0 pts for any of the following:
   - `print()` or `input()` statements in `calculate_average()` or `determine_grade()`
   - Changing `main()` in any way
   - Changing the method signature of `calculate_average()` or `determine_grade()`
   - Your code or tests fail due to syntax error.
   
## Submission due Sep 23
Submit your `grades.py`, your `test file`, and your CFG PDF file to the [Canvas assignment page](https://uncw.instructure.com/courses/99267/assignments/1398306).
 
