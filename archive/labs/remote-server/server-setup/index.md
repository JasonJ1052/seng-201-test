---
title: Connecting to ada
weight: 5
description: Instructions for connecting to ada and installing a VPN for offsite work
---

We will use an on-premises (*on-prem*) server called Ada, named after [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace), who wrote the first algorithm for the precursor to modern computers, [Babbage's Analytical Engine](https://www.computerhistory.org/babbage/engines/).


## Offsite - use the VPN client
The `ada` server is accessible only from the UNCW network. 

You will need to use UNCW's Virtual Private Network (VPN) client software to reach the server while offsite. 
1. Install the VPN client software. **You can only install the VPN client while offsite.**
   - **Windows or Mac**: Follow the instructions at https://uncw.teamdynamix.com/TDClient/1875/Portal/KB/ArticleDet?ID=12377. Do this if you are running WSL.
   - **Native Linux**: Point your web browser at https://vpn.uncw.edu and follow the prompts.
2. Open the Cisco AnyConnect VPN program and connect to the pre-configured UNCW VPN. 
3. I recommend that you disconnect from the VPN when you don't need it because it can slow your connection.






## Connecting to `ada` via SSH

We will use the Secure Shell (SSH) program to connect to `ada`. SSH is an extremely popular software tool for creating client-server connections. SSH will connect you to `ada`'s Linux CLI, which will function like a WSL or MacOS Terminal.

SSH is pre-installed on MacOS, Ubuntu, and WSL. Open a Terminal and enter the following:
```bash
ssh <your-uncw-id>@ada.cis.uncw.edu  
# for example, ssh laymanl@ada.cis.uncw.edu
```

Enter your UNCW login password when prompted. Choose "yes" when prompted to trust the connected machine.

You should see something like the following after successfully signing in:
{{<figure src="ada-login.png">}}

You are now logged into the `ada` server. `ada` is running Ubuntu Linux, and understands all the standard Linux [CLI commands](../../cli-basics/).

There are many commands at your disposal, including `python` and `git`. 

Type `pwd` to see your home directory location.

## Rules for using `ada`

`ada` is a shared server. As such:
- Do not read, write, or edit files outside your home directory.
- Do not change the permissions on your home directory using `chmod` or any other command.
- Follow the [Seahawk Respect Compact](https://uncw.edu/about/know-us/respect-compact) at all times.
- Do not intentionally do anything to harm the server, such as fill up the hard disk or overload the CPU.

Activity on the server is logged. Any intentional or negligent violation of these rules will result in a grade of 0 **for the course** and a violation of the Student Code of Conduct reported to the Dean of Students.

When in doubt if you are allowed to do something, ask the instructor first.

## Next
Once you are done, move onto the [Working on `ada` lab](../working-on-ada/).