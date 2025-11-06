---
title: Undoing mistakes with Git
weight: 15
description: Resetting your work to a safe state
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/N4ByQO0KxVI?si=r-hVom5k_ozZV-xR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

One of Git's powers is being able to "go back in time" to a previous version to undo a terrible mistake or simply to start fresh.

## How to identify the scenario that applies to you

We will walk through some common scenarios where you might want to undo your work and reset to a known safe state.

"Going back in time" depends on what you want to change and the current state of your repository in terms of (a) what's changed in the *workspace*, (b) what is *staged* in the index, and (c) what has been *committed* to the local repository.

Use the `git status` command to identify staged and unstaged changes, and `git log` to check the local repo version history.


## Starting state
In [Lab: Git Basics](../git-concepts/), we  created a Git repository for a simple `speakeasy/` project. We added two files, `main.py` and `README.md`, and committed two versions:
{{< figure src="speakeasy-v2-state.jpg" alt="The current state of the speakeasy/ project with two versions committed.">}}

We will pick up our example from this point.




## Oops #1: Deleted something from the workspace
1. Open Visual Studio Code for the `speakeasy/` folder.
2. Now delete `main.py`

{{< figure src="delete-main.jpg" alt="Deleting main.py from the workspace.">}}

Let's say you want to recover what you just deleted. This scenario may involve one file, many files, directories, or anything in the project folder. So when I use the word "file" below, I mean any of those things.

Your options depend on whether the file has been *staged* with `git add` or committed at some point in the past.

#### If the file *has* been staged before
1. First try using your IDE's undo feature: CTRL+Z or CMD+Z. If you see the file reappear, you are good to go.
2. If undo doesn't work, use `git restore [name]`. Git will place a copy in the workspace.

#### If the file *has not* been staged
1. Try using your IDE's undo feature.
2. If that doesn't work, check your operating system's "trash can".
3. Sorry. It's gone.


## Oops #2: Undoing *unstaged* changes


Suppose you're editing a file tracked by Git. You don't like what you've done, and want to start over from most recent version.

1. Make sure `main.py` is back in your workspace.
2. Add the following code to `main.py`:
    ```python
    import random

    def silly_compliment():
        compliments = [
            "You're as useful as a screen door on a submarine, but twice as fun!",
            "Your brain is like a sponge... except it soaks up memes more than facts!",
            "You're as rare as a unicorn at a hotdog stand."
        ]
        
        return random.choice(compliments)
    ```
3. Save the file.
4. Add the line `I like working on it!` to `README.md` and save the file.
5. Make a new file `hello.py` and add `print("Hello world!")` to it.
6. Run `git status`

`git status` tells you that `main.py` and `README.md` have been modified but are not staged, and it tells you that `blah.py` is new and *untracked*:

{{< figure src="hello-main-unstaged.jpg" alt="Making changes to main.py">}}

Our changes are only in the workspace, they are not *staged* in the index yet.

Now, let's undo some changes:
1. Run the command `git restore main.py` to reset to the file to the most recent version, in this case, the version `b424cc`.
   - The contents of `main.py` will change in the editor.
   - Notice that `hello.py` and `README.md` are unchanged. This is because we specified `main.py` as the target of `git restore`
2. Restore the changes to `main.py` by undoing with CTRL+Z or CMD+Z.
3. Now run the command `git restore .`
   - Notice that both `main.py` and `README.md` reset to their previous version. This is because we specified the target `.`, which is shortcut for "the current working directory". Both `main.py` and `README.md` are tracked by Git, so they *both* reset.
   - However, `hello.py` is *untracked* by Git so it is unaffected.

After running these commands, we are in the state below where `hello.py` is a new file but not being tracked by Git. Both `README.md` and `main.py` are as they were in the most recent committed version.

{{< figure src="hello-unstaged.jpg" alt="main.py and README.md are reset, hello.py remains unstaged">}}

Now what if you want to get rid of an untracked, unstaged file like  `hello.py`? Just delete the file!

