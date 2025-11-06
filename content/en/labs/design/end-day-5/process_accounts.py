"""This module contains functions and classes to support processing bank account information"""
from bankaccount import BankAccount

ACCT_NUM = 0
FIRST_NAME = 1
LAST_NAME = 2
BALANCE = 3


# Yes, you could make the Column names parameters, and that would be a good idea!
def load_data(filename: str):
    """
    Read data from a CSV file, and return a list of BankAccount objects.
    - File not present
    - content not in the expected format: CSV with appropriate # of columns
    - make sure file isn't empty

    :param filename this should be a string of the relative filename
    :return list of BankAccount objects based on the file content.

    """

    # Violation #1: data filename is hardcoded. Eliminated by making it a variable.
    accounts = []
    with open(filename, encoding='utf-8') as infile:
        next(infile)  # Skip the first line
        for line in infile:
            line = line.strip().split(',')  # transform a line of text into a list of elements
            # Violation of #1: using index integers in line. FIXED.
            new_account = BankAccount(line[ACCT_NUM], line[FIRST_NAME], line[LAST_NAME], line[BALANCE])
            accounts.append(new_account)

    if not accounts:
        raise ValueError("That file is empty! Try again.")
    return accounts

def file_search(accounts: list[BankAccount], acct_num: int) -> BankAccount:
    for acct in accounts:
        if acct.account_num == acct_num:
            return acct

    raise ValueError("Account not found!")

def main():
    """Main method that loads data and responds to user commands"""

    accounts = []
    # while accounts == []:
    while not accounts:
        filename = input("Enter the data file to load: ")
        # Load the bank account data from a text file into a list.
        # Violation of #2: main() function was loading data AND providing the user interface.
        try:
            accounts = load_data(filename)
        except FileNotFoundError:
            print("Could not find that file. Try again.")
        except (IndexError, ValueError, UnicodeDecodeError) as err:
            print("File is in a bad format. Try again.", err)

    print(f"Loaded {len(accounts)} accounts!")

    while True:
        print("Make a selection:")
        print("1) Display account")
        print("0) Exit")

        choice = input()
        if choice == '1':
            # Exercise:
            # a) extract the search functionality into a function
            # b) Have it raise an exception if the account number is not found
            # c) Handle the user input and the exception in main()
            try:
                print(file_search(accounts, int(input("Enter an account number: "))))
            except ValueError as verr:
                print(verr)

        elif choice == '0':
            print("Goodbye!")
            exit(0)
        else:
            print("I don't understand that option. Try again.")
                    

if __name__ == "__main__":
    main()
