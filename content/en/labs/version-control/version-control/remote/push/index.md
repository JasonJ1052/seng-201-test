---
title: git push
weight: 10
description: Manually sending changes from the local to the remote
---

We showed in [Scenario 1](../new-project/) that the `git push` command was necessary to share the version history from the local repo to the remote repo.

Sending changes to and pulling changes from the remote repo is always *manual*, just like staging, committing, and merging are. This is a good thing because it allows you to decide *when* to share changes or integrate changes from your teammates.

Let's illustrate the sharing process.

## Create a second version

1. Edit your `test.py` file. Make a change to the code. What is up to you.
2. Save the file, stage, and commit your change.
3. Run `git log`

The repos now look like this:
{{<figure src="git-commit-v2.jpg" alt="Version 2 committed to the local repo">}}

Your `git log` clearly shows the new version saved to the local repo.

However, open your remote repository's GitHub page in your browser. You will see that it is still showing the previous version. Your local `main` branch is linked to the remote `main` branch, but the latter is not up-to-date.

Again, sharing with and retrieving from the remote requires a manual command.

## `git push`

Run the command `git push`. This sends any changes to your local repo to the remote.

{{<figure src="git-push.jpg" alt="Updating the remote with a second version using git push">}}


Refresh the GitHub page in your browser, and you will see that the version name and the content of `test.py` are updated to the latest version. You will also see two versions now in the commit history.

Now everything is up to date!

Running `git push` always runs on the ***active branch***, which is `main` in our case. Suppose you have two local branches, `main` and `rand`. If you have parallel commits to in multiple branches, you will either need to need to `checkout` and `git push` each branch , or run `git push --all`.

# Knowledge Check
- (Question) What does the `git push` command do?
- (Question) Why is sending and pulling changes from the remote repository a manual process?
- (Question) How does the local main branch stay linked to the remote main branch?
- (Question) What happens if there are changes in the remote branch that are not present in your local branch before you push?
- (Question) How can you verify that your push was successful?
- (Challenge) Make a change to a file in your local repository, commit it, and then push it to the remote repository.
- (Challenge) View the commit history and confirm changes appear both locally and on the remote.