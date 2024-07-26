import json
import os

class Bank(object):
    
    def __init__(self) -> None:
        self.accounts = {}
        self.filename = os.path.join("/home/himanshu/Python.py/OOPs/Bank_project","bank_details.json")
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            self.accounts = {}
    
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.accounts, file, indent=4)
        
    def creating_account(self, name, account_no, balance=0):
        if account_no in self.accounts:
                print("ACCOUNT ALREADY EXIST")
        else:
                self.accounts[account_no] = {
                "name": name,
                "balance": balance                                                          
            }
                self.save_data()
                print("ACCOUNT SUCCESSFULLY CREATED")
        
    def deposit(self,account_no,amount_deposit):
        if account_no in self.accounts:
            self.accounts[account_no]['balance'] += amount_deposit
            print(f"DEPOSITED - ₹{amount_deposit} TO ACCOUNT NO - {account_no}") 
            print(F"NEW BALANCE : ₹{self.accounts[account_no]['balance']}")
            self.save_data()
        else:
            print("ACCOUNT DOES NOT EXIST OR CHECK THE ACCOUNT NUMBER")
            
    def withdraw(self,account_no,amount_withdraw):
        if account_no in self.accounts:
            if self.accounts[account_no]['balance'] >= amount_withdraw:
                self.accounts[account_no]['balance'] -= amount_withdraw
                print(f"WITHDRAW - ₹{amount_withdraw} FROM ACCOUNT NO - {account_no} REMAINING AMOUNT - { self.accounts[account_no]['balance'] - amount_withdraw}")
                self.save_data()
            else:
                print("INSUFFICIENT AMOUNT")
                
    def show_info(self,account_no):
        if account_no in self.accounts:
            print("ACCOUNT DETAILS")
            print(f"NAME            -  {self.accounts[account_no]['name']}")
            print(f"ACCOUNT NUMBER  -  {account_no}")
            print(f"BALANCE         -  ₹{self.accounts[account_no]['balance']}")
            
    def confidential(self):
        for i,(key,value) in enumerate(self.accounts.items()):
            print(F"ACCOUNT NO - {i+1}")
            print(f"ACCOUNT HOLDER  -  {value['name']}")
            print(f"ACCOUNT NUMBER  -  {key}")
            print(f"BALANCE         -  ₹{value['balance']}")
            print()
    
    def delete_account(self,account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
            print("ACCOUNT DELETED SUCCESSFULLY")
            self.save_data()
        else:
            print("ACCOUNT DOES NOT EXIST")
def main():
    bank = Bank()
    print("WELCOME TO OUR BANK")
    
    while True:
        print("\n1. CREATE ACCOUNT")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. GET ACCOUNT INFORMATION")
        print("5. EXIT")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            name = input("ENTER THE HOLDER'S NAME : ") # Convert name input to uppercase
            account_no = input("CREATE THE ACCOUNT NUMBER: ")
            bank.creating_account(name, account_no)
        
        elif choice == '2':
            account_no = input("ENTER THE ACCOUNT NUMBER : ")
            amount = float(input("ENTER THE AMOUNT TO BE DEPOSITED : "))
            bank.deposit(account_no, amount)
        
        elif choice == '3':
            account_no = input("ENTER THE ACCOUNT NUMBER : ")
            amount = float(input("ENTER THE AMOUNT TO BE WITHDRAW : "))
            bank.withdraw(account_no, amount)
        
        elif choice == '4':
            account_no = input("ENTER THE ACCOUNT NUMBER : ")
            bank.show_info(account_no)
        
        elif choice == '5':
            print("THANK YOU FOR USING OUR BANK. GOODBYE!")
            break
        
        elif choice == '28042004':
            print("\nWELCOME TO INNER SERVER OF THE BANK")
            print("1. GET ACCOUNT INFORMATION")
            print("2. DELETE AN ACCOUNT")
            choice2 = input("Enter choice: ")
            if choice2 == "1":
                bank.confidential()
            elif choice2 == "2":
                account_no = input("ENTER ACCOUNT NUMBER TO DELETE : ")
                bank.delete_account(account_no)
            else:
                print("INVALID CHOICE")
                    
        else:
            print("INVALID CHOICE. PLEASE ENTER A VALID OPTION.")

if __name__ == "__main__":
    main()
    
    
    
