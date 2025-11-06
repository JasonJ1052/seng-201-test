---
title: Assignment 3.b - Meteoric Design, Implementation, and Test
weight: 20
description: Apply low-level design rules to implement and test your application.
---


## Part B - design, implementation, and test
You will work with your partner(s) to design, implement, and test your solution to [Assignment 3, Part A](../assn3-design/). Download [`meteoric.py`](meteoric.py) and [`test_meteoric.py`](test_meteoric.py) to your `assignment3/` folder. 

You must identify a way to communicate and collaborate on the assignment:
1. Meeting in person to work together
2. Chatting and sharing code over a tool like Discord, Slack, or Teams. You may use the [class Slack workspace](https://join.slack.com/t/drlaymansfall-a7l7865/shared_invite/zt-2o004p6eb-v0TO387qJeNx_NzfaKOjTA).
1. Emailing back and forth and texting.

**You may only collaborate with your partner(s). You will submit one final solution.** Review the [section of the course policies](https://uncw.instructure.com/courses/83039) on collaboration, cheating, and personal proficiency. 

All partners must contribute equally to the assignment. Design will be done collaboratively in class. Implementation and testing tasks must be divided equally among the partners. Make each person responsible for implementing *and* testing part of the solution.

## Design - in class

In class on October 17, **discuss** the organization of your code with your partner(s). You must come to an agreement on the design. 

Follow the [6 low level design rules](../../labs/design/example/):
>    1. Separate input/output logic from business logic.
>    2. Functions should have a single responsibility.
>    3. Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise.
>    4. Raise specific errors and define your own if needed.
>    5. Avoid magic literals.
>    6. DRY (Don’t Repeat Yourself) and the Rule of Three.

Rules 3-4 require your judgment. There are many ways to solve this problem while adhering to the design rules. Be prepared to justify your design decisions!

You may evolve your design during Implementation and Test.

**By the end of class**, show the instructor:
- The function signatures you have decided on in `meteoric.py` 
- Comments or docstrings that (i) define each function, **and** (ii) which partner is responsible for implementing and testing the function.


## Implementation
1. Put your names at the top of `meteoric.py` in the module docstring.
1. You may create classes and files and use imported libraries, but these things are not necessary.
2. You may evolve your design as you go along. This is a natural part of implementation.
3. You are free to modify the provided code, including `load_data()` code. 
4. You may use a Python implementation of the [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) from the web. If you do, add a comment to the code containing a link to the website.
5. Add docstrings following our [conventions](../../labs/style-and-documentation/documenting/) to any functions, classes, and files you create. Additionally, identify the partner primarily responsible for implementing and testing each function.
6. The code must adhere to the [PEP8 coding conventions](../../labs/style-and-documentation/conventions/) discussed in class. You are free to use a Visual Studio Code extension that helps you achieve compliance.


## Testing
1. If you are a WSL or Linux user, [set up pytest for the project](https://llayman.github.io/seng-201/labs/testing/pytest/#installing-pytest-with-pip).
2. Add test cases to `test_meteoric.py`. Any additional source files you create must also have a `test_*.py` test.
3. All test cases must run from the CLI with `pytest`.
4. Use `pytest --cov --cov-branch --cov-report=html` to [generate a branch coverage HTML report](../../labs/testing/coverage/) in your project directory.
5. You must achieve 90% branch coverage in all source files ***except*** for `main()`.


## Rubric
- (5pts) [PEP8 coding conventions](../../labs/style-and-documentation/conventions/) followed
- (5pts) [Docstring conventions](../../labs/style-and-documentation/documenting/) followed for modules (files), classes (if any), and functions.
- (25pts) User commands are correctly implemented, including exception handling of user input errors.
- (10pts) Adherence to our [6 low level design rules](../../labs/design/).
- (15pts) Multiple test cases with proper [test structure](../../labs/testing/organizing/) for your source code. `pytest` branch coverage HTML report demonstrating &ge;90% branch coverage of all source code except for `main()`.


## Submission due Oct 21
Upload anything `.py` files from your project directory to [Assignment 4 on Canvas](https://uncw.instructure.com/courses/83039/assignments/1243174).