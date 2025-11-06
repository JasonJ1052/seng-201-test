---
title: Git basics
weight: 10
description: Basic Git concepts and commands
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/jhcSduKToq8?si=KgV5hTN7VdkhSrqC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The Git Verson Control System (VCS) stores versions in ***repositories***. You will typically have one repository for each project. For example, you would have a repository for Assignment 2, a separate repository for Assignment 3, etc. 

Git divides the world into three parts to facilitate tracking and sharing versions.

{{< figure src="ws-lr-rr.jpg" alt="Workspace, local repo, and remote repo image" >}}

The ***workspace*** or ***working directory*** is the directory on your computer where the project resides, e.g., `seng-201/assignment3/`. You work on your files in this directory as usual.

A ***local repository*** is a *hidden directory* within the *workspace* where Git stores the version history and other information. The local repository is created by the Git program. You interact with the local repository using `git` commands to create new versions, compare files, and revert back to earlier versions.

A ***remote repository*** is a copy of the *local repository* on a computer somewhere else. In this class, the copy will be kept on GitHub, but software companies may have their own servers. The remote repository enables teams to share project changes and to restore the project if something terrible happens to someone's computer.

You **must** learn and understand the relationship between these entities to master Git. Tools like OneDrive and Google Drive have similar concepts, but what distinguishes Git from those tools is that you decide *when* to save and share changes to your project between these entities.

## Keeping a version history

We will start with the most simple use case for a VCS: we want to kept a historic timeline of versions. A ***version*** is a snapshot of files in the ***workspace*** at a point in time.


### Step 1. Start with a directory

Create a subdirectory called `speakeasy` in your `seng-201/` directory. Change into the `speakeasy` directory

Open the directory in your code editor. Create a file named `main.py` with the following:

   {{< card code=true header="`main.py`" lang="python" >}}
print("Welcome to the Speakeasy!")
print("Did you know? The term 'speakeasy' was coined during Prohibition in the United States.")

mocktails = ["Cucumber Lemonade", "Pineapple Ginger Beer", "Berry Spritzer"]
print("\nToday's Mocktail Menu:")
for drink in mocktails:
    print(f"- {drink}")

print("\nThank you for visiting! Come again soon.")
{{< /card >}}

We have created only the workspace -- no Git yet:

{{< figure src="ws-only.jpg" alt="Workspace only" title="Conceptual model">}}

### Step 2. `git init`

We need to initialize each project to use Git. In the Terminal:
1. Make sure you are in the `speakeasy/` directory.
2. Run the command `git init`
3. You will see output like `Initialized empty Git repository in /Users/laymanl/seng-201/speakeasy/.git/`

This command initializes the *local repository* within the working directory. The local repository is created within a hidden `.git/` subdirectory. Run the command:
- (Mac/Linux) `ls -al` 
- (Windows) `dir /a`

to see the `.git/` subdirectory. You will *not* see it in the file browser of your IDE by default.
You may see the `.git/` subdirectory in your Mac Finder or Windows Explorer depending on your settings. 


{{< figure src="ws-lr-only.jpg" alt="Workspace and local repo only" title="Conceptual model">}}

Git is now monitoring the workspace for changes to files and subdirectories. You only need to run `git init` once to track a new project and any subdirectories under that project.

#### A word about git directories
First, you should not keep Git repositories in directories that are in OneDrive, Google Drive, or the like. You can run into weird authentication errors. 

Second, do not nest Git local repositories, i.e., do not run `git init` on a directory, then run `git init` later on a subdirectory of the original. 

If you ran `git init` in the wrong place, find that hidden `.git/` directory and delete it. This will remove the Git repository (and all of its history), but will not change the workspace files.

#### Checking where you are: `git status`
Run the command `git status`. You should see something like:
```bash
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	main.py

nothing added to commit but untracked files present (use "git add" to track)
```

`git status` is useful for understanding the state of your workspace and local repository. Breaking down the contents:
- `On branch main`: we will discuss branches in a future lab. Ignore for now.
- `No commits yet`: Git is telling us we have not created a version yet. We have to do this manually.
- `Untracked files...`: Git says there are files that have been added, changed, or removed that we have not versioned yet.

### Step 3. Creating the first version

Creating a version entails two steps. Run the following in the Terminal:
```bash
git add main.py
git commit -m "First commit of main.py"
```

- `git add [file]`: Adds a changed file to the *index*. 
  - The ***index*** is the list of files that will be saved to the version.
  - It is possible to edit, say, 10 files, but only save 5 of them to the version. The *index* lets you be selective if you need to.
