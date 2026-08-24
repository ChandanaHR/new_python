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

With encapsulation:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
account = BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)
print(account.get_balance())
The user doesn't directly manipulate the internal balance.


1c) Access Control in Python
Python doesn't have strict access modifiers like Java:
public
private
protected
Instead, Python uses naming conventions.
There are mainly three levels:
Syntax	Meaning
name	Public
_name	Protected convention
__name	Private/name mangling

1c1) Public Members
A public member can be accessed from anywhere.
Example:
class Employee:
    def __init__(self):
        self.name = "Chandana"
        self.salary = 50000
employee = Employee()
print(employee.name)
print(employee.salary)
Output:
Chandana
50000
You can also modify them:
employee.name = "Rahul"
employee.salary = 60000
So:
self.name
self.salary
are public attributes.

1c2) Protected Members — _name
Python uses a single underscore to indicate that a member is intended for internal or subclass use.
Example:
class Employee:
    def __init__(self):
        self.name = "Chandana"
        self._salary = 50000
employee = Employee()
print(employee.name)
print(employee._salary)
Python does not actually prevent access.
The underscore is a convention.
It tells other developers:
"This is intended for internal use. Please don't access it directly unless you know what you're doing."
    Protected with inheritance
This is where _name becomes particularly useful.
class Employee:
    def __init__(self):
        self._salary = 50000
class Manager(Employee):
    def show_salary(self):
        print(self._salary)
manager = Manager()
manager.show_salary()
Output:
50000
The child class can access _salary.
So conventionally:
name       → Public
_name      → Internal / subclass use


1c3) Private Members — __name
Two underscores indicate a private-style member.
Example:
class BankAccount:
    def __init__(self):
        self.__balance = 10000
Now:
account = BankAccount()
print(account.__balance)
You'll get:
AttributeError
Why?
Because Python performs name mangling.
..........What is Name Mangling?
This is an important interview question.
When Python sees:
self.__balance
inside a class, it internally changes the name approximately to:
self._BankAccount__balance
So:
class BankAccount:
    def __init__(self):
        self.__balance = 10000
Internally becomes approximately:
_BankAccount__balance
You can technically access it:
account = BankAccount()
print(account._BankAccount__balance)
Output:
10000
But you should not do this in normal application code


1d) Getter and setters
Suppose:
class Employee:
    def __init__(self):
        self.__salary = 50000
We don't want users directly accessing:
employee.__salary
So we provide methods.
Getter
A getter is used to read data.
def get_salary(self):
    return self.__salary
Setter
A setter is used to modify data.
def set_salary(self, salary):
    if salary > 0:
        self.__salary = salary
Complete example:
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")


employee = Employee(50000)

print(employee.get_salary())

employee.set_salary(60000)

print(employee.get_salary())

Output:

50000
60000

Invalid value:

employee.set_salary(-10000)

Output:

Invalid salary

This is controlled access.

1e) Real world example
class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.__balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Amount withdrawn successfully")

    def get_balance(self):

        return self.__balance

    account = BankAccount("Chandana", 10000)
print(account.account_holder)
print(account.get_balance())
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())

Why not simply use Getter/Setter methods?
We can write:
employee.get_salary()
employee.set_salary(60000)
But Python gives us a much cleaner approach:
employee.salary
while still running getter/setter logic behind the scenes.
This is where:
⭐ @property
comes in.

class Employee:
    def __init__(self, salary):
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive")

Now:
employee = Employee(50000)
print(employee.salary)
employee.salary = 60000
print(employee.salary)
