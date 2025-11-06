---
title: Assignment 6 - Branching and Merging
weight: 35
description: Practicing branching and merging in git
---

## Objectives
- Practice with Git branching and merging

## Instructions
You will continue to work in the `git-calc` project.

### Part A: Merge your work into `main`

In the previous assignment, we created a branch called `more-options` and committed your changes there. Time to merge those changes into the `main` branch.

1. Checkout the `main` branch and use the `merge` command to merge your `more-options` branch into `main`.
2. Draw a sketch of your branch history *after completing the merge* in a style similar to the example below [from our labs](../../labs/version-control/git-branching/). Use `git log` to help put it together.
   1. Clearly mark the `main` and `more-options` branches and the position of the HEAD.
   2. Take a picture or draw the history in a file. Put the file in your `git-calc/` directory, stage it, and commit it to `main`.

{{< figure src="../../labs/version-control/git-branching/feature-1-v2-concept.jpg" >}}

### Part B: Resolving merge conflicts
I have created another branch, `rand`, that adds random number generation to `calc.py`. Unfortunately, this will generate [merge conflicts](../../labs/version-control/merge-conflicts/) with your changes.

1. Make sure `main` is the active branch.
2. Run `git merge origin/rand`
3. You must resolve the merge conflicts correctly, meaning:
   1. All of your new options still work.
   2. My random number generation option works.
   3. The user menu and all logic is updated to include all options and quit properly.
4. Manually run `calc.py` and check all the options. 
5. Stage and commit to `main` once the merge conflicts are resolved.
6. Draw a second sketch showing your current branch history. 
   1. Clearly mark *all three* the branches and the position of the HEAD.
   2. Take a picture or draw the history in a file. Put the file in your `git-calc/` directory, stage it, and commit it to `main`. You can combine it with the previous picture into one file if convenient.

## Rubric
Partial credit is not awarded for these items: all or nothing.
- (5 pts) Two drawings showing correct Git history.
- (5 pts) Version history of submission shows:
  - a minimum of two commits to the `more-options` branch
  - a merge commit on the `main` branch incorporating the changes from the `rand` branch
- (5 pts) *All* options (original features, your additions, and random numbers) correctly work in the final commit.


## Submission due April 27
Zip the *entire* `git-calc/` directory and upload it to Canvas, which will include the hidden `.git/` directory containing the local repository.







