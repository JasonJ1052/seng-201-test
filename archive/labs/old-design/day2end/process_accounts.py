"""This module contains functions and classes to support processing bank account information"""
from bankaccount import BankAccount

class BankDataError(Exception):
    pass

def search_for_account(accounts, acct_num):
    for acct in accounts:
        if acct.account_num == acct_num:
            return acct
    else:
        raise ValueError("Cannot find account with that number.")

def load_from_file(filename):
    accounts = []

    try:
        with open(filename, encoding='utf-8') as infile:
            next(infile)  # Skip the first line
            for line in infile:
                line = line.strip().split(',')  # transform a line of text into a list of elements
                new_account = BankAccount(line[0], line[1], line[2], line[3])
                accounts.append(new_account)
    except FileNotFoundError:
        raise BankDataError("Error: Cannot find that file.")
    except (ValueError, IndexError):
        raise BankDataError("Error: Bad data in the file. Make sure it file is in proper format.")

    return accounts

def main():
    """Main method that loads data and responds to user commands"""
    
    # Load the bank account data from a text file into a list.
    # DESIGN ISSUE: Not testable
    # DESIGN ISSUE: Not robust against bad data
    accounts : list[BankAccount] = [] 

    while True:
        try:                           
            print("Make a selection:")
            print("1) Display account")
            print("2) Load accounts from a file")
            print("0) Exit")

            choice = input()
            if choice == '1':
                acct_num = int(input("Enter an account number: "))
                acct = search_for_account(accounts, acct_num)
                print(acct)
            elif choice == '2':            
                filename = input("Enter a filename to load: ")
                # This has the effect of wiping out everything that came before.            
                accounts = load_from_file(filename)
                print(f"Loaded {len(accounts)} accounts.")           
            elif choice == '0':
                print("Goodbye!")
                exit(0)
            else:
                print("I don't understand that option. Try again.")
        except (BankDataError, ValueError) as err:
            print(f"Error: {err}")
        
                    

if __name__ == "__main__":
    main()
