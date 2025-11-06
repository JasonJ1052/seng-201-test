---
title: Git and GitHub setup
weight: 5
description: Setting up Git and GitHub utilities
---


Git is the world's most popular version control system. GitHub is a cloud service that hosts shared code repositories.

We will setup these and then delve further.



## Git installation

Git is available for all operating systems. 

- **On Mac**: Open a Terminal and run `git --version`. If git is already installed, you will see something like `git version 2.39.5 (Apple Git-154)`.You will be prompted to install git if you do not have it.
- **Lab computers**: Should already have `git` installed. Run `git --version` from a Terminal and you should see a verison number like `git version 2.49.0.windows.1`. If not, let the instructor know.
- **Windows**: Follow the instructions [on this page](windows).


## Git configuration

Close any open Terminals. Run the following in a new Terminal.
```bash
git config --global user.name "John Doe"  # Put your real name
git config --global user.email johndoe@example.com  # Put a permanent email here
```

You only run these once when you install Git.

## GitHub set up
We will use GitHub in this class to remotely store versions of our code. Many organizations use GitHub to store their code, including many popular open source projects.

**Use a permanent, personal email account** to register for a free GitHub account at [https://github.com](https://github.com). You will eventually lose access to your UNCW email, but you will want to access your GitHub account long after you graduate.

That's all you need to do for now. We will use GitHub soon.