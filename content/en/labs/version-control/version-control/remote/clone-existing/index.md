---
title: Scenario 2 - Clone an existing project
weight: 15
description: The remote already exists and you want the project
---


**Scenario**: A remote repository already exists, and you need a copy of the version history on your computer. You could be a part of a team working on the same project, or maybe you created a new project in lab and you need to check it out from your home computer.

## `git clone`

Let's start a new project to illustrate the process.
1. In your Terminal, navigate to your `seng-201/` directory.
   - When you clone, it will create a new subdirectory for you. So you need to be in the *parent* of where you want the workspace to live. We want to be in `seng-201/` for this example.
1. Run `git clone https://github.com/llayman/git-remote-clone`

You will see output similar to:
```bash
➜  ~ git clone https://github.com/llayman/git-remote-clone          
Cloning into 'git-remote-clone'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 4 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (4/4), done.
➜  ~ 
```
You will also have a new subdirectory named `git-remote-clone` inside `seng-201/`.


{{<figure src="git-clone.jpg" alt="git clone executing and creating a new repo">}}
What happened?
1. `git clone` went to the target URL looking for a repo. It found it, and made a copy of the version history on your local computer in the `git-remote-clone/` subdirectory.
2. Git created a local copy of the `main` branch, which is linked to the remote `main` branch
3. Git checked out the `main` branch into the workspace folder `git-remote-clone/`.

You are now ready to open `git-remote-clone/` in Visual Studio Code or other editor and start working. You edit, stage, commit, make branches, and push as usual.

<mark>**Do not edit the files yet.**</mark> Leave them in their initial version to illustrate the [next lab](../pull/).

## Knowledge Check

- (Question) What does the `git clone` command do?
- (Question) How does `git clone` handle creating a subdirectory for the repository?
- (Question) After cloning, what branch is typically checked out in your local copy?
- (Question) Does `git clone` also copy files into your workspace?
- (Question) How is the local main branch linked to the remote main branch after cloning?
- (Challenge) Clone an existing repository to your local machine and verify the directory structure.
- (Challenge) Open the cloned project in an editor and review its initial state without making changes.