- `git commit -m "<message>"`: Commit your changes to a new version.

{{< figure src="add-commit.jpg" alt="Creating the first version" title="Conceptual model">}}

We have just created a new ***version***: a snapshot of project files at a point in time. We have added and committed `main.py` to a new version in Git local repository. We can now, if we want, **restore** `main.py` to this version in the future. 

### Step 4. Creating another version

Let's make some edits to our project. First, the following line to `main.py`:
```python
print("Don't forget to tip your server!")
```
Second, create a new file named `README.md` in your IDE:
```markdown
This is my first project!
```

Go to the Terminal and run `git status`. You will see something like:
```bash
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

This is the current status. We have added a file, but we have not added it to the index nor committed it yet. We also haven't added or committed our changes to `main.py` yet. Remember, everything in Git is ***manual*** and this is by design.

{{< figure src="new-file.jpg" alt="Changes made, but not added to the index nor committed.">}}

The `Changes not staged for commit:` section tells us which files have changed in the workspace, but we haven't added to the *index*. We also see the `Untracked files:` section, which is telling us that `README.md` is a new file with no version history.

Let's commit them both at once. Run the following:
```bash
git add .
git commit -m "Added message and README file"
```

The command `git add .` tells Git to add *ALL* changes, additions, and deletions in the *current directory*. This is how you should get a snapshot of all changes to your project.

We have now created a new version. Our Git looks like this:

{{< figure src="new-version.jpg" alt="Second set of changes added and committed to the local repository.">}}


#### Differences
It is important to understand that Git does not store entire copies of files. You cannot go into the hidden `.git/` directory and simply copy "version 1" of your files. 

Git stores ***file differences***. It compares Version 2 of your files to Version 1 to see what has changed, and stores the set of changes. This set of changes is called a ***difference***, or a ***diff*** for short. Storing only the differences makes Git more space efficient, and also enables some useful comparison functionality that we will use in a future lab.


### Step 5: Viewing history with `git log`
Type `git log` in your Terminal. You will see something like this:
```git
commit b424cc472f7276dc35493abbd186563a191ca25b (HEAD -> main)
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Mon Oct 21 15:21:44 2024 -0400

    Added message and README file

commit 8356ea035b8d6538f9ea4eabe2393d6cd6016553
Author: Lucas Layman <laymanl@uncw.edu>
Date:   Mon Oct 21 15:13:00 2024 -0400

    First commit of main.py
(END)
```

Press `q` to exit the log viewer.

Each block is a version. The versions are not numbered 1, 2, 3, etc. but are identified by a unique *hash* like `b424cc472f7276dc35493abbd186563a191ca25b`. They are shown in reverse chronological order.

`git log` shows you the version history of the local repository. `git log` useful to see what work has been done recently. The log output also highlights the importance of a meaningful, succinct commit messages.

## Important concept review

The *workspace* is the directory on your filesystem that your project lives in. You code here. When you make changes to files, they are immediately saved in the workspace because the workspace is synonymous with your filesystem.

The *local repository* is Git's history of versions. Versions are snapshots of the workspace files at a point in time. The developer must manually *add* and *commit* changes to create a version.

Git does not store entire copies of files, but rather the *differences* from one version to the next.



## Summary of the process
To create a version history for a project (a directory), do the following:
1. Run `git init` to create the local repository.
2. Make changes to files: adding new files, editing existing files, deleting files.
3. `git add .` to stage all changes in the index.
4. `git commit -m "<message>"` to save the version to the local repository.
5. Repeat steps 2--5.


## Knowledge Check
- (Question) Explain the purpose of the local repository and how it differs from the workspace.
- (Question) What is the function of a remote repository in Git?
- (Question) Describe the significance of the `.git/` directory.
- (Question) What happens when you run `git init` in a directory?
- (Question) What does the `git status` command show you?
- (Question) What is the purpose of the Git index (staging area)?
- (Question) What command do you run to add something to the staging area?
- (Question) What command do you run to save a new version in the local repository?
- (Question) What happens if you try to save a new version without staging first?
- (Question) True or False: A version is a copy of the entire file that was changed?
- (Question) Versions in Git are not stored sequentially as in Version1, Version2. How are versions uniquely identified in Git?
- (Challenge) Create a new directory, initialize it with Git, and create a new file. Commit changes to track the file.
- (Challenge) Add modifications to an multiple files and use `git status` to see the changes. Commit only a subset of the changes.
- (Challenge) Describe how you would undo an incorrect `git init` operation.