---
title: Branching and Merging, Part 2
weight: 25
description: Handling merge conflicts
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/NAUU5PwsZk8?si=5Gk6dQtFcOTLktOy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The [previous lab](../git-branching/) explained the concept of ***branching***, which creates parallel version histories. ***Merging*** is the process of unifying parallel version histories back into a single history. 

One example is you create a branch to implement a long and complicated feature. Once the feature is complete and tested, you merge it back into the `main` branch.

***Merge conflicts*** occur when Git cannot automatically resolve differences between branches. This usually happens when:
- Two branches modify the same line in a file.
- One branch deletes a file while the other modifies it.

Merge conflicts occur frequently in real projects. Our goal is to learn how to recognize a conflict and resolve it.


## Example 1: Simple Text Conflict

Do the following:
1. Make a new subdirectory called `merge-conflicts` in your `seng-201/` directory.
2. Run `git init` to initialize a new Git repository.
3. Create the file `stats.py` and paste in the following code:
    ```python
    def calculate_stats(numbers):
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
        return {"total": total, "mean": mean, "count": count}
    ```
4. Run `git add .` to stage the changes.
5. Run `git commit -m "elementary stats added"` to commit the changes.

#### Create conflicting changes
1. Run `git switch -c stddev` to create a new branch called `stddev` from your default branch (`main` or `master`)
2. Modify `stats.py` to contain the following:
```python
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "count": count, "std_dev": std_dev}
```
3. Now stage and commit the change.
4. Run `git switch main` (or `master`) to switch back to your default branch. `stats.py` will show the "old" code from the default branch.
5. Change `stats.py` to the following:
```python
# main: math_operations.py
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    min_val = min(numbers)
    max_val = max(numbers)
    return {"total": total, "mean": mean, "count": count, "min": min_val, "max": max_val}
```
6. Stage and commit this change.

**Now we have a conflicting change**. We changed the last few lines of `calculate_stats()` differently in each branch. 

{{< figure src="text-conflict.jpg" alt="branch history view depicting parallel changes to stats.py" >}}
`stddev` is the active branch, but we have changes to `stats.py` in both branches that edit the same lines.

## Understanding a merge conflict
Now, let's merge in an attempt to join our two branches. Make sure you are in the `main` branch, and run `git merge stddev`.

You will see output similar to the following in the Terminal:
```bash
Auto-merging stats.py
CONFLICT (content): Merge conflict in stats.py
Automatic merge failed; fix conflicts and then commit the result.
(3.12.2) ➜  merge-conflicts git:(main) ✗ 
```

{{< figure src="text-merge.jpg" alt="branch history depicting the merge conflict" >}}

Git has attempted to merge the two version histories, but this process failed because both branches edited the same lines of code. We are now in a ***conflicted*** state. You can think of the conflicted state as an unfinished commit. You can either discard the changes with `git reset`, or you can resolve the issues and finish the new commit.

If Visual Studio Code is configured as your Git editor, you will see a screen similar to the following:
{{< figure src="merge-conflicts-code.png" alt="Visual Studio Code showing merge conflicts" >}}



**Notice that the content of `stats.py` has physically changed!** Git has inserted special characters into the code. The code will no longer compile. 

To resolve a merge conflict, ***you*** must decide what to keep. Our example has 3 conflicting lines. The lines in the `main` branch, pointed to be the `HEAD`, are marked with:
```python
<<<<<<< HEAD
    min_val = min(numbers)
    max_val = max(numbers)
    return {"total": total, "mean": mean, "count": count, "min": min_val, "max": max_val}
=======
```

The lines changed from the `stddev` branch are marked with:
```python
=======
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "count": count, "std_dev": std_dev}
>>>>>>> stddev
```

Remember, we ran the command `git merge stddev`, so `HEAD` is the main branch and the "incoming change" is from the `stddev` branch.

## Resolving a merge conflict

To resolve a merge conflict entails three things:
1. Edit the code to keep what you want.
2. Remove any lingering Git lines beginning with `<<<<<<<`, `=======`, or `>>>>>>>`.
3. Add and commit the changes.

Most IDEs provide you with some shortcuts and a merge editor. I find these to be dangerous. You really want to think about the code and what you want to keep in most cases. 

Let's resolve the merge conflicts manually. Here `stats.py` currently the entire code:
```python{linenos=true}
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
<<<<<<< HEAD
    min_val = min(numbers)
    max_val = max(numbers)
    return {"total": total, "mean": mean, "count": count, "min": min_val, "max": max_val}
=======
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "count": count, "std_dev": std_dev}
>>>>>>> stddev
```

As the developer, I actually want to keep **both** changes because I want the min, max, and standard deviation values.

I leave lines 8-9 (min and max) and lines 12-13 (standard deviation) as-is. I'll delete lines 7, 11, and 15 containing the Git special characters.

Now the problem is with the `return` lines: I want a combination of them. There is no shortcut to do this. I will simply create my own return line that amalgamates the old ones. 

My code looks like this after resolving the conflicts:
```python{linenos=true}
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    min_val = min(numbers)
    max_val = max(numbers)
    
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "count": count, "min": min_val, "max": max_val, "std_dev": std_dev}

```

I'm happy with my code. I should run and test it.

The last step is to stage and commit my changes:
- `git add .`
- `git commit -m "Resolving merge conflicts with min, max, and stddev"`

I now have a new ***merge commit*** on the `main` branch that contains these changes. This version acts like any other version in your local repo, and the `HEAD` will be pointing toward it. You will notice that all the angry red and `!` markers are gone from your IDE. I now have three versions in `main`'s history.

{{< figure src="test-merge-resolved.jpg" alt="branch history with the previous merge conflict resolved">}}

