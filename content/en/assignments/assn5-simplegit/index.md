---
title: Assignment 5 - Simple Git
weight: 30
description: Practicing basic Git commands
---

## Objectives
- Practice the basic Git commands: `init`, `add` and `commit`.


## Setup

1. You must have completed the [Lab: Git and GitHub setup](../../labs/version-control/installing/).
1. Create a new directory named `git-calc/`.
1. Download [`calc.py`](calc.py) and put it in the `git-calc/` directory.
1. Create a new file named only `.gitignore` in the `git-calc/` directory. Note the `.` at the beginning! Paste in the following text:
   ```bash
   # This will ignore files we don't need but may show up.
   venv/
   .venv/
   __pycache__/
   .idea/
   .DS_Store
   .vscode/
   ```
1. Open the `git-calc/` directory in PyCharm.



## Instructions
Run `calc.py` and to try it out with the options. You are going to add to the functionality.


Follow the style in the code. Do not worry about unit testing or error handling for this assignment. 

1. Run the `git init` command to initialize a new local repository.
1. Add a "power" option to raise one number to the power of another. Add it to the user menu. Add and commit your changes using git *with a meaningful commit message*.
1. Add a "logarithm" option that computes the `log(x, base)`.  Import the standard [`math` library](https://docs.python.org/3/library/math.html) and use the [`log()`](https://docs.python.org/3/library/math.html#math.log) function. Add it to the user menu. Add and commit your changes using git *with a meaningful commit message*.
1. Add one more mathematical operation of your choice. Again, add and commit your changes using git *with a meaningful commit message*.
1. All pre-existing options must continue to work, including "Quit".


## Rubric
Partial credit is not awarded for these items: all or nothing.
- (5 pts) Version history (`git log`) of submission shows a minimum of three new commits.
- (5 pts) Commit messages  are *meaningful*, *concise*, and *accurate* messages. 
- (5 pts) *All* options (original features + your additions) correctly work in the final commit.


## Submission due October 15
Zip/compress your `git-calc/` folder and upload the zip to the Canvas assignment page.





