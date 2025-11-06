---
title: Branching and Merging, Part 1
weight: 20
description: Working concurrently
---

## Class video

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/nPYJe5wY7RU?si=ctAtbnoY9gRHRcKq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Introduction

One of Git's main features is ***branching***: the ability to create parallel timelines in version history, and then merge them together later. 

{{< figure src="git-branches.jpg" alt="A simple Git branching model">}}

The circles in the illustration represent versions. The lines indicate different branches. We will build a similar diagram below while introducing branching concepts.

Why branching? It allows version histories to be a little dirty, or only incrementally complete. Then we share when we're happy and done.

This feature is essential for working on a team, and also by yourself to preserve a "clean" main branch while updating functionality in parallel.

### The active branch

Git has a notion of the ***active branch***, which is the branch you are currently committing to. So far, you have only been committing to the `main` branch in our examples.


### The `main` branch

Let's create a new project:
1. Create a directory `git-branching` in your `seng-201/` directory. 
2. Change into the `git-branching` directory and run `git init` to initialize a new Git repo.
3. Create the file `app.py` with the following content:
    ```python
    def main():
        print("Welcome to the main branch!")

    if __name__ == "__main__":
        main()
    ```
4. Run `git add .`
4. Run `git commit -m "first version"`



Every Git repository has a ***default branch*** called `main` (or `master` prior to July 2020). This branch is created for you when you run `git init`.


In the Terminal window, you may see the text `(main)` in the command prompt indicating that `main` is the active branch:

{{< figure src="main-active-terminal.png" alt="main branch showing active in the terminal" >}}

Your IDE also displays the active branch in the bottom left:
{{< figure src="main-active-code.png" alt="main branch showing active in the Visual Studio Code footer" >}}

Most software groups treat the `main` branch as the place where only robust, finished, shippable code lives. You are not allowed to commit directly to `main` in many organizations. Instead, the expectation is that you work in a different branch and integrate with main when finished and approved.

Committing directly to `main` is fine for small personal projects that you don't expect anyone else to use or that won't live long. Most short class assignments fall into this category. 

But, you should use branches for any other scenario, even if working by yourself!

## What is a branch?

Remember how we said that the special variable `HEAD` in Git is a *pointer* or *reference* to a specific version in the commit history? Usually, the `HEAD` is pointing to the most recent version of the ***active branch***.

Branches, including the `main` branch, are additional named variables that point to a specific version. When you run `git init`, creates a named `main` variable that points to a specific version. When you make your first commit, `main` will point to the first version in your repository:

{{< figure src="main-v1-repo.jpg" alt="conceptual view of main and HEAD pointers after committing the first version" >}}

{{< figure src="main-v1-concept.jpg" alt="branch history after first commit to main" >}}



## To branch or not to branch

Before you create a branch, you must decide what to do with any ***unstaged*** and ***staged*** changes. 

When you create a new branch, un-committed changes (unstaged and staged) are brought into the new branch. This is often desirable. 

Suppose you start working on code and you realize "this is more complicated than I thought and going to take a lot of effort." You can move these changes to a new branch, and the version history of your current branch will be unchanged.

You may also want to save all your currently unstaged and staged changes to the active branch. You have three options:

1. If you have no changes in the working directory, then you're good to create a new branch.
2. Stage and commit changes if you want to create a new version in the active branch.
3. Create a new branch if you want your staged and unchanged changes to appear in the branch, but you want the old branch, e.g., `main`, to be unchanged for now.
4. You can also [undo those changes using `git reset` or something similar.](../git-undo/).

You decide what's best. 

## Creating a new branch

Run the command `git switch -c feature-1`. You will see something similar to:

{{< figure src="git-checkout-b.png" alt="checking out a new branch" >}}

You have created a new branch named `feature-1`, and you have set the *active branch* to `feature-1`. The `switch -c` command tells the `HEAD` to point to `feature-1`, which makes `feature-1` the active branch.

