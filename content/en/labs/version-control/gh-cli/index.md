---
title: GitHub CLI setup
weight: 16
description: Prepare to work with remote repositories on GitHub
---

## Signup to GitHub

Sign up for a free [GitHub](https://github.com) account if you haven't already. I recommend that you use a permanent, personal email.

## Install the GitHub CLI
Let's install the GitHub CLI, which will make working with remote GitHub repositories easier.

### On MacOS
1. Install Homebrew if you do not have it already. Run the following in the Terminal and follow the on-screen instructions:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Run `brew install gh` and follow the on-screen instructions.

### On your personal Windows computer
Download and install <https://github.com/cli/cli/releases/download/v2.81.0/gh_2.81.0_windows_amd64.msi>

### On a Lab computer
1. Make a directory in your HOME directory named `gh`. For example, `C:\Users\laymanl\gh`
2. Download and unzip <https://github.com/cli/cli/releases/download/v2.81.0/gh_2.81.0_windows_amd64.zip>
3. Open the new directory. Click until you find the `bin` directory inside. Drag that `bin` directory to the `C:\Users\YOUR_ID\gh\` directory you created.
4. Hit the Windows key and search for `user environment variables`. Select the program `Edit the user environment variables for this account`
5. Click the `New` button, then `Browse`
6. A File Explorer will appear. Navigate inside the `C:\Users\YOUR_ID\gh\bin` directory. Click "Okay".
7. Now open a new Terminal window. Run the command `gh` and you should see a list of available commands.

## Login with the GitHub CLI
Run `gh auth login` and follow the onscreen instructions to register your computer with GitHub.
- Leave the default options selected in the CLI. You will hit Enter to open a web browser. Sign into GitHub with your GitHub credentials.
  {{< figure src="terminal.png" alt="GitHub CLI prompt to open browser from the terminal" >}}
	- **If the browser does not open**: manually open a browser to https://github.com/login/device. Sign into GitHub with your GitHub credentials if needed.
- Enter the code shown in the Terminal window.
  {{< figure src="code.png" alt="Enter CLI code in browser" >}}
- Complete the authorization and leave the default options as-is. 

Once you have finished, your Terminal and Browser should look like this:
  {{< figure src="linking-finished.png" alt="CLI and browser success messages once linking finished" >}}

That's it. We are now ready to work with Git and GitHub.