---
title: Editing code
weight: 10
description: Tips and tricks for editing code with PyCharm
---

## Editing
An Editor pane will automatically open every time you open a file. Things to know about the Editor windows:

1. **PyCharm automatically saves your files.** No need to explicitly save.
1. The **line numbers** on the left side are used to identify individual lines of code in error messages and elsewhere. 
2. Familiar text editing features like Cut and Paste are available in the `Edit` menu at the top or Right-Clicking in an editor window. Learn those keyboard shortcuts!
3. `CMD+/` (Mac) or `Ctrl+/` (Windows, Linux) **toggles comments** on the current line or selected lines. This is one of my favorite keyboard shortcuts!
   <video controls autoplay playsinline muted loop>
   <source src="comment.webm" type="video/webm">  
  </video>
1. Suppose your code calls a function defined elsewhere. Hold down `Cmd` (Mac) or `Ctrl`(Windows, Linux) and hover over the function call. It will turn blue like a link. Left click the link and the function definition in the editor. Very handy! Look up the **Go back** keyboard shortcut to return your cursor to where you were.
   <video controls autoplay playsinline muted loop>
   <source src="ctrl-click.webm" type="video/webm">  
  </video>
1. Not happy with a variable or function name? `Right-click it > Rename...` It will be renamed everywhere in scope!
2. Use the arrow keys to move the cursor one character at a time. Hold down `Ctrl` (Windows, Linux) or `Option` (Mac) while tapping the left- or right-arrows. You will skip entire "words". Again, very handy. Hold down `Shift` as well to select those words!

   <video controls autoplay playsinline muted loop>
   <source src="word-nav.webm" type="video/webm">  
  </video>


### Exercise

Create a new file called `fib.py` in your `pycharm-test` folder and paste in the following code:

{{< card code=true header="**Python code to compute the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)**" lang="python" >}}
def fibonacci(n):
    """
    Computes and returns the Fibonacci sequence of length n.
    Assumes n >= 1
    """
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    result = [1, 1]
    for i in range(2,n):
        result.append(result[i-1] + result[i-2])
    return result


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))
print(fibonacci(10))
{{< /card >}}

2. Hold down `Cmd` (Mac) or `Ctrl` (Windows, Linux) and mouse over one of the `fibonacci()` calls at the bottom. Click the link and watch the cursor jump.
3. Using the keyboard shortcut, comment out the first three `print(...)` calls at the bottom all at once.
5. Now uncomment them all at once.
6. `Right-click` a `fibonnaci()` call and rename the symbol. Where does it change in the code?
7. Hit `Ctrl+Z` or `Cmd+Z` to undo the rename.


## Knowledge check:
- Question: How do you comment/uncomment a block of code with your keyboard?
- Question: What does holding down `Cmd` or `Ctrl` + left-clicking on a name in the editor window do?
- Exercise: Add a second function to your `fib.py` file named `hello()` that simply prints `Hello World` when called. Now, try to rename (as described above) the `hello` function to `fibonacci`, which already exists. Describe what happens. 