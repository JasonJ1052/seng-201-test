---
title: Week 3
weight: 5
description: Reinforcing selection, iteration, and function calling.
---

## Instructions
For all of the following, write both the function and some code that calls and tests the function.

<mark>Complete the following without using ANY outside aid.</mark> If necessary, refer only to the python `help()` command or the official documentation at <https://python.org>.

Use [PyCharm](../../pycharm-install/) to complete this task. I know that PyCharm has a built-in AI Assistant. I strongly recommend that you disable it. You are going to be quizzed on these skills in class, and you will not be allowed to use any outside assistance.


1. Write a function named `multiply()` with two parameters, `a` and `b`, that **returns** the result. 
    - Verify that both `a` and `b` are integers. 
    - Return nothing if either `a` or `b` is not an integer.
1. Write a function named `divide()` with two parameters, `a` and `b`, that **returns** the result of `a` / `b`. 
    - Verify that both `a` and `b` are either integers. 
    - Return nothing if either `a` or `b` is not a number.
    - Return nothing if `b` equals `0`.
1. Write a `calculator` function
    - The function must contain an "infinite" while loop that does the following until the user chooses to 'exit'.
    - Prompt the user to make a choice of either `multiply`, `divide`, or `exit`.
    - Do not allow or handle an invalid choice.
    - If the user picks `exit`, the program must end.
    - Prompt the user to enter two values, `a` and `b`.
    - Based on their choice, call either your `multiply()` or `divide()` function.
    - If either `multiply()` or `divide()` returns nothing, print an error message. 
    - Otherwise, print the result in the format, e.g, `4 * 5 = 20` or `2.4 / 1.2 = 2.0`.
    - Round the `divide` result to the tenths place using the built-in `round()` function when printing.



## Submission
Submit your `.py` file to Canvas for a check. You are not graded on completeness or correctness -- this is for learning and feedback.

## Key Skills
- Function definition: parameters and returns.
- Logical selection using `if`.
- Type checking using `isinstance()`.
- Functions calling functions.