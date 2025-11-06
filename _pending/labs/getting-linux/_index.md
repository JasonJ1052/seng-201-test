---
title: 01. Installing a *nix operating system
weight: 5
description: In this lesson, you will set up an operating system in the Unix family.
---

Most commercial software runs on Linux. Linux is derived from an OS called Unix. So are Android, macOS, and iOS. 

Windows and Unix-derived operating systems do the same things, but the specific commands you type and the way you set up your user environment differ between the OS families. 

## Mac users

You don't need to do anything. macOS is derived from Unix, so everything we do in Linux you should be able to do in macOS. There will be a few minor differences. 

Just don't tell anyone that you're using Linux on a Mac, because you are not! macOS is not Linux, but they speak the same language and have many of the same command line tools.

## Windows users

You will install Ubuntu Linux, which will require 18-30GB of disk space. 

You will continue to run Windows, but we will use ***virtualization tools*** to install Linux and make it think that it is running on actual hardware, when in reality it is running "inside" Windows. The virtualization tools pass OS commands from Linux to Windows, and Windows ultimately controls the hardware. Linux will act like a "computer within a computer".

Scroll to the appropriate section:
- [If you use a lab computer](#if-you-use-a-lab-computer)
- [If you use a personal computer](#if-you-use-a-personal-computer)

### If you use a lab computer
You will use a program called VirtualBox to install and use Linux. VirtualBox is already installed in CG 2055 and CG 2004. 

1. Follow this tutorial <https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview>. There are 5 pages in the tutorial.
    - This tutorial includes downloading VirtualBox, downloading an Ubuntu .iso image, and installing Ubuntu inside a VirtualBox Virtual Machine.
    - **Important Note:** In Step 2 of the tutorial, *do not* put create "machine folder" inside of folder that is backed up by OneDrive or Google Drive. Mine defaults to  `c:\Users\laymanl\VirtualBoxVMs`, which is fine.
1. The VM should start automatically.
1. An Ubuntu installer application should be running inside the VM with a screen like the following:
    {{< figure src="vb-installing-ubuntu.png"  width="600" alt="Installation screen inside the VM" >}}
    Allow this program to finish `Copying files...` It may take a long time. 
1. Once the installer application finishes, you will be prompted to login using the username and password you created while following the tutorial.
1. You should see the Ubuntu desktop and a Welcome application. You can skip through the Welcome application without installing anything it recommends. 
    {{< figure src="vb-ubuntu-home.png"  width="600" alt="Installation screen inside the VM" >}}
1. Finally, in the VirtualBox menu bar at the top, select Device &rarr; Shared Clipboard &rarr; Bidirectional for a quality of life improvement. You are now good to go!
    {{< figure src="vb-clipboard.png"  width="500" alt="Enabling bidirectional clipboard in VirtualBox" >}}

### If you use a personal computer

You will enable a virtualization feature called the Windows Subsystem for Linux (WSL) and install a Linux distribution. 

1. Press the Windows key and search for "windows features". Select the "Turn Windows features on or off" option.
    {{< figure src="windows-features.png" width="640" alt="Searching for Windows Features options" >}}
1. Scroll down and ensure that "Virtual Machine Platform" and "Windows Hypervisor Platform" are both checked. Hit "OK". 
    {{< figure src="feature-options.png" width="480" alt="Turning on Windows virtualization support" >}}
1. Reboot your computer if prompted to do so.
1. Hit your Windows key, search for PowerShell. Right click it and "Run as Administrator".
    {{< figure src="powershell.png" width="640" alt="Opening powershell" >}}
1. In Powershell, run the command `wsl --install`. This may take a while to complete.
1. Reboot your computer.
1. Open the Microsoft Store app on your computer. Search for "Ubuntu" and get the "Ubuntu 24.04 LTS" app. This will take some time to complete.
    {{< figure src="choose-distribution.png" alt="Finding ubuntu on the microsoft store" >}}
1. Ubuntu will then be installed on your machine. Once installed, you can either launch the application directly from the Microsoft Store or search for Ubuntu in your Windows search bar.
    {{< figure src="search-ubuntu-windows.png" alt="Open Ubuntu from windows" >}}
1. Follow the instructions in the Ubuntu terminal to create a username and password for Linux. **Note that Linux will *not* show the password as you type.**
1. Once everything is complete, you should see a prompt similar to "username@computer_name" on your screen, e.g.:
   {{< figure src="prompt.png" alt="Linux command prompt" >}}

Follow the instructions for Method 1 here: <https://canonical-ubuntu-wsl.readthedocs-hosted.com/en/latest/guides/install-ubuntu-wsl2/>







