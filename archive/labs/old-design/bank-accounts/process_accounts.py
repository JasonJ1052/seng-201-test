"""This module contains functions and classes to support processing bank account information"""
from bankaccount import BankAccount


def main():
    """Main method that loads data and responds to user commands"""
    
    # Load the bank account data from a text file into a list.
    accounts : list[BankAccount] = [] 
    with open("accounts.csv", encoding='utf-8') as infile:
        next(infile)  # Skip the first line
        for line in infile:
            line = line.strip().split(',')  # transform a line of text into a list of elements
            new_account = BankAccount(line[0], line[1], line[2], line[3])
            accounts.append(new_account)
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
