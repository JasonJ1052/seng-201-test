---
title: The Command Line Interface
weight: 10
description: >
  Get to know the software engineer's preferred way of interacting with the OS
---

{{% pageinfo %}}
This is a placeholder page that shows you how to use this template site.
{{% /pageinfo %}}

# Installing Windows Subsystem for Linux (WSL) on Windows 10/11

Windows Subsystem for Linux (WSL) allows you to run a Linux distribution alongside your Windows operating system. Follow these steps to install WSL on your Windows machine.

## Step 1: Enable the WSL Feature

1. Open **PowerShell** as Administrator: Press `Windows Key + X` and select **Windows PowerShell (Admin)**.

1. Run the following command to enable WSL:
  ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

Enable the Virtual Machine Platform (required for WSL 2):

powershell

    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

    Restart your computer to apply the changes.

Step 2: Set WSL 2 as the Default Version (Optional)

If you want to use WSL 2, set it as the default version:

    Open PowerShell as Administrator.

    Run the following command:

    powershell

    wsl --set-default-version 2

Step 3: Install a Linux Distribution

    Open the Microsoft Store.

    Search for the Linux distribution you want to install (e.g., Ubuntu).

    Click Install to download and install the distribution.

Step 4: Initialize Your Linux Distribution

    Once the installation is complete, launch your Linux distribution from the Start Menu.

    Follow the on-screen instructions to complete the setup:
        Set a username.
        Set a password.

Step 5: Update and Upgrade Packages

    Once the Linux distribution is initialized, update and upgrade the package lists by running:

    bash

    sudo apt update && sudo apt upgrade

Additional Commands

    List installed WSL distributions:

    powershell

wsl -l -v

Set a specific WSL version for a distribution:

powershell

wsl --set-version <distribution-name> <version>

Uninstall a Linux distribution:

powershell

    wsl --unregister <distribution-name>

Conclusion

You've successfully installed the Windows Subsystem for Linux on your Windows machine. You can now start using Linux alongside Windows to run your favorite Linux tools and applications.