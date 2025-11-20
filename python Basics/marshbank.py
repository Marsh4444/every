import random
import sys

class MarshBank:
    """🏦 A simple Bank Management System built by Marsh."""

    # Class-level dictionary to store all accounts (by name and account number)
    accounts = {}

    def __init__(self, name, balance):
        """Constructor — runs automatically when a new account is created."""
        self.name = name
        self.balance = balance
        self.account_number = self.get_account_number()

        # Register account using both name and account number as keys
        MarshBank.accounts[self.name] = self
        MarshBank.accounts[self.account_number] = self

        print(f"✅ Account created for {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}\n")

    def get_account_number(self):
        """Generates a unique 10-digit account number for each user."""
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    def deposit(self, money):
        """Deposits money into the user’s account."""
        if money < 0:
            print("❌ Invalid deposit amount.")
        else:
            print("Deposit in progress...")
            self.balance += money
            print(f"✅ Deposit completed!\n{self.name} ({self.account_number}) now has a total balance of ${self.balance}.\n")

    def withdraw(self, money):
        """Withdraws money from the user’s account (with basic identity check)."""
        access = input('\nWhich account do you want to access? ')
        if access != self.name:
            print("❌ SCAM ALERT! Unauthorized access detected.")
            sys.exit()  # Ends the program
        else:
            if money < 0:
                print("❌ Invalid withdrawal amount.")
            elif money > self.balance:
                print("❌ Insufficient funds.")
            else:
                print("Withdrawal in progress...")
                self.balance -= money
                print(f"✅ Withdrawal completed!\n{self.name} ({self.account_number}) now has a balance of ${self.balance}.\n")

    def transfer(self, identifier, amount):
        """
        Transfers money from the sender to another account.
        'identifier' can be a name or an account number.
        """
        pass

    def get_balance(self):
        """Returns the user’s balance."""
        return self.balance


# --- Sample Test Run ---
account_1 = MarshBank('Chris', 1000)
account_2 = MarshBank('Ella', 500)

account_1.deposit(200)
account_1.withdraw(100)
account_1.transfer('Ella', 300)
