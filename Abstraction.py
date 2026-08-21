Abstraction
1a) Show only what is necessary and hide the implementation details.

Real-World Example of Abstraction
Think about using an ATM.
When you withdraw money, you do:
Insert Card
    ↓
Enter PIN
    ↓
Choose Withdraw
    ↓
Enter Amount
    ↓
Receive Money
You don't need to know:
How the bank verifies your account
How the database is queried
How the bank communicates with its server
How the transaction is processed
How the ATM communicates with the banking system
You only interact with the necessary interface.
That's abstraction.

In programming
You might write:
atm.withdraw(5000)
You don't care about the internal implementation of withdraw().

1b) What is an Abstract Class?
An abstract class is a class that is designed to be a blueprint/base class for other classes.
It usually contains one or more abstract methods.
Python provides the abc module for creating abstract classes.
        from abc import ABC, abstractmethod
ABC → used to create an Abstract Base Class
@abstractmethod → used to declare an abstract method
Basic Abstract Class Example

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
      Animal is an abstract class.
      sound() is an abstract method.

1c) What is an Abstract Method?
An abstract method is a method that declares what a subclass must implement, but the base class doesn't provide the actual implementation.
Every Animal must have a sound() method, but I don't know what sound each animal makes.

Implementing the Abstract Class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
Animal says:
def sound(self):
but doesn't decide how sound should be produced.

1d) Why Can't We Create an Object of an Abstract Class?
Try:
animal = Animal()
Python will give an error similar to:
TypeError: Can't instantiate abstract class Animal
with abstract method sound
Because Animal is incomplete.
It says:
"Every animal must have a sound."

1e) Abstract Class Can Have Normal Methods
An abstract class doesn't have to contain only abstract methods.
Example:
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_company(self):
        print("Company: ABC Technologies")
But it doesn't define the actual sound.
Therefore Python doesn't allow us to create an object directly from it.
class Developer(Employee):
    def calculate_salary(self):
        print("Salary = ₹80,000")
dev = Developer()
dev.calculate_salary()
dev.display_company()

1f) Abstract Class With Constructor
You can also have __init__() inside an abstract class.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print(f"{self.name} writes code")
dev = Developer("Chandana")
dev.work()

