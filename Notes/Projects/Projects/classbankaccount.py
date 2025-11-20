import random

class BankAccount:
    """Creating a bank account where users can deposit ,transfer ,send and check balance
    """

    #A global variable
    accounts = {} #created an empty dictionary
    
    def __init__(self, account_name, account_amount = 0):
        """Constructor of Bank"""
        self.name = account_name.title()
        self.amount = account_amount
        self.account_number = self.generate_account_number()#why did we use this expression

        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.amount:.2f}")

    #Register account by name and number
        BankAccount.accounts[self.name] = self
        BankAccount.accounts[self.account_number] = self

        
        # Only generate if user doesn’t already exist
        #if account_name.title() not in BankAccount.accounts:
         #   self.account_number = self.generate_account_number()
        #else:
         #   self.account_number = BankAccount.accounts[account_name].account_number

    def account_details(self):
        """Gets the account details of the usser"""
        print(f"\nAccount Name: {self.name}\n\nAccount Balance: {self.amount}")
        print(f"\nAccount summary:\n\nThe account of {self.name}, as an account balance of {self.amount}\n")

    def  account_balance(self):
        """Gets the balance of the account"""
        print(f"\nYour Balance: {self.amount}")

    def generate_account_number(self):
        """Generates users account number"""
        account_num = ''.join(str(random.randint(0, 9)) for _ in range(10))
        #user_no = f"\n{self.name}, This is your Account number: {account_num}"
        return account_num

    def deposit(self, money):
        """Add money to the account."""
        if money > 0:
            self.amount += money
            print(f"\nDeposit in progress\nDeposit to {self.name} is completed ✅✅, Your account as been updated\n")
            self.account_balance()
            #print(f"\n✅ {money} deposited successfully.\nNew balance: {self.amount}\n")
        else:
            print("\n❌ Invalid deposit amount")

    def withdraw(self, money):
        """Withdraw money from the account."""
        if 0 < money <= self.amount:
            self.amount -= money
            print(f"\n✅ {money} withdrawn successfully.\nNew balance: {self.amount}\n")
        else:
            print("\n❌ Insufficient balance or invalid amount")

    
    def transfer(self, account, money):
        """Transfer money to another account using name or account number."""
        #receiver = account
        #receiver = BankAccount.accounts.get(account) #get() is a dictionary method used to retrieve a value for a given key —without causing an error if the key doesn’t exist.
        if account:
            if money > 0 and self.amount >= money:
                self.withdraw(money)
                account.deposit(money)#this line keeps giving attribute error
                print(f"\n💸 {money} transferred successfully to {account.name}")
            else:
                print("\n❌ Transfer failed: insufficient funds or invalid amount")
        else:
            print("\n❌ Receiver not found (check name or account number)")


#creating a baby class that inherits from the BankAccount class as the parent class

class InterestRewardsAcct(BankAccount):
    """Adds interest to bank account deposit"""

    def deposit(self, money):
        self.amount = self.amount + (money * 1.05)#we overite the former attribute 
        print("\nDeposit complete.")
        self.account_balance()

#Creating another class that inherits the InterestRewardsAcct

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name): 
        super().__init__(initial_amount, acct_name)#lets us quickly reach parent class methods or constructors from the child class
        self.fee = 5 #we then give another attribute to this class

    def withdraw(self, money):
        if self.amount >= money:
            self.amount -= (money + self.fee)
            print("\nWithdraw completed.")
            self.account_balance()

        else: 
            print(f'\nWithdraw interrupted: you dont have sufficient balance')




            
             
            
        


















    