## Example 2: Conflicts in multiple files

Let's work through merge conflicts in multiple files. 

#### Create a new file
In the `main` branch, create the file `app.py` with the following:
```python
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))
```
Stage and commit the change to `main`. We now have four versions in the `main` branch history.


{{< figure src="added-app.jpg" alt="branch history with app.py added">}}

#### Create a new branch
Run `git switch -c mode`. Make the following changes:
1. In the Explorer pane, right-click `app.py` and Rename it to `main.py`.
2. Set `main.py` to:
```python
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))

    numbers = [8, 9, 10, 11, 12, 13, 14]
    print(stats.calculate_stats(numbers))
```
3. Set `stats.py` to:
```python
import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    min_val = min(numbers)
    max_val = max(numbers)
    mode = max(numbers, key=numbers.count)
    median = sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 != 0 else (sorted(numbers)[len(numbers) // 2 - 1] + sorted(numbers)[len(numbers) // 2]) / 2

    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"total": total, "mean": mean, "median": median, "mode": mode, "count": count, "min": min_val, "max": max_val, "std_dev": std_dev}
```
4. Stage and commit the changes.

We renamed the "main" file and added some code, and we also added median and mode to stats.

{{< figure src="added-mode.jpg" alt="mode branch added">}}


#### Concurrent changes to the main branch
Now switch to `main` again with `git switch main`.

1. We are going to streamline stats.py. Edit `stats.py` and change it to the following:
```python
import math

def calculate_stats(numbers):
    count = len(numbers)
    mean = sum(numbers) / count
    
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {"mean": mean, "std_dev": std_dev}
```
2. Open `app.py` and add another sample:
```python
import stats

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(stats.calculate_stats(numbers))

    numbers = [2, 2, 2]
    print(stats.calculate_stats(numbers))

```
3. Stage and commit the changes.

So we now have conflicting, concurrent changes in `main` that will cause a problem with the changes in the `mode` branch.


{{< figure src="main-conflicting.jpg" alt="more conflicting changes in main">}}


#### Resolving merge conflicts in multiple files
Now, let's create and deal with the inevitable merge conflicts:
1. `git switch main`
2. `git merge mode` to merge the `mode` branch into `main`.

Both the Terminal and your IDE will indicate that you have conflicts in multiple files. You simple need to deal with them one at a time.

{{< figure src="mode-merge-conf.jpg" alt="conflicts in multiple files">}}

First, let's open `main.py`. Notice how the rename happened automatically from `app.py` to `main.py`. If you're unhappy with this change, simply right-click and rename it back.

Let's look first at `main.py`:
{{< figure src="main.py.png" alt="Merge conflicts in main.py">}}

We have a conflict because the sample lines were changed concurrently. Remember the process:
- Edit the code to the be way you like
- Remove the special Git characters

I like more samples, so edit the file to keep both numbers and print them both out. Your final result should look like this:

{{< figure src="main.py.editing.png" alt="resolving conflicts in main.py">}}

Now let's go to `stats.py`, which looks like this:

{{< figure src="stats.py.png" alt="Merge conflicts in stats.py">}}

Most IDEs provide you with some shortcuts for resolving merge conflicts:
- **Accept Current Change**: Keep only the changes in `main`.
- **Accept Incoming Change**: Keep only the changes in `stddev`
- **Accept Both Changes**: Keep all the changed lines from both branches.
- **Compare Changes**: Provide another text view of the changes.
- **Resolve in Merge Editor**: I recommend skipping this.
  
In this case, I decide that I don't care at all about the median and mode any more. I just want to keep the streamlined version.

Click on the "Accept Current Change" link. You will see only the changes to `main` (the HEAD) are kept, and all incoming changes from `mode` are discarded.

P.S. If you make a mistake, remember that all you're doing is editing text files at this point. Just hit CTRL+Z/CMD+Z to undo.

Finally, make sure all your files are saved, stage, and commit the changes. Our final branch history looks like this:

{{<figure src="mode-merge-final.jpg" alt="multiple merge conflicts resolved" >}}

## Summary
Merge conflicts don't have to be scary, but they can be annoying. 
**Keeping your commits in all branches small and incremental will make merging easier**. 

The process for resolving merge commits is:
1. Look for the conflicting changes and decide what to do. 
2. remove the Git special characters.
3. Save, stage, and commit the merge conflict resolution.

Take your time with merge conflicts. Just quickly hitting "Accept Incoming Changes" or "Accept Current Changes" without a thought is what gets you in trouble. 
This may mean you manually edit the code, and that's not a bad thing. 

I strongly encourage you to avoid GUI-based merge editors, of which there are a few, until you master the process. It's just text editing. Editing the code manually will help ensure each decision you make is *intentional* and *easy to undo* in the text editor. Once you have mastered merging manually, then feel free to move onto the GUI programs.

## Knowledge Check
1. What causes a merge conflict in Git?
2. Suppose you want to merge a branch named `bug-fix` into the `main` branch. What git command do you run to perform the merge?
3. How can you identify merge conflicts using Git commands?
4. Describe the purpose of the conflict markers `<<<<<<<`, `=======`, and `>>>>>>>`.
5. (True/False) You can have multiple conflicting regions in a single file?
6. (True/False) You can have multiple files with conflicts?
7. Suppose the branch `delicious` is created from the `main` branch. The file `cheese.py` exists in both branches. `cheese.py` is editing in the `delicious` branch, and deleted in the `main` branch. Will there be a merge conflict if `main` is merged into `delicious`? Will there be a merge conflict if `delicious` is merged into `main`?
8. What are the three steps to resolving a merge conflict?
