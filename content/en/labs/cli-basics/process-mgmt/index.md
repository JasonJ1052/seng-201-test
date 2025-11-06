---
title: Process management
description: Use the CLI to manipulate the OSes processes. 
weight: 20
---

## Part 4: Process Management

### Key terms
We discussed what a ***process*** is when we introduced Operating Systems concepts. Below you will see a reference to ***PID - Process ID***. This is an integer that uniquely identifies the process to the OS. As a user, you use the PID to specify which process you are talking about.

Run the following:
{{< card code=true lang="bash" >}}
ps
top  # (Mac/Linux only) hit q or Control+C to quit the program.
{{< /card >}}

### Monitoring and Controlling Processes
- `ps` - Report a snapshot of current processes
- `top` - (Mac/Linux only) Display processes and how much memory or CPU they are using. Similar to the Activity Monitor on Mac and the Task Manager on Windows. Hit `q` to exit.
- Use the keyboard combo `Control+C` to kill/quit the current process.
- `kill` - Send a signal to a process

### Exercise

We are going to install Python and create a wild task.

<!-- 1. **On Ubuntu only:** Run the command `sudo apt install python3`
   - You will be prompted to type your password. The terminal *will not* show any characters while you are typing.
   - You will see some text as python3 installs. -->
1. Open a second Termina by clicking the `+` button next to the tab in the menu of the current Terminal. You should see a second "fresh" terminal pane.
    <!-- - **Ubuntu on WSL**: Click the drop down next to your Ubuntu tab and make sure to pick Ubuntu again. You should see a second "fresh" Linux pane. If you see Powershell or Command Prompt, you're in the wrong place. -->
3. Now run `python3` or `python` and create the following infinite loop. You can also do this in IDLE or other editor if having trouble running python from the command line.

    {{< card code=true header="**python**" lang="python" >}}
while True:
    print("hello there")
    {{< /card >}}

We should now have an out of control Python process gobbling up CPU cycles. 

Switch back to the other Terminal tab and run the following commands.

{{< card code=true lang="bash" >}}
ps
top  # (Mac/Linux only) find the PID of the python process that is gobbling all the CPU
     # If using Windows, open the Task Manager program
kill <PID>  # Replace <PID> with the actual process ID
{{< /card >}}

The terminal will not say anything, but run `top` again. The runaway Python process should be gone. Switch back to the Terminal tab where you had that Python process and it should say `terminated` or something similar.


### Knowledge Check
- Question: How can you view real-time process activity?

## Conclusion
Anything you can do with your OS's GUI, you can do on the command line. It just looks different. Become comfortable with the CLI -- you will find that it can be MUCH faster for certain tasks, and will be indispensable to you as a software engineer.

<!-- Also, the commands above have equivalent commands on Windows machines (mostly). If you are a regular Windows user, you would do yourself a favor to learn the equivalent commands to things like `ls`, `rmdir`, and `cd` in the Windows CLI (PowerShell). -->

### Final Knowledge Check
- Question: Summarize the steps to create a new directory, navigate into it, create a text file, and view it using `less`.
- Question: From the CLI, how would you find the runaway process with a memory leak (probably using the most memory) and terminate it?

<!-- ## Further Reading
- Consider walking through this tutorial for even more explanation and extra commands and concepts: <https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal> -->

## Programming PRactice
- Once finished, work on the Warm-up [Programming Practice](../../programming-practice/) problems.