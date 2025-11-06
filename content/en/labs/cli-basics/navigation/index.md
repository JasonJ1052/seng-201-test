---
title: Navigating the file system
description: Use the CLI to move through the filesystem and see its contents.
weight: 5
---


## Part 1: Navigating the File System
### Understanding the File System Structure

Filesystems are follow a "tree" structure for both Windows and Unix-based systems. Specifically, an upside-down or sideways tree. 

{{< figure src="Directory-Filesystem-Hierarchy-Standard.jpg" alt="A graphical representation of the Linux filesystem with the root directory as the base, and other directories under it as descendants." attr="https://linuxconfig.org/wp-content/uploads/2013/03/Directory-Filesystem-Hierarchy-Standard.avif">}} 

#### Key terms and concepts

<mark>**Course Note**: You need to know terms and concepts that ***look like this***.</mark>


***Directories*** hold files and other directories. When you use the term ***subdirectory***, you are talking about the directories listed inside the current working directory.

***Files*** represent programs, pictures, audio, video, word processing docs, etc. Files can be run by the operating system (in the case of programs) or opened by another piece of software, like Photoshop, Microsoft Word, or Python.

The file system has a ***root directory***. On Mac (and Linux), this directory is named `/`. On Windows, it is typically `C:\`.
  - Mac & Linux uses forward slashes (`/`), whereas Windows uses backslashes (`\`). Use forward slashes (`/`) when in POwerShell and it will automatically transform them. Most software programs use `/`.

A user's ***home directory*** is where their user-specific content lives, like documents and pictures that you save. On your personal computer, you probably only have one user. A lab machine will have many different users. 
  - On Linux, the home directory for the user named 'alice' is `/home/alice/`
  - On Mac, it would be `/Users/alice/`
  - On Windows, it would be `c:\Users\alice\`

You can use the Terminal/CLI to ***navigate*** the file system, like you would graphically using the Windows Explorer or Mac Finder. As you navigate with the CLI, you are "in" one directory at a time. The directory that you are currently "in" is called the ***working directory***. Commands run in the context of the working directory. 

<!-- Autocomplete

`sudo apt install tree`
`tree`
`cd /`
`tree` -->

###  Explore the root directory using the `ls` and `cd` commands.
Open a Terminal for Mac or PowerShell for Windows. 
  
Type in the following CLI commands one at a time and see what happens. The commands below have a `#` character, which indicated the beginning of a comment. `# comments` are there for clarification and you do not type them.
{{< card code=true lang="bash" >}}
pwd     # Print the path of the working directory.
ls      # List the files in the current directory.
cd ..   # Go "up" one level in the file tree.
pwd     # Print the path of the working directory.
ls      # This should now list different things.
ls /    # List the files in the root.
cd /    # Change working directory to root.
ls      # list files.
cd ..   # Go up... But it won't go anywhere because you can go higher!
ls      # You're still in the root. List root's files.
{{< /card >}}

None of these commands *change* anything on your computer. They give you information and let you navigate between directories.

**Mac users:** If you encounter a `Permission Denied` error while running the `ls /` or `cd /` commands, try running `sudo ls /` or `sudo cd /`. It will prompt you to enter your password. The `sudo` command makes you an "administrator" in the eyes of the CLI. Mac is protecting the sensitive `/` directory, and wants to make sure you have permission to do what you're trying to do.

### Key Commands
  - `pwd` - Print Working Directory - what is the name of the directory you are currently "in". Use then when you don't know where you are.
  - `ls` - List contents. Will show both subdirectories and files in the working directory.
  - `ls <target>` - List the contents of target directory, e.g., `ls /usr/`
  - `ls -l` (Mac only) - Lists contents and gives you additional information, like the file type. May also do `ls -l <target>`
  - `ll` (Mac only) - Shorthand for `ls -l`. Can do `ll <target>`
  - `cd` - Change Directory. This is how you navigate. 
    - `cd /` changes to the root directory
    - `cd ~` or simply `cd` will navigate to the user's home directory.
    - `cd ..` go "up" one level to the parent of the current directory
    - `cd <target>` changes to the `<target>` directory.

You can "jump" directories by putting the directories full name, like `ls /usr/bin/`. A directory's full name is called its ***path***.

You can also specify ***relative*** paths, which we will discuss more later.

The terminals are capable of ***autocompleting***. Type `cd` to change to your home directory, then type `cd D` then hit the Tab key. What happens? The terminal will find all subdirectories (if any) of your working directory that start with capital D.

<mark>**Extremely important point on Mac, Linux, and in most programs**</mark>: file system names are ***case-sensitive***. For example, you can have files named `user.txt` and `User.txt` and or a directory `/usr/` and `/Usr/` they are different. Capitalization matters in software development. Windows doesn't care about capitalization (sometimes), but you should care.

### Exercise:

1. 
    - (Mac) Navigate to the `/usr/` directory. 
    - (Windows) Navigate to the `C:\Users` directory.
    - Use the `pwd` command to display your current directory. 
2. Type `ls`. What do you see?
2. (Mac only) Now type `ls -l` or `ll`. What do you see?
3. Use `cd ~` to navigate to the home directory. Use `ls` to display the files and folders. What do you see?

### Knowledge Check:

- Question: What does the `pwd` command do?
- Question: How do you navigate to the *root* directory?
- Question: How do you navigate to your *home* directory?


## Next
Move on to [File and directory management](../file-mgmt/).