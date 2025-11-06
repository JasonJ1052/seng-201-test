---
title: 10. Code-level Design
weight: 999
description: Best practices for organizing functionality.
---


## Motivation
We make references to "writing code *the right way*", but that is secondary to getting the correct answer. After all, how can you get a good grade if it doesn't work?

In software engineering, everything needs to work, but doing it *the right way* is equally important. Why? 
- Because you are on a team, and someone else may have to understand and edit your code. Including your future self. We call this ***understandability***.
- Poorly-implemented solutions are more difficult to change without introducing bugs. We call this ***maintainability***.
- Poorly-implemented solutions may work with small data, but become intolerable with millions of records. We call this ***efficiency***.
- Overly-specific solutions that make assumptions about the data will break when encountering "the real world". Avoiding this is called ***robustness***.

## The Rules

These characteristics are the result of your *code design*. The labs in these sections will go through code-level design principles that you, the developer, are responsible for when writing code. 


We will start with a relatively simple program then add functionality to it. 

In extending this program, we will implement the following design rules that will help improve the ***understandability***, ***maintainability***, ***efficiency***, and ***robustness*** of the software:
1. Separate input/output logic from business logic.
6. Functions should have a single responsibility.
2. Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise.
3. Raise specific errors and define your own if needed.
4. Avoid magic literals.
5. DRY (Don't Repeat Yourself) and the Rule of Three.

**Write these down!** We will explore them in-depth in turn.

## Example program

Imagine you are a bank teller working an old command-line console that provides access to customer's bank accounts. The program does not do much right now, but we will add to it.

Do the following:
1. Create a subdirectory named `bank-accounts/` in your `seng-201/` directory.
2. Download the following files and put them in the `bank-accounts/` directory:
    - [`process_accounts.py`](bank-accounts/process_accounts.py): the main program file that you run.
    - [`bankaccount.py`](bank-accounts/bankaccount.py): defines a `BankAccount` class that is used by the program.
    - [`accounts.csv`](bank-accounts/accounts.csv): a plain text file in Comma-Separate Value (CSV) format. Open it in a text editor (like Visual Studio Code) and also in a spreadsheet program like Excel or Google Sheets. CSV is a common way of sharing tabular data in plain text. 
      - You can read the CSV file in Python the same way you do a plain text file.
      - The first line of the CSV file contains the column headers – descriptive names for each comma-separated value. 
      - Each line of the `accounts.csv` file represents one bank account.
      - The format for each line is
`<AccountNumber>,<FirstName>,<LastName>,<AccountBalance>,<DateOpened>,<DateOfLastTransaction>`
    - [`accounts_bad_numbers.csv`](bank-accounts/accounts_bad_numbers.csv): a data file with strings where there should be numbers.
    - [`accounts_missing_columns.csv`](bank-accounts/accounts_missing_columns.csv): a data file that contains only `<AccountNumber>,<FirstName>,<LastName>`
    - [`accounts_expanded.csv`](bank-accounts/accounts_expanded.csv): more columns added.
    - [`progress.jpg`](bank-accounts/progress.jpg): a file we will use for testing.
3. Run `process_accounts.py`. Select the menu option to view an account, then enter an account number from the CSV file. You should see the account data. Some sample accounts:
   - 796505
   - 872934


## Rules 1&ndash;2
Make sure you have all the files from above in a `bank-accounts/` directory. 

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iEc9o2YsBtk?si=T9qMoYyLrRLCFfI9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### End of Day 1
Here is the code for `process_accounts.py` at the end of the first lecture: [`process_accounts.py`](day1end/process_accounts.py).


## Rules 3&ndash;4

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Alri5LC-hGg?si=uNMuUXEqSoOwRUV3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### End of Day 2
Here is the code for `process_accounts.py` at the end of the second lecture: [`process_accounts.py`](day2end/process_accounts.py).

[`accounts_expanded.csv`](bank-accounts/accounts_expanded.csv): more columns added.

<!-- Let's start with [Rule 1: Separate input/output logic from business logic](../rule-1/) -->