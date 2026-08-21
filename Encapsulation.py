1a) Encapsulation means bundling data and the methods that operate on that data 
inside a class, while controlling how that data can be accessed or modified.
Think about a bank account.
A bank account has:
    Account number
    Account holder name
    Balance
And operations:
    Deposit money
    Withdraw money
    Check balance
You don't want anyone to directly modify the balance like:
  You don't want anyone to directly modify the balance like:
account.balance = -100000
Instead, you want:
account.deposit(5000)
account.withdraw(2000)
The class controls how the data is changed.

1b) Why do we need Encapsulation?
Without encapsulation:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
account = BankAccount(10000)
account.balance = -50000
print(account.balance)
Output:
-50000
  
