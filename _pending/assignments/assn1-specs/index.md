---
title: Assignment 1 - Problem Statements
weight: 5
description: Practice creating a well-defined problem statement, and then implementing it.
---

> "Programming all too often begins without a clear understanding of the problem."
> 
> &ndash; J.M. Yohe[^1]


A good ***problem statement*** has the following structure in clearly-labeled sections[^2]:
1. Concise and precise statement of the problem.
   - Provide a summary of the problem. What is the problem you are trying to solve?
   - If appropriate, include relevant calculations or computations provided by your customer/boss/instructor.
   - *Do not* write the precise algorithm you will implement.
2. Clearly specified  *input format*. Input includes function arguments, file contents, or user console input. What does the data look like? For example:
   - three integer values separated by spaces on a line.
   - each bank record consists of the id number (integer), a name (string), and current balance (a float). These values are read from a file. Each line corresponds to a single record, and the values are separated by commas.
   - the user will be prompted to enter their first name, last name, and date of birth in the console as strings.
3. Clearly specified *output format*.
   - Output could be printed to the screen, text written to a file, or the values returned from a function.
   - As with input, describe what does this data look like?
4. Define exceptional conditions, e.g., things you should check for (like invalid values) and what you should do if they occur. For example:
   - The user enters a float when an integer is expected. What will you do?
   - The user provides a filename to read that doesn't exist. What will you do?
5. Sample input. This needs to be as exact and precise as possible. For example (matching #2 above):
   - `22,56,999`
   - `850123456,"Bob Smith",500.00`
   - `First name: "Bob", Last name: "Smith", DOB: "01/02/2004"`
6. Sample output. Exact and precise as possible as with the sample input.

[^1]: Yohe, J. M. (1974). An Overview of Programming Practices. ACM Computing Surveys (CSUR), 6(4), 221–245. 
[^2]: Ledgard, Henry F. (1975). *Programming Proverbs*. Hayden Book Co.

## Part A - write a problem statement


This will be completed in class.

**With a partner (required):** Write a problem statement using the best practices described in class. Here is the high-level problem:

> Write a program where the user enters three side lengths and the program says if they can form a triangle or not. This is the [Triangle Inequality Theorem](https://en.wikipedia.org/wiki/Triangle_inequality).
>
>
>Suppose we label the numbers `a`, `b`, and `c`. They can form a triangle if:</br>
`a + b ≥ c`, and<br/>
`b + c ≥ a`, and<br/>
`a + c ≥ b`.
>
> The user will input the values from the console. The three sides should be entered separately. Your program must accept the input values, produce a result, and then terminate. You may include a loop that allows the user to repeat the process multiple times before quitting. It's up to you.

Use this [plain text template](spec.txt) to write your problem statement. You must save it as a plain `.txt` file, not Word or anything else.
<!-- 
### Grading 
You and your partner have complete freedom in specifying your problem so long as the following criteria are met:
- It accepts user input and produces output for the user.
- It correctly calculates the result.
- The statement identifies at least two *exceptional conditions* and how they will be handled. -->


### Grading
I expect that each `spec.txt` will be different, and that is okay. I am looking for the completion of the problem statement sections that address the functionality required.

#### Rubric
- **(6 pts)** All elements of the template are completed. Sample input values and sample output values must include *normal* and *exceptional* behaviors.
- **(1 pts)** At least two exceptional conditions are specified.
- **(3 pts)** Correct spelling and grammar.



### Submission due by Thursday, February 6
Each partner submits their team's `spec.txt` to the [Canvas assignment 1.A page](https://uncw.instructure.com/courses/90540/assignments/1268124). 


## Part B - Implementation

**Individually** create `triangle.py` and implement the problem you specified in `spec.txt`.

The goal is to warm-up your Python skills, and to see how the implementations of two people working from the same spec will be different. 

**You may not share code under any circumstances**. Getting answers to simple Python questions from your peers is fine. Review the Syllabus section on [Collaboration and Cheating](https://uncw.instructure.com/courses/83039/assignments/syllabus#collaboration) for what is allowed and not allowed. If in doubt, ask me -- I promise I won't be mad if you ask.

### Grading

You are graded on the correctness of your code, not the correctness of the `spec.txt`. If you discover an error in your `spec.txt`, you may communicate it with your partner. 

#### Rubric

- **(10 pts)**: Functionally correct implementation that (a) accepts user input according to the format in your spec, and (b) produces correct output as to whether the input can form a triangle or not for several valid input values.
- **(5 pts)**: The program detects and handles at least two exceptional conditions you specified in `spec.txt`. "Handling" means it does not crash with an exception, but terminates or continues gracefully.

You will receive 0 points if your program does not run due to syntax errors or does not complete under "normal" conditions.

### Submission due by Sunday, February 9
Submit your `triangle.py` file to the [Canvas assignment 1.B page](https://uncw.instructure.com/courses/90540/assignments/1268125).