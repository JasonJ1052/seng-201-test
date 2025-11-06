---
title: Assignment 5 - Simple Git
weight: 30
description: Practicing basic Git commands
---

## Objectives
- Practice the basic Git commands: `add` and `commit` and, if necessary, `reset`
- Navigate to a remote GitHub repository and `push` code to it.


## Setup
1. You must have completed both [Lab: Git and GitHub setup](../../labs/version-control/installing/) and [Lab: GitHub CLI setup](../../labs/version-control/gh-cli/) prior to starting this assignment.
2. Click this link: https://classroom.github.com/a/YpAD2CPJ
3. Select your name on the "Join the classroom" page and continue.
4. Select "Accept this assignment" on the next page. You will see a confirmation screen similar to the one below. Refresh the page if you don't see it.
   {{<figure src="confirmation.png" alt="Classroom assignment confirmation">}}

5. Click on the link to your assignment repository. You will see a GitHub remote repository containing a README.md file:
   {{<figure src="classroom-repo.png" alt="starting point of the repo for the assignment">}}
6. Open a Terminal open with your `seng-201/` as the working directory. Run the commands below separately, replacing `YOUR_REPOSITORY_URL` with the URL of your assignment repository from the previous step. 
   ```bash
   git clone YOUR_REPOSITORY_URL  # copy the code from GitHub to a new local repostiory
   ```
7. In the Terminal, type `cd YOUR_NEW_DIRECTORY` to change into the project directory. It will be something like `cd git-calc-LASTNAME`
8. Run the command `git checkout -b more-options`

This will create a new subdirectory named `git-calc-YOUR_NAME` that is a "clone" of a Git repository I created. The `checkout -b` command creates a new branch, which will be explained in the future.

Open the `git-calc` directory in your IDE. You will see two files, `calc.py` and `.gitignore`. You will do all your work in `calc.py`.



## Instructions
Run `calc.py` and to try it out with the options. You are going to add to the functionality.


Follow the style in the code. Do not worry about our design rules, unit testing, input validation, or error handling.


1. Create a ***separate commit*** with a brief, meaningful message for each option below. You must have **at least two new commits** to the `more-options` branch:
   1. Add a "power" option to raise one number to the power of another. Stage and commit it.
   1. Add a "logarithm" option that computes the `log(x, base)`.  Import the standard [`math` library](https://docs.python.org/3/library/math.html) and use the [`log()`](https://docs.python.org/3/library/math.html#math.log) function.
   5. The options must be incorporated into the user menu.
1. All pre-existing options must continue to work, including "Quit".
4. Run the command `git push` to send your completed code to the remote (GitHub). 
   - Verify that your changes are in GitHub by visiting your remote repository's web URL and changing the `main` dropdown to say `more-options`.


## Rubric
Partial credit is not awarded for these items: all or nothing.
- (5 pts) Version history (`git log`) of submission shows a minimum of two new commits (in addition to my initial commit) with are *meaningful*, *concise*, and *accurate*. Commit messages are short summaries of the changes.
- (5 pts) Your remote repo's version history show that you contributes a minimum of two versions on the `more-options` branch.
- (5 pts) *All* options (original features + your additions) correctly work in the final commit.


## Submission due April 13
Your code is pushed to your GitHub repository.





