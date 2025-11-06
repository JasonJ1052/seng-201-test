---
title: Scenario 3 - Retrieving changes
weight: 20
description: Manually retrieving sending changes from the remote to the local
---


**Scenario**: Your started work on an assignment in the computer lab and pushed your changes to the remote. You went home and `clone`d the repo, worked some more, then `push`ed your changes to the remote. Now you are back in lab, and you need to get the latest changes from the remote. Or, perhaps a teammate pushed changes to the remote and you need to retrieve them.


## Remote changes
I will make some changes to and push them, so the repos now look like this:

{{<figure src="git-new-remote-version.jpg" alt="A new version is available on the remote">}}

The remote repo has a new version, but your local repo is not up-to-date. You need to manually retrieve the changes. This is a good thing! You don't want changes to automatically be applied whenever someone else on your team sends them to the remote repo. They could conflict!

## Super important point
Before you retrieve changes from the remote, you almost always want to ***either***:
1. Stage and commit any unsaved changes you have.
2. Undo, reset, or discard any uncommitted changes you have.
Ideally, you should have a "clean" workspace before you retrieve changes. It will make life easier on you.

## `git pull`
Run the command `git pull`. A few things happen:
- The changes from the remote repository on the active branch, `main`, are fetched and integrated into your local repo.
- Any changes are automatically ***merged*** into your workspace. This is why we wanted our workspace to be "clean."

{{<figure src="git-pull.jpg" alt="result of git pull when a new version exists">}}

You now have the most recent version of `main` in your workspace. you are ready to edit it, commit, and push as usual.

## Concurrent changes to the local and the remote
All of this is relatively straightforward when you are the only one working on a project. The version history of branches remains somewhat linear: you are the only one committing, pushing, and pulling, so you are always (probably) working on the latest version.

Life gets considerably more challenging when you have a team of developers all pushing and pulling from the same repo. If you commit a change to `main` to your local repo, but then Bob pushes a new version of `main` to the remote repo, what happens when you try to `push` or `pull`? Git will protect us from losing work, but we will likely end up with ***merge conflicts***. 

Team coordinator through Git remote repos *can* be smooth if we follow a good process. We will discuss this next.

## Knowledge Check
- (Question) What does the `git pull` command do?
- (Question) Why is it important to have a “clean” workspace before running `git pull`?
- (Question) What happens if there are conflicting changes on the local and remote repositories when using `git pull`?
- (Challenge) Create a scenario where you make changes locally and have conflicting changes on the remote repository. Use `git pull` and resolve any conflicts.
- (Challenge) Demonstrate how to ensure your workspace is clean before pulling changes.
