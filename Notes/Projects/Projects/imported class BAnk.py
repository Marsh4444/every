from classbankaccount import *

#marsh = BankAccount('marsh', 1_000)
melo = BankAccount('melo', 500)
#marsh.account_details()
#print(marsh.generate_account_number())
#print(marsh.account_number)
#marsh.deposit(100)
#marsh.withdraw(0)
#marsh.transfer(melo, 200)
#marsh.deposit(100)
#print(melo.generate_account_number())
#melo.transfer(marsh, 100)
#marsh = InterestRewardsAcct('marsh', 400)
#marsh.deposit(200)
#marsh.withdraw(150)

joy = BankAccount('joy', 300)
#joy.deposit(200)
#joy.withdraw(150)
joy.transfer(melo, 100)


print(joy.account_number)

print(BankAccount.accounts)

for key, value in BankAccount.accounts.items():
    print(f"{key} → {value.name}, {value.account_number}, ${value.amount}")
