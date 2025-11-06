---
title: Running code and the integrated terminal
weight: 15
description: How to run Python code and leverage PyCharm's terminal.
---

PyCharm uses tools installed on your computer to run programs. PyCharm should automatically find the Python you have installed on your computer if installed in a "standard" location.

## Running code
There are multiple ways to run a program file:

1. In the editor window, `Right-click` anywhere in the code to open the **context menu**, then select `Run [filename]` or `Debug [filename]`.
   - If necessary, select the `Python Debugger` popup, and select default options of subsequent pop-ups until you see the program run in the interactive Terminal at the bottom.
   - We will discuss the difference between `Debug` and plain `Run` in the future. 
      {{< figure src="run-context.png" alt="Running from the context menu" width="480">}}
1. Use the run shortcuts at the top of the PyCharm window. You select the file you want to run from the dropdown, and then either the Run or Debug button. By default, PyCharm will run the most recent program run.
      {{< figure src="menu-shortcut.png" alt="Running from the PyCharm toolbar">}}
3. Use keyboard shortcuts to re-run the most recent program:
      - `Shift+F9` (Windows, Linux) or `^D` (Mac) to Debug
      - `Shift+F10` (Windows, Linux) or `^R` (Mac) to Run without debugging.
  

### Exercise
1. Create `hello.py` in the `pycharm-test` directory if needed and add `print("Hello World")`
2. Run `hello.py` using the the context window.
3. Run it using the PyCharm toolbar.
4. Run it using keyboard shortcuts.

When you run your `hello.py` program, you should see output in the Debug or Run pane at the bottom. The exact output differ from mine, but you should see `Hello World` in there. 
{{< figure src="python-debug-console.png" alt="A screen shot of python running" >}}

## The Integrated Terminal
PyCharm also has an **Integrated Terminal**, which is an embedded version of the Command Prompt (Windows) or Terminal (Mac). You can use CLI commands like `cd`, `ls`, `mkdir`, etc.

Open the Integrated Terminal by either:
- Clicking the Terminal icon in the bottom left
- Using the PyCharm menu, `View → Tool Windows → Terminal`
- Using the keyboard shortcut `Alt+F12` (Windows, Linux) or `Option+F12` (Mac)

When you ran your `hello.py` program, you should have seen a flurry of output in the **Integrated Terminal** window at the bottom. What just happened?
1. PyCharm opened a Terminal CLI, like you did in the [Launching a Terminal lab](../../cli-basics/launching/), except this one is embedded in PyCharm.
2. PyCharm issued the CLI command `python` with your file as an argument.
3. `python` runs in the Terminal and prints output.

{{< figure src="integrated-terminal.png" alt="PyCharm's integrated terminal" >}}

I find it convenient to use this integrated Terminal rather than switching to a another window. Or you may prefer to keep them separate. Do what works for you. 


### Exercise
1. List directory contents in the integrated Terminal using the `ls` command.
2. Type `cd ~` in the integrated Terminal to switch to your home directory. Notice how the contents of the Project pane ***do not change***. You are only changing the working directory in the Terminal.
4. Use the Terminal to navigate to your `pycharm-test` directory using `cd` commands.
5. Run the command `touch hello2.py`. Does it appear in the Explorer pane?
6. Run the command `rm hello2.py`. What happened? What happened in the Project pane?


## Knowledge check:
- Question: What is the keyboard shortcut for debugging/running your program?
- Question: How do you open the integrated Terminal in PyCharm?
- Question: How can you print the name of the *current working directory* in the integrated Terminal?
- Question: If you have a runaway process in the integrated Terminal, how do you cancel/kill it so that you regain control of the Terminal? (The answer is the same as for the regular Terminal.)