This means any committed changes will be saved to the version history of `feature-1` but *not* to `main`. Your workspace state looks like the following:

{{<figure src="git-checkout-b-repo.jpg" alt="HEAD and feature-1 now point to the first version" >}}

We have not yet committed a new version, so all three variables are pointing the first version.

<mark>**Remember:**</mark> Why do we want to use branches? It allows version histories to be a little dirty, or only incrementally complete. Then we share when we’re happy and done. This feature is essential for working on a team, and also by yourself to preserve a “clean” main branch while updating functionality in parallel

## Committing a new version to the branch

Change `app.py` to the following:
```python
def main():
    print("Welcome to the main branch!")
    feature_1()

def feature_1():
    print("Feature 1 activated!")

if __name__ == "__main__":
    main()
```

Add and commit the change:
```bash
git add app.py
git commit -m "Add feature 1 function"
```

Run `git log`, and you will see something like this:
```bash
commit 89c5985701b1a6b188d1c23fef3b0196dd17b34e (HEAD -> feature-1)
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Tue Oct 29 11:29:37 2024 -0400

    Add feature 1 function

commit e436c51cd2760e9ef0d49a65472a404044c2d3c0 (main)
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Tue Oct 29 11:19:05 2024 -0400

    first version
```
You are looking at the version history of the `feature-1` branch. Note that the history is based on the first version from `main`.

Conceptually, our branch history looks like this:

{{< figure src="feature-1-v2-concept.jpg" alt="Diagram showing 1 version in main, and 1 version in the feature-1 branch">}}

The local repository looks like this:
{{< figure src="feature-1-v2-repo.jpg" >}}

### A second commit
Let's make another change and commit it to the `feature-1` branch. Do the following the following code:

1. Replace `app.py` with the following:
    ```python
    import random

    def main():
        print("Welcome to main!")
        feature_1()

    def feature_1():
        print("Feature 1 activated!")
        print(f"Your random number is {random.randint(1,100)}.")


    if __name__ == "__main__":
        main()
    ```
2. `git add .`
3. `git commit -m "adding random number generation"`

We now have two new versions in our `feature-1` branch. Our repo and branch history look like this:

{{< figure src="feature-1-v3-repo.jpg" alt="repo state after committing another version." >}}

{{< figure src="feature-1-v3-concept.jpg" alt="branch history after committing another version." >}}

## Switching between branches

Run the command
`git switch main` to switch back to the `main` branch. Notice there is no `-b`.

**Question:** What happens to the code in your IDE?

You should see that the contents of `app.py` are replaced with the contents as they were in the first version. Here is the current state of the repo:

{{< figure src="checkout-main-repo.jpg" alt="checking out main again. Contents of files are replaced and the HEAD is moved" >}}

{{< figure src="checkout-main-concept.jpg" alt="checking out main again. HEAD now points to the last main version, but feature-1 is unaffected" >}}

Several things happened:

- `switch` tells `HEAD` to point to the same version as the `main` variable. This makes the `main` branch the *active branch* again.
- Git replaces the contents of the workspace with the files as they were at the `main` version.
- `feature-1` is unaffected. The version committed to `feature-1` is still in the local repository, so we can go back to the files at that version by checking out the `feature-1` branch. 
  
  
**Exercise**: Switch to `feature-1` to verify that all your changes have been saved in that branch. Switch back to `main` when you are done.

## Merging
Our repo reflects the most common use case for branches: you work on something in a branch for a while, you make it perfect, and you are now ready to bring your work into `main`. Remember, `main` should only contain clean, complete, "good" code.


You want now to ***merge*** your `feature-1` branch *into* the `main` branch. ***Merging*** is the process of combining the histories of two branches.


Run the following:
1. `git switch main` to ensure that `main` is the active branch.
2. `git merge feature-1` to *merge* the feature-1 versions into `main`

