---
title: Text files
description: Use the CLI to manipulate and print text files (like source code).
weight: 15
---

## Part 3: Text File Manipulation
You can use the CLI to do simple or complex text manipulation. As developers, you will use an IDE like PyCharm or Visual Studio Code to do such tasks most of the time. However, it can be handy to do from the CLI sometimes.  Many scripts used to compile and build software these CLI text-manipulation techniques.

### Important concepts
Most CLI commands, including the ones you have already seen like `ls` and `pwd` have an output that is printed to the terminal. Some commands, like `cp`, do NOT have an output printed to the screen.

Below you will see the special `>` and `>>` operators. 
- `>` is the ***redirect operator***. It takes the output from a command and writes it to a file you specify, e.g., `echo "hello" > file.txt`. It will create the file if it does not exist, and will **overwrite the file** if it does exist!
- `>>` is the ***append operator***. It will create the file if it does not exist, and will **append to the end of the file** if it does exist!

### Viewing and Editing Text Files
- `echo` - Display a line of text
- `cat` - Concatenate and display file contents
- `more` - View file contents one screen at a time
<!-- - `grep` - Search for patterns in Files -->

{{< tabpane >}}
{{< tab header="Mac/Linux" lang="bash"  >}}
echo "Hello, CLI" > hello.txt
cat hello.txt
echo "Another line" >> hello.txt
cat hello.txt

seq 1 1 10000 >> numbers.txt  # making a big file - no need to learn. 
cat numbers.txt
more numbers.txt # Spacebar goes forward, b goes back, q to quit.
{{< /tab >}}

{{< tab header="Windows" lang="powershell"  >}}
echo "Hello, CLI" > hello.txt
cat hello.txt
echo "Another line" >> hello.txt
cat hello.txt

1..10000 | Out-File numbers.txt  # making a big file. Don't worry about learning this command.
cat numbers.txt
more numbers.txt # Spacebar goes forward, b goes back, q to quit.
{{< /tab >}}
{{< /tabpane >}}

<!-- {{< card code=true lang="bash" >}}
echo "Hello, Linux CLI" > hello.txt
cat hello.txt
echo "Another line" >> hello.txt
cat hello.txt
grep "Hello" hello.txt
grep "o" hello.txt
seq 1 1 10000 >> numbers.txt  # making a big file - no need to learn. 
cat numbers.txt
less numbers.txt # Spacebar goes forward, b goes back, q to quit.
{{< /card >}} -->

### Exercise
1. Use `echo` to create a text file with some content. Try `echo "this is my first file" > myfile.txt`
1. Use `cat` will print *all* of the file's contents to the screen all at once.
1. Use `echo` to *append* text to the file.
1. Use `more` to view the file content one screen at a time. Hit `q` to exit.
<!-- 1. Use `grep` to search for the word "first" in the file. -->

### Knowledge check
- Question: How can you append text to an existing file using `echo`?
- Question: What command would you use to search for a specific word in a file? 

## Next
Move on to [process management](../process-mgmt/).