The `restore` command replaces the workspace files with the most-recently-committed versions of those files in the local repository, i.e., the files as they were in `b424cc`.


## Oops #3: Undoing *staged* changes

Suppose you are adding, editing, or deleting files and you have run the `git add .` command to stage the changes in the index. You realize that you made a mistake, and you do not want to save those changes. You either want to work on them some more, or you simply want to start over.

We will start at the end of the previous scenario: `main.py` and `README.md` are unchanged and look like they do in the most recent version `b424cc`, while we added  added a new file `hello.py` that is not staged yet.

Run the following:
1. Re-add the following code to `main.py`:
    ```python
    import random

    def silly_compliment():
        compliments = [
            "You're as useful as a screen door on a submarine, but twice as fun!",
            "Your brain is like a sponge... except it soaks up memes more than facts!",
            "You're as rare as a unicorn at a hotdog stand."
        ]
        
        return random.choice(compliments)
    ```
1. Run `git add .` to stage the changes to both `main.py` and the new `hello.py` file.
2. Run `git status`

{{< figure src="hello-staged.jpg" alt="hello.py and main.py are staged for committing">}}
 
`main.py` and `hello.py` are now in the index of changes we want to save to a new version, but we haven't committed that new version to the local repository yet.

**Suppose at this point** that we need to do more work in `hello.py` and `main.py`. Maybe we've made a mistake, and we're not ready record these changes. 
- Run the command `git reset hello.py`. This will unstage the file, meaning it will not be included in the commit until you run `git add` again. 
- You can also run `git reset .` to unstage any staged changes. The files will be unchanged in your working directory.


{{< figure src="reset.jpg" alt="main.py and hello.py is unstaged">}}

The files still have all their changes in the workspace. You are ready to edit and fix up whatever you need.


## Oops #4: Completely restart from the last version

This is a common scenario. You work for a bit and then decide that all the changes you have made are bad, and the easiest thing is just **to start over**.

You want to wipe out ***all*** the changes in both your workspace and the index. ***Be careful***: once you do this, you can't undo it.

Let's start where we ended in the previous figure: we've changed `main.py` and added the new file `hello.py`. These changes are not staged in the index yet.

Do the following:
1. Run `git status` to see that we have unstaged and uncommitted changes.
2. The `git reset --hard HEAD`
    - `HEAD` is a special reference that means "the most recent committed version".
    - `--hard` argument tells Git "destroy changes to *tracked* files in the workspace and the index"

You should see output like
```bash
HEAD is now at b424cc4 Added message and README file
```

`b424cc4` is the most recent committed version in the local repository, and "Added message and README file" was the message for that version. 

Run `git status`:

{{< figure src="reset-hard-head.png" alt="wipe out all changes since the last commit">}}

**Notice that untracked files are unaffected**. We have not added or committed `hello.py`, so it remains untouched. But `main.py` has been reset to its most recent version.

All together, `git reset --hard HEAD` says "reset the *tracked* files in the workspace by **replacing** (`--hard`) the workspace contents with **the most recent version** (`HEAD`)"



Again, **this is a destructive action**. You cannot undo it once done. But, it is very useful for starting fresh. Your local repository is unaffected by the command.


## Oops #5: Undoing the most recent *commit*
You have run `git add .` and then a `git commit -m "<message>"`. Committing saves a new version to the local repository. 

Maybe you are unhappy with the version and you want to edit your work. Maybe you forgot to add a file that needed to be there. In these cases, the simplest thing is often to make the changes and just make another commit.

You committed version should be "good code". Bug free, compiles, works. However, sometimes you commit a mistake. You find a terrible bug in your code. Or you committed a syntax error and didn't notice. **These scenarios call for you to undo the commit**. 

Starting from the previous scenario, we have `hello.py` in the workspace but untracked. Let's introduce a bug to `main.py`:
1. Open `main.py` and add the line `tip = float(input("Enter a tip amount: "))`
2. Make sure to save `main.py`
3. Run `git add .`
4. Run `git commit -m "Enable user to type a tip amount"`

