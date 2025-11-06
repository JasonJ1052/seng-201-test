---
title: File and directory management
description: Use the CLI to manage files and directories. 
weight: 10
---

By the end of the lab, you should be able to navigate the file system using the CLI, manage files and directories, manipulate text files, understand basic file permissions, and utilize process management commands.

## Part 2: File and Directory Management


<mark>**Reminder:** All file system names a case-sensitive.</mark>

Now, let's practice adding and removing files and directories using the CLI.

### Creating and Removing Directories
- `mkdir` - Make Directory
- `rmdir` - Remove Directory
- `rm -r` - Remove Directory and its contents recursively. ***WARNING***: This is going to delete the directory and everything below it recursively. Linux does not have 'undelete', so be very careful with this command!


The commands below have a `#` character, which indicated the beginning of a comment. `# comments` are there for clarification and you do not type them.

{{< card code=true lang="bash" >}}
cd   # switch to your home directory
mkdir MyLab
ls   # You should see the new MyLab/ directory.
cd MyLab
ls   # You will not see anything. The directory is empty.
cd ..
rm -r MyLab
ls   # MyLab should now be gone
{{< /card >}}

### Creating, Copying, and Deleting Files
- `cp` - Copy Files and Directories
- `rm` - Remove Files
- `mv` - Move or Rename Files


{{< tabpane >}}
{{< tab header="Mac/Linux" lang="bash"  >}}
cd ~  # go to your home directory
ls
touch sample.txt  # Create blank file
ls
cp sample.txt sample_copy.txt
ls
mv sample.txt renamed_sample.txt
ls
rm sample_copy.txt
ls
{{< /tab >}}

{{< tab header="Windows" lang="powershell"  >}}
cd ~  # go to your home directory
ls
echo "hello" > sample.txt  # create a text file containing the string "hello"
ls
cp sample.txt sample_copy.txt
ls
mv sample.txt renamed_sample.txt
ls
rm sample_copy.txt
ls
{{< /tab >}}
{{< /tabpane >}}

<!-- {{< card code=true lang="bash" >}}
cd  # go to your home directory
ls
touch sample.txt
ls
cp sample.txt sample_copy.txt
ls
mv sample.txt renamed_sample.txt
ls
rm sample_copy.txt
ls
{{< /card >}} -->

### Exercise

1. Create a new directory named `LabDirectory`
1. Navigate into this directory using the `cd` command
1. Create a new file named `LabFile.txt` inside this directory. Use `touch`
1. Copy this file to a new file named `LabFileCopy.txt`. Use `cp`
1. Delete `LabFileCopy.txt`. Use `rm`

## Next
Move on to [Text files](../text-files/).