You will see output similar to:
```bash
(3.12.2) ➜  git-branching git:(main) git merge feature-1
Updating e436c51..b2f5622
Fast-forward
 app.py | 9 ++++++++-
 1 file changed, 8 insertions(+), 1 deletion(-)
```
You will also see that your IDE's editor contents for `app.py` contain all the changes from the most recent version of `feature-1`. Run the `git log` command and you will see that `HEAD`, `main`, and `feature-1` all point to the most recent version from `feature-1`. 

Here is the state of our repo:
{{< figure src="git-merge-feature1-repo.jpg" alt="merging feature-1 updates the main and HEAD variables to point to feature-1 and replaces the workspace" >}}

**Conceptually**, we have created a new version of `main` that includes all the changes from the `feature-1` branch. I say *conceptually* because have not actually created a new version in the repo, but have updated the `main` variable to point to the same version as `feature-1`.

{{< figure src="git-merge-feature1-concept.jpg" alt="conceptually, we have created a new version in main that contains all the changes from feature-1" >}}

The `feature-1` branch is still alive and well, and we can check it out and code against it. How does merging work?
1. **Find most recent common ancestor**: Git first identifies the most recent common ancestor (base commit) of the two branches. This is where both branches diverged from each other. In the illustration, this was the first commit `e436c5`.
2. **Analyze changes**: Git then looks at the changes that have been made in both branches since that common ancestor.
3. **Apply Changes**:
    - If the changes are ***non-conflicting*** (meaning they don’t overlap), Git automatically combines them. This is what happened here.
    - If there are ***conflicting*** changes (meaning the same parts of a file have been modified differently in each branch), Git pauses and marks the conflicts. You’ll need to resolve these conflicts manually before completing the merge.
4. (Sometimes) **Create a Merge Commit**: Once all changes are applied, Git creates a new commit (called a "merge commit") on the active branch. This merge commit has two parents—one from each branch being merged—and represents the integration of both sets of changes.
   - I say "sometimes" because in cases where `main` has not changed, like in this lab example, a merge commit on `main` is not created. `main` is simply *"fast-forwarded"* (that is the actual Git term) to the latest version of `feature-1` by moving the `main` pointer.
   - However, if changes were made to both `main` and `feature-1`, we would see a merge commit. 

In our case, we had a ***non-conflicting*** merge. This is the best case scenario. In a real project involving multiple engineers editing the same parts of code, you will very likely have **conflicting** changes.

We will discuss handling merge conflicts in the next lab.


## Exercise
1. Create a new `practice` branch.
1. Make at least **three** separate commits to the `practice` branch. Add code of your choosing. It can be trivial or non-trivial. You can modify existing lines or delete then. Follow the rules of good commit behavior:
   1. Commit early and often, but only commit working code. Comment out code that has syntax or semantic errors.
   2. Write a concise, descriptive commit message.
2. Merge the `practice` into the `main` branch.
3. Make a commit to the `main` branch.
4. Merge the `main` branch into the `practice` branch


## Summary and Key Commands
Git enables you to create branches, and switch between them. When you switch branch, Git replaces the contents of your working directory with the most recent version in the branch. The version history of all branches are kept separately in the local repository. This allows you to work on different things in parallel.

- Create a new branch: `git switch -c [name]`
- Switch between branches: `git switch [name]`
- Merge `[branch-name]` into the active branch: `git merge [branch-name]`

## Knowledge Check
- Question: What is the purpose of branching in Git, and why is it useful?
- Question: What are two ways that you can identify the ***active branch*** you are currently working in?
- Question: What is the name of the ***default branch*** created when you initialize a new Git repository?
- Question: When you change the code in a branch, is `main` affected?
- Question: Briefly describe what the special `HEAD` variable in Git refers to.
- Question: Suppose you make have three branches: `main`, `dev`, and `release`. Fill in the blank: the branch names are __________________ inside Git that point to specific _____________________ in the repository.
- Question: When you run `git switch feature-1`, you are making the _____________ variable point to the ________________ variable.
- Challenge: Create a new Git project, create and switch to a new branch, and modify a file with a new feature. Commit the change to this branch.