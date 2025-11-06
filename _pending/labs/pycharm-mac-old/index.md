---
title: for Mac
weight: 15
description: Instructions for installing PyCharm on Mac
---

This lab is for those who are installing PyCharm on Mac machines.

## Installation
<!-- 1. You must request a [free PyCharm Professional license](https://www.jetbrains.com/shop/eform/students). Sign up using your `@uncw.edu` email address. -->
1. Download [PyCharm for Mac](https://www.jetbrains.com/pycharm/download/) `.dmg` file.
1. Locate the downloaded `.dmg` file and click to open. Drag PyCharm into the Applications folder.

<video controls autoplay playsinline muted loop width="400">
   <source src="install-pyc.webm" type="video/webm">  
   </video>


## Setup
1. Open your Finder, select Applications, then PyCharm. 
1. You may wish to pin PyCharm to your dock after launching.
1. You should see a prompt to activate the license. Select "Activate License" then "Log In to JetBrains Account". 
   {{< figure src="01-activation-prompt.png" alt="PyCharm license activation prompt" width="300">}} {{< figure src="02-activation-options.png" alt="Pycharm activation options" width="300">}}
1. Complete the login process using the Jetbrains website.

### Enable launching PyCharm from the Terminal
1. Open the Mac Terminal application as described in the [Launching a Terminal lab](../../cli-basics/launching/#launching-a-terminal-on-mac).
1. In the Terminal, type the command
   {{< card code=true lang="bash" >}}
sudo nano /usr/local/bin/pycharm
{{< /card >}} 
1. Enter your password when prompted. 
1. You will now see the Nano text editor in your terminal. Type or paste in the following:
   {{< card code=true lang="bash" >}}
#!/bin/sh

open -na "PyCharm.app" --args "$@"
{{< /card >}} 
   {{< figure src="03-nano.png" alt="Creating a pycharm launch script using nano" width="600">}} 
1. Hit Control+O to save, then Enter to accept the filename.
1. Hit Control+X to exit the text editor.
1. Run the following command in the Terminal:
   {{< card code=true lang="bash" >}}
sudo chmod +x /usr/local/bin/pycharm
{{< /card >}} 

You will now be able to type `pycharm .` in the Terminal to open PyCharm to edit the current directory's contents.


## Test drive

We are going to create a sample project directory using the Terminal, then open PyCharm and edit files in that directory. A video follows the steps.

1. Open the Terminal application. 
2. Run the following in the Terminal:
   {{< card code=true lang="bash" >}}
cd       # make sure in your home directory
mkdir seng-201   # This directory will hold all our code for the course
cd seng-201      # change to the new directory
mkdir pycharm-test  # Make a new subdirectory for a test project.
cd pycharm-test     # change into the subdirectory
pycharm .   # launch PyCharm in the current directory
{{< /card >}}
   The `pycharm` command launches the PyCharm program. The command `pycharm .` says launch Pycharm and have it open the current *working directory*. The symbol `.` always means the working directory. Sometimes it will be necessary to explicitly tell the CLI we are referring to the working directory; more on those situations as they arise.
1. A PyCharm window will open after a moment.
2. You may be asked if you "trust the authors of the files in this folder". Click the checkbox and then pick "Yes, I trust the authors."

Here is the process in a video:
<video controls autoplay playsinline muted loop width="640">
<source src="launch.webm" type="video/webm">  
</video>


### Creating a new file
Let's create a file in the Terminal in our project directory. We should see it immediately in PyCharm.

1. Go back to your Terminal and make sure you are in the `pycharm-test` directory. 
2. Type the command `touch hello.py` to create an empty Python file.
3. Go back to PyCharm. You should see the file `hello.py` in the directory here. Click on it and it will open an empty editor pane.
4. In the code editor, type `print("Hello World")`. 
5. Go back to the Ubuntu Terminal and type `cat hello.py`. You should see the code.

<video controls autoplay playsinline muted loop width="640">
<source src="hello.webm" type="video/webm">  
</video>

## Next

So you now have PyCharm successfully editing files and interacting with directories on Mac. 

You are now ready to code! Move on to [PyCharm Basics lab](../../pycharm-basics/).