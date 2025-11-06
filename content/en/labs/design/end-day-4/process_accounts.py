"""This module contains functions and classes to support processing bank account information"""
from bankaccount import BankAccount

ACCT_NUM = 0
FIRST_NAME = 1
LAST_NAME = 2
BALANCE = 3


# Yes, you could make the Column names parameters, and that would be a good idea!
def load_data(filename):
    # Violation #1: data filename is hardcoded. Eliminated by making it a variable.
    accounts = []
    with open(filename, encoding='utf-8') as infile:
        next(infile)  # Skip the first line
        for line in infile:
            line = line.strip().split(',')  # transform a line of text into a list of elements
            # Violation of #1: using index integers in line. FIXED.
            new_account = BankAccount(line[ACCT_NUM], line[FIRST_NAME], line[LAST_NAME], line[BALANCE])
            accounts.append(new_account)
    return accounts

def main():
    """Main method that loads data and responds to user commands"""

    filename = input("Enter the data file to load: ")
    # Load the bank account data from a text file into a list.
    # Violation of #2: main() function was loading data AND providing the user interface.
    accounts = load_data(filename)
    print(f"Loaded {len(accounts)} accounts!")

    while True:
        print("Make a selection:")
        print("1) Display account")
        print("0) Exit")

        choice = input()
        if choice == '1':
            acct_num = int(input("Enter an account number: "))
            for acct in accounts:
                if acct.account_num == acct_num:
                    print(acct)
                    break
            else:
                print("Account not found!")
        elif choice == '0':
            print("Goodbye!")
            exit(0)
        else:
            print("I don't understand that option. Try again.")
                    

if __name__ == "__main__":
    main()
