import random
import sys

class MarshBank:
    """🏦 A simple bank management system that allows users to create accounts,
    deposit, withdraw, transfer funds, and check balances.
    """

    # Class variable (shared across all accounts)
    accounts = {}

    def __init__(self, name, balance):
        """Initialize a new account with name and balance."""
        self.name = name
        self.__balance = balance  # Encapsulated balance for data protection
        self.account_number = self.get_account_number()

        # Register both name and account number as keys pointing to the same object
        MarshBank.accounts[self.name] = self
        MarshBank.accounts[self.account_number] = self

        print(f"✅ Account created for {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}\n")

    # === PROPERTY DECORATORS ===
    @property
    def balance(self):
        """Getter: Returns account balance safely."""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """Setter: Controls how balance is updated (no negative values)."""
        if value < 0:
            print("❌ Balance cannot be negative.")
        else:
            self.__balance = value

    # === METHODS ===
    def get_account_number(self):
        """Generates a unique 10-digit account number for every new user."""
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    def deposit(self, money):
        """Deposit funds into the account."""
        if money <= 0:
            print("❌ Invalid deposit amount.")
            return
        print("💵 Deposit in progress...")
        self.balance += money
        print(f"✅ Deposit completed for {self.name}.")
        print(f"💰 New Balance: ${self.balance}\n")

    def withdraw(self, money):
        """Withdraw funds from account (requires account name validation)."""
        access = input('\nEnter your account name to confirm: ').lower()
        if access != self.name.lower():
            print("❌ SCAM ALERT! Unauthorized access detected.")
            sys.exit()  # Stops the program if name mismatch
        else:
            if money <= 0:
                print("❌ Invalid withdrawal amount.")
            elif money > self.balance:
                print("⚠️ Insufficient funds. Try a smaller amount.")
            else:
                print("🏧 Withdrawal in progress...")
                self.balance -= money
                print(f"✅ Withdrawal successful for {self.name}.")
                print(f"💰 Remaining Balance: ${self.balance}\n")

    def transfer(self, account, funds):
        """Transfer funds to another registered account."""
        receiver = MarshBank.accounts.get(account)  # Fetch receiver using name or number

        if not receiver:
            print("❌ Invalid receiver account.\n")
            return

        # Validate transfer amount
        if funds <= 0:
            print("❌ Invalid transfer amount.")
        elif funds > self.balance:
            print("⚠️ Insufficient balance for transfer.")
        else:
            print("🔁 Transfer in progress...")
            self.balance -= funds
            receiver.balance += funds
            print(f"✅ ${funds} transferred successfully to {receiver.name}.")
            print(f"💰 Your New Balance: ${self.balance}\n")

    def get_balance(self):
        """Return account balance."""
        print(f"💰 Current Balance for {self.name}: ${self.balance}")
        return self.balance

    def account_summary(self):
        """Display a summary of the user's account."""
        return (f"\n📜 Account Summary:\n"
                f"👤 Name: {self.name}\n"
                f"🏦 Account Number: {self.account_number}\n"
                f"💰 Balance: ${self.balance}\n")


# === MENU SYSTEM ===
def menu():
    """Displays user options."""
    print("""
            🌍 Welcome to MarshBank 🏦
            1. Create Account
            2. Deposit
            3. Withdraw
            4. Transfer
            5. Check Balance
            6. Exit
            """)

while True:
    menu()
    prompt = input("👉 Enter your choice: ")

    if prompt == "1":
        name = input("Enter account name: ")
        balance = float(input("Enter initial deposit amount: "))
        MarshBank(name, balance)

    elif prompt == "2":
        acc_no = input("Enter your account number: ")
        acc = MarshBank.accounts.get(acc_no)
        if acc:
            amount = float(input("Enter deposit amount: "))
            acc.deposit(amount)
        else:
            print("❌ Account not found!")

    elif prompt == "3":
        acc_no = input("Enter your account number: ")
        acc = MarshBank.accounts.get(acc_no)
        if acc:
            amount = float(input("Enter withdrawal amount: "))
            acc.withdraw(amount)
        else:
            print("❌ Account not found!")

    elif prompt == "4":
        acc_no = input("Enter your account number: ")
        acc = MarshBank.accounts.get(acc_no)
        if acc:
            receiver_no = input("Enter receiver account name or number: ")
            amount = float(input("Enter transfer amount: "))
            acc.transfer(receiver_no, amount)
        else:
            print("❌ Account not found!")

    elif prompt == "5":
        acc_no = input("Enter your account number: ")
        acc = MarshBank.accounts.get(acc_no)
        if acc:
            acc.get_balance()
        else:
            print("❌ Account not found!")

    elif prompt == "6":
        print("👋 Thank you for banking with MarshBank!")
        break

    else:
        print("⚠️ Invalid choice! Please select from 1–6.")
