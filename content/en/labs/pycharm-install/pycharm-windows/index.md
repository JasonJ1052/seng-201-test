---
title: for Windows
weight: 20
description: Instructions for installing PyCharm on Windows
---

This lab is for those who are installing PyCharm on Mac machines.

## Installation
1. **If you are on a <mark>lab computer</mark>, skip to the next section.**
1. Download [PyCharm](https://www.jetbrains.com/pycharm/download/).
1. Locate the downloaded `.exe` file and double-click to run. 
1. Choose the following options: 
      {{< figure src="install-options.png" alt="Windows PyCharm installation options" width="480">}} 
1. Finish the installation and run Pycharm.
1. Close any PowerShell or other terminal windows you have open.

## Test drive

We are going to create a sample project directory using PowerShell, then open PyCharm and edit files in that directory. A video follows the steps.


1. Open the Terminal (PowerShell) application. 
2. Run the following in PowerShell:
   {{< card code=true lang="powershell" >}}
cd ~                # make sure in your home directory
mkdir seng-201      # This directory will hold all our code for the course
cd seng-201         # change to the new directory
mkdir pycharm-test  # Make a new subdirectory for a test project.
cd pycharm-test     # change into the subdirectory
pycharm64 .           # launch PyCharm in the current directory
{{< /card >}}
   The `pycharm64` command launches the PyCharm program. The command `pycharm64 .` says launch Pycharm and have it open the current *working directory*. The symbol `.` always means the working directory. Sometimes it will be necessary to explicitly tell the CLI we are referring to the working directory; more on those situations as they arise.
1. A PyCharm window will open after a moment, and you will be asked if you want to "trust" the directory. Select the top option and, if using your own computer, the bottom option:
         {{< figure src="trust-pycharm.png" alt="Pop-up from PyCharm asking if you trust the contents of the directory. Pick yes." width="480">}} 
1. PyCharm will finish opening, and you will see a code editor with a boilerplate `main.py` file.


### Creating a new file
Let's create a file in the PowerShell in our project directory. We should see it immediately in PyCharm.

1. Go back to PowerShell and make sure you are in the `pycharm-test` directory. 
2. Type the command `echo "print('Hello World')" > hello.py` to create a Python file.
3. Go back to PyCharm. You should see the file `hello.py` in the directory here. Click on it and it will open an empty editor pane.
4. In the code editor, add the line `print("How are you?")`. 
5. Go back to the Powershell and type `cat hello.py`. You should see the code.

## Next

So you now have PyCharm successfully editing files and interacting with directories on Mac. 

You are now ready to code! Move on to [PyCharm Basics lab](../../pycharm-basics/).