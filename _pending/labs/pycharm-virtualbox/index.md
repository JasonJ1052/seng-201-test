---
title: for VirtualBox
weight: 10
description: Instructions for installing PyCharm on Ubuntu running in VirtualBox
---

This lab is for those who are on Windows and are running Ubuntu inside **VirtualBox** [using Option 2 for Windows from the Installing a *nix operating system lab](/labs/getting-linux//#option-2---virtualbox).

## Installation
1. You must request a [free PyCharm Professional license](https://www.jetbrains.com/shop/eform/students). Sign up using your `@uncw.edu` email address.
1. Open VirtualBox and start up your Ubuntu virtual machine (VM). Sign in to Ubuntu. 
   - You may want to go full screen. Do this by selecting View -> Full Screen. 
   - If the Full Screen is small, right-click on the Desktop -> Display Settings then change the Resolution to something larger, probably 1920x1080.
   - You exit full screen by hitting `Right CTRL+F`
1. You should open this page in Firefox launched within Ubuntu for easy copy-and-paste.
1. Open a Terminal [as described in the Launching a Terminal lab](../../cli-basics/launching/#using-virtualbox).
1. Copy and paste in the following commands. You will need to enter your password.
   {{< card code=true header="**bash**" lang="bash" >}}
BUILD=2.5.2.35332
sudo apt install libfuse2 libxi6 libxrender1 libxtst6 mesa-utils libfontconfig libgtk-3-bin
wget https://download.jetbrains.com/toolbox/jetbrains-toolbox-$BUILD.tar.gz
tar -xzf jetbrains-toolbox-$BUILD.tar.gz && cd jetbrains-toolbox-$BUILD && ./jetbrains-toolbox
{{< /card >}}
1. The commands will take a few minutes to run. You should see a JetBrains Toolbox window popup when done. Agree to the JetBrains User Agreement and click Start (you may need to scroll down in the popup).
   {{< figure src="00-toolbox-license.png" alt="JetBrains Toolsbox start screen" width="400">}}
1. Scroll down to PyCharm Professional and click "Install". PyCharm will download.
   {{< figure src="01-dl-pycharm.png" alt="Select and install pycharm" width="400">}}

## Running PyCharm
1. Click on PyCharm Professional in the JetBrains Toolbox.
1. PyCharm will launch and show license prompts. Select "Activate License" then "Log In to JetBrains Account". 
   {{< figure src="02-activation-prompt.png" alt="PyCharm license activation prompt" width="300">}} {{< figure src="03-activation-options.png" alt="Pycharm activation options" width="300">}}
1. Complete the activation in the web browser. Then go back to PyCharm. You should see that you are signed in. Click "Done" and you should see the main PyCharm launch page.
   {{< figure src="04-home.png" alt="PyCharm launch screen" width="600">}}

1. The Ubuntu "Dash Bar" is on the far left of the screen. Right-click on PyCharm and select "Pin to Dash" to easily launch it.
   {{< figure src="05-pin.png" alt="Pin PyCharm to dash bar" width="300">}}
1. Finally, run the following command in the Ubuntu Terminal, which will create an ***alias*** to run PyCharm from the command line:
{{< card code=true header="**bash**" lang="bash" >}}
printf "pycharm() { nohup ~/.local/share/JetBrains/Toolbox/apps/pycharm-professional/bin/pycharm.sh \"\$@\" >/dev/null 2>&1 & }\n" >> ~/.bashrc && source ~/.bashrc
{{< /card >}}

You should now be good to go to develop Python code in Ubuntu.

## Test drive

We are going to create a sample project directory in Ubuntu, then open PyCharm and edit files in that Linux directory. A video follows the steps.

1. Start a ***new*** Terminal in Ubuntu. 
2. Run the following in the Terminal:
   {{< card code=true header="**bash**" lang="bash" >}}
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
<source src="vb-py-launch.webm" type="video/webm">  
</video>


### Creating a new file
Let's create a file in the Terminal in our project directory. We should see it immediately in PyCharm.

1. Go back to your Ubuntu terminal and make sure you are in the `pycharm-test` directory. 
2. Type the command `touch hello.py` to create an empty Python file.
3. Go back to PyCharm. You should see the file `hello.py` in the directory here. Click on it and it will open an empty editor pane.
4. In the code editor, type `print("Hello World")`. 
5. Go back to the Ubuntu Terminal and type `cat hello.py`. You should see the code.

<video controls autoplay playsinline muted loop width="640">
<source src="hello-vb.webm" type="video/webm">  
</video>

## Next

So you now have PyCharm successfully editing files and interacting with directories inside Ubuntu. 

You are now ready to code! Move on to [PyCharm Basics lab](../../pycharm-basics/).