You will see output like:
```bash
[main 81a55e5] Enable user to type a tip amount
 2 files changed, 3 insertions(+)
 create mode 100644 hello.py
```

We should now have three versions in our local repository. Run `git log` to see them:
{{< figure src="version-3.jpg" alt="committing the third version">}}

We realize that we have committed a bug. `tip = float(input("Enter a tip amount: "))` will crash the program if the user types in a non-numeric number for the tip, like `"one dollar"`. We want to undo the commit so we can fix the bug and to keep our version history containing only "good code".

You have two options here:
1. You may have some changes to your workspace that you want to keep. Like you want to keep `hello.py`. Or maybe your code in `main.py` is pretty good, and you just want to fix it up a little bit.
2. Your last commit was a total disaster. You don't want to keep any changes you made to `main.py` or `hello.py`. You want to completely throw away the most recent version and go back to the one before it.

#### Option 1: Preserve your work, fix it, then make a new commit.

Run the command `git reset HEAD~1`. You will see output like:
```bash
Unstaged changes after reset:
M       main.py
```

Now run `git log`. You will see something like:
```bash
commit b424cc472f7276dc35493abbd186563a191ca25b (HEAD -> main)
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Mon Oct 21 15:21:44 2024 -0400

    Added message and README file

commit 8356ea035b8d6538f9ea4eabe2393d6cd6016553
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Mon Oct 21 15:13:00 2024 -0400

    First commit of main.py
```

Notice that `git log` only shows two versions! What have we done? Your current Git state is like this:


{{< figure src="git-reset-head" alt="forgetting the most recent version">}}

The command `git reset HEAD~1` tells the local repository to "forget" the most recent version. It's like it never happened.

However, **the files in your workspace and index are *unchanged!*** All the edits and additions are still there for you to work with, they are just not committed. 

Now you have the opportunity to fix up those files, `add` them, and `commit` them.

#### Option 2: Disaster! Delete the last version *and* reset all the files
This is just like [Oops #4](#oops-4-completely-restart-from-the-last-version) where you reset the tracked files, but you also want to destroy the most recent commit.

The command to do this is `git reset --hard HEAD~1`. **This command is destructive and you cannot undo the consequences.**

Assuming you have changes to `main.py` and `hello.py` from the previous scenario:
- Do `git add .` and `git commit -m "Enabling the user to enter a tip"` to stage and commit a new version
- Run `git reset --hard HEAD~1`
- Run `git log` to see the version history

{{< figure src="git-reset-hard-head" alt="forgetting the most recent version and resetting tracked files">}}

`hello.py` is unaffected because it is untracked, however, `main.py` and `README.md` are reset to their version 2 status. We've also deleted the bad version. 

## Recap
Git has even more functionality for "going back in time", such as going back two, three, or more versions in the past. Or undoing multiple commits at once. Those use cases can be tricky to do correctly without unintended consequences.

For now, the "Oops" scenarios above will be sufficient 95% of the time as you develop your Git skills:
1. Deleted a file from the workspace: Undo (CTRL+Z/CMD+Z) or `git restore <filename>`
2. Undoing *unstaged* changes: `git restore <filename>`
3. Undoing *staged* changes: `git reset <filename>`
4. Completely restart from the last version: `git reset --hard HEAD`. **This is destructive!**
5. Undoing the most recent *commit*:
    - and keep your work: `git reset HEAD~1`
    - and throw away work: `git reset --hard HEAD~1`. **This is destructive!**

## Knowledge check
- (Question) Describe how `git status` and `git log` help identify a repository's state.
- (Question) What command would you use to recover a deleted file that was previously staged or committed?
- (Question) Explain how to undo changes that are staged but not committed.
- (Question) What happens to untracked files when you run `git restore .`?
- (Question) Which command do you run to completely reset your working directory to the most recent version?
- (Question) Which command do you run to destroy/remove the last version in the local repository?
- (Challenge) Simulate deleting a file and use Git commands to recover it.
- (Challenge) Experiment with staging changes, then undo them.