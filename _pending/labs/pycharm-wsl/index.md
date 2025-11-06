---
title: for WSL
weight: 5
description: Instructions for installing PyCharm to work with the Windows Subsystem for Linux
---

This lab is for those who are on Windows and have set up the Windows Subsystem for Linux (WSL) [following Option 1 from the Installing a *nix operating system lab](/labs/getting-linux/#option-1-preferred---windows-subsystem-for-linux).

## Installation
1. You must request a [free PyCharm Professional license](https://www.jetbrains.com/shop/eform/students). Sign up using your `@uncw.edu` email address.
1. Download and install [PyCharm for Windows](https://www.jetbrains.com/pycharm/download). You must have **Pycharm Professional**, not the Community edition.
1. Complete the install process. I recommend the options below, but they are not required:
   {{< figure src="00-install-options.png" alt="Pycharm installation options on windows" width="480">}}

## Setup
1. Run PyCharm after installation is complete.
1. You should see a prompt to activate the license. Select "Activate License" then "Log In to JetBrains Account". 
   {{< figure src="01-activation-prompt.png" alt="PyCharm license activation prompt" width="300">}} {{< figure src="02-activation-options.png" alt="Pycharm activation options" width="300">}}
1. Complete the login process using the Jetbrains website.
1. You should now see a "Welcome to PyCharm" screen. Select "WSL" in the left pane, then click "New Project" in the main pane.
{{< figure src="03-select-wsl.png" alt="Selecting WSL from the PyCharm home page" width="480">}}
1. You WSL instance you created should already be selected. Click "Next".
{{< figure src="04-choose-wsl-instance.png" alt="Choosing a WSL instance." width="480">}}
1. PyCharm will process for a minute then present a "Choose IDE and Project" screen.  Leave the "IDE Version" as-is.  Click the `...` next to the "Project directory" selector.
   {{< figure src="05-project-setup.png" alt="IDE and Project configuration options." width="480">}}
1. We are now going to create a directory in Ubuntu to keep all your class projects. We will also create a new test subdirectory in that directory. 
   1. In the pop-up, expand the directories to select `\\wsl.localhost\Ubuntu\home\<your_username>`. Left click to select the directory. 
   2. Then click the "New Directory" button at the top. 
   3. Then enter `seng-201` in the pop-up name box.
      {{< figure src="06-home-select.png" alt="Creating the 201 folder" width="320">}}
   1. Now select the `seng-201` folder and click the "New Folder" button again. Enter `pycharm-test` in the box.
      {{< figure src="07-proj-directory.png" alt="Creating a test project." width="320">}}
   1. Finally, select the `pycharm-test` folder and click "OK".
1. You will be back on the "Select IDE and Project" page. It should look like below. Click the blue "Download IDE and Connect" button.
   {{< figure src="08-dl-ide.png" alt="Accept project settings." width="320">}}
1. PyCharm will take several minutes to download and configure necessary software to talk to your Ubuntu instance. After it completes, you will be shown a user agreement. Accept it.
   {{< figure src="09-ide-dl-progress.png" alt="Download progress." width="400">}}
   {{< figure src="10-agreement.png" alt="License agreement." width="400">}}
1. Finally, you should see the PyCharm IDE editor window. Click the Play button at the top to see the Python program run. You are done with the setup.
   {{< figure src="11-finished.png" alt="PyCharm running on WSL" width="600">}}

You may see some Windows Firewall pop-ups. It is okay to allow them.

## Configure the Ubuntu CLI
Finally, we are going to make it so you can open PyCharm from the Ubuntu CLI. This will be very convenient later.

1. First, close PyCharm.
1. Open an Ubuntu Terminal [as described in the previous lab](../../cli-basics/launching/#using-the-windows-subsystem-for-linux).
1. Run the following command, which will create an ***alias*** to run PyCharm from the command line:

{{< card code=true header="**bash**" lang="bash" >}}
printf "pycharm() { \"/mnt/c/Program Files/JetBrains/PyCharm 2024.3.1.1/bin/pycharm64.exe\" \"\$@\" > /dev/null 2>&1 & }\n" >> ~/.bashrc && source ~/.bashrc
{{< /card >}}

## Test drive

Let's open PyCharm from the Ubuntu CLI and do somet light editing.

1. Run the following commands from the Ubuntu terminal:
   {{< card code=true header="**bash**" lang="bash" >}}
cd       # make sure in your home directory
cd seng-201
cd pycharm-test  # change to test directory
pycharm .   # launch PyCharm in the current directory
{{< /card >}}
1. PyCharm should open after a moment. You may see a prompt to "Trust the directory...". Do that. You may need to click on the Explorer icon in PyCharm to see your files:
   <video controls autoplay playsinline muted loop width="800">
   <source src="pycharm-from-cli.webm" type="video/webm">  
   </video>
1. Go back to your Ubuntu terminal and make sure you are in the `pycharm-test` directory. 
2. Type the command `touch hello.py` to create an empty Python file.
3. Go back to PyCharm. You should see the file `hello.py` in the directory here. Click on it and it will open an empty editor pane.
4. In the code editor, type `print("Hello World")`. 
5. Go back to the Ubuntu Terminal and type `cat hello.py`. You should see the code.

   <video controls autoplay playsinline muted loop width="800">
   <source src="hello.webm" type="video/webm">  
   </video>

## Next
So you now have PyCharm successfully editing files and interacting with directories inside Ubuntu. 

You are now ready to code! Move on to the [PyCharm basics lab](../../pycharm-basics/).
