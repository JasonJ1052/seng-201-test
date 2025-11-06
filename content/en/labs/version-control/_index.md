---
title: 09. Version Control
weight: 45
description: Creating a history of code changes and sharing code with your team.
---

Coding is an incremental activity. You write code, it's a little broken, you fix it. You work on the next thing, it's a little broken, you fix it. And so forth until you're "done".

During the coding process, you have probably done the following:
- Saved a copy of the file at a point when you *know* it just works. Then you keep coding.
- Wanted to go back in time to a point when everything *did work* so you can start over.
- Had to email or otherwise share your code files between computers.

***Version Control Systems (VCSes)*** are systems that manage changes to source code, documents, and other files over time. VCSes are also how all teams store and share their code on a shared project. VCSes are essential to software engineering.

A VCS is a computer application, the most prolific of which is called [Git](https://git-scm.com/) and was created by Linus Torvalds, the creator of Linux. All VCSes, including Git, have the following features:
1. The ability to make a ***version***: a snapshot of the project files at the current time.
2. The ability to ***revert*** to an earlier version.
3. The ability to ***compare*** versions of the project files to see their differences.
4. The ability to ***share*** versions with a central repository that multiple people can access.

Importantly, it is up to the programmer to decide ***when*** to create a version, when to revert, and when to share. This is in contrast to your OS or an app like OneDrive or Google Drive, which do some of these things automatically.

We will use Git and GitHub in this class as our VCS. We will start by setting up these tools on your computer.

