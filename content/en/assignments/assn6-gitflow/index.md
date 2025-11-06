---
title: Assignment 6 - GitHub Flow
weight: 40
description: Properly using Git to collaborate on teams
---

## Objectives
- More practice with Git branching and merging
- Practice of a proper Git workflow to handle merge conflicts properly in a team environment

## Interactive class
The Setup, Part A, and Part B of this assignment were worked on in an interactive class. 

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/DSycGqIMGZc?si=vhfTNqSkqmRuAbvY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Setup
1. You must have completed [Lab: GitHub CLI setup](../../labs/version-control/gh-cli/) prior to starting this assignment.
2. Run the command `git config pull.rebase merge`
2. Click this link: https://classroom.github.com/a/SIP7ZMX7
3. Teams:
    - **The first teammate**: Create a name like "alice-bob" using your first names.
    - **The second (and third) teammate**: Join the team your partner made.
4. Finally, accept the assignment.
5. Click the link to your team repo on the confirmation page.
6. You will see a repo like the following:
    {{<figure src="assn6-repo.png" alt="Assignment 6 repo" width="320">}}
7. `git clone` the repository to your computer, and open the directory in PyCharm.
8. Configure `pytest`:
    - If you do not have a `.venv/` folder, click the bottom right of PyCharm where your Python version is listed. Select `Add New Interpreter -> Add Local Interpreter`, then hit Okay on the pop-up.
    - Open an Integrated Terminal window in PyCharm.
    - Run `pip install pytest pytest-cov`


<mark>**PAUSE HERE and wait for the instructor**</mark>

## Part A - race to `main`
1. Run `main.py`, which won't do much, but may create some additional files in your workspace.
2. You should be on the `main` branch. Add a comment with *only your name* to the top of `main.py` in a comment, e.g., `# Alice Bobberton`.
3. Stage, commit, and push the change. Some of you will not be able to... 
 
<mark>**PAUSE HERE and wait for the instructor**</mark>



What happens? How do you fix the problem?
1. The partners need to pull, resolve the conflicts, add, commit, and push the changes.
2. Make sure that each partner has added, committed, and pushed their name.
3. Once done, all partners `git pull` the main branch. 

<mark>**PAUSE HERE and wait for the instructor**</mark>

Committing to the same branch in a remote repository is a race. Two, three, five, or 10 people committing to the same branch is chaos.

## Part B - proper git flow

### B.1 - Group discussion
1. Make sure that `main.py` in the remote repo's `main` branch contains all team members' names.
2. Make sure everyone's local `main` branch is up to date with the remote `main` branch by running `git pull`.
3. Open `string_stuff.py` and *discuss*:
   1. Who will implement `reverse_words()`
   2. Who will implement `count_vowels()`
   3. (If you have a 3-person team): who will implement `is_palindrome()`
   4. You do not need to edit `main.py` for this assignment.
1. Each person creates a ***new feature branch*** to work in. Use a descriptive branch name reflective of the *work you will be doing*, not your name.

<mark>**PAUSE HERE and wait for the instructor**</mark>

### B.2 - Individual work

1. Each person implements their function **in their branch -- not in the `main/master` branch**. Talk to and help one another. You can use internet resources, but cite them in a comment if you do.
   - All of your work should be in `string_stuff.py`
   - Do not worry about writing test code yet.    
2. Remember to do small, incremental commits when appropriate.
3. Run `main.py` and manually test your work.
4. Stage, commit, *and* `push` your changes to the remote. Pay attention to the console because you may have to run a variant of the `git push` command.

<mark>**PAUSE HERE and wait for the instructor**</mark>

#### Integrate your work with `main`

Now it is time to integrate your changes into `main`. It will not be painless as there is still a race, but there is a right way and a wrong way to do it. We already did the wrong way. Here is the right way:

1. `git switch main`
2. `git pull`: make sure you have the latest changes from the `main` branch in case someone else committed something.
3. `git switch <your-branch>`
4. `git merge main`: this merges the changes from `main` into your branch. 
5. Resolve any conflicts in your branch and commit the changes to your branch.
6. `git switch main`: now we switch back to `main`
7. `git merge <your-branch>`: bring the changes from your branch into main. This should be smooth because you already resolved merge conflicts between your-branch and main.
8. `git push`: now push the updated `main` to the remote.

This flow will help ensure that `main` is "good, clean, code". Merge conflicts will usually only happen in your branch, which is where you want to deal with them. 

If each person completes steps 1-7 before anyone else pushes to main, the process will be smooth. If `main` changes while you are in the middle of these steps, you will not be allowed to push in step 7. You will have to pull `main` and resolve the merge conflicts either in `main` or in `your-branch`.

### Good communication helps
A simple heads-up to your partner of, "Hey, I just pushed some changes to main. Make sure to integrate them into your branch" goes a long way. 

And "I'm getting ready to integrate to main. Please don't push anything yet" also helps.

### B.3 - Integrate group work
Ensure that everyone's changes to their branches are integrated into the `main` branch using proper merging. Make sure `main.py` runs and works properly for the completed functions.

## Part C - for homework due Monday
Part C will add tests to the project to give you some more practice writing test cases in addition to practicing your Git workflow. Code really isn't complete until it is tested, and developers write unit tests for the code they implement.

### Preparation
1. Complete Part B first.
2. Ensure that your `main` remote branch is up-to-date, correct, and "good code".
3. Ensure that each partner has checked out and pulled the `main` branch updates.
4. Ensure that each partner has merged `main` into their branch. 

At this point, all branches and main should be at the same version, so everyone is starting from the same place.

### Instructions
You will write `pytest` unit test cases in `test_string_stuff.py` for each of the functions. Refer to the [testing labs](../../labs/testing/) as necessary. Work with your partners. 


- **Individual work**
   - The partner who wrote a function also writes the tests for that same function in `test_string_stuff.py`.
   - Each partner must write a minimum of two test cases: (1) testing "normal" input, (2) verifying the assertions are raised correctly.
   - Commit and push your work to the same branch you worked on while implementing the function, not to `main`.
   - You do not need to write test cases for `main.py`.
- **Group integration**: Follow the Git Flow from your worksheet to integrate your work into `main`. Each person:
   1. `git switch main`
   2. `git pull`: make sure you have the latest changes from the `main` branch in case someone else committed something.
   3. `git switch <your-branch>`
   4. `git merge main`: this merges the changes from `main` into your branch. 
   5. Resolve any conflicts in your branch and commit the changes to your branch.
   6. `git switch main`: now we switch back to `main`
   7. `git merge <your-branch>`: bring the changes from your branch into main. This should be smooth because you already resolved merge conflicts between your-branch and main.
   8. `git push`: now push the updated `main` to the remote.
- **Finishing up**:
  - Make sure that all functions and tests work in the `main` branch.
  - Ensure that you have [total branch coverage](../../labs/testing/coverage/#using-pytest-cov-to-compute-test-coverage) of the functions you implemented in `string_stuff.py`.
    - You do not need to commit any coverage information to your repo. The `.gitignore` file should be ignoring these files, and that's okay!
  - Make sure that your "final" version of `main` is pushed to GitHub.


## Assignment 6 Rubric
- (15pts) `git log` history shows multiple commits to each partner's branch and integration into main following the prescribed Git Flow
- (15pts) Final version of `main` contains functionally correct implementations and test cases achieving 100% branch coverage of all functions implemented in `string_stuff.py`.


## Final submission due Sunday, October 26
You will push all your branches and finished code to GitHub.
