1a) Inheritance in Python
Inheritance allows one class to acquire the properties and methods of another class.
Think of it like parents passing common characteristics to their children.

Why is Inheritance required?
The biggest reason is code reusability.
Suppose you don't use inheritance.
You might write:
class Car:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")
class Bike:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")
Notice something?
Both Car and Bike have the same methods:
start()
stop()
We are repeating code.
This violates the idea:
Don't Repeat Yourself (DRY)

Parent Class / Superclass / Base Class
These three terms generally refer to the same thing:
Parent class
Superclass
Base class
Suppose:
class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")
Here:
Vehicle is the parent class.

Child Class / Subclass / Derived Class
Now suppose we create:
class Car(Vehicle):
    pass
Here:
Car
is the child class.
It is also called:
Subclass
Derived class
So:
Vehicle → Parent
Car     → Child

  Child can also have its own features
Inheritance doesn't mean the child can only use the parent's functionality.
The child can add its own methods.
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def write_code(self):
       print("Developer is writing code")
Now:
developer = Developer()
developer.work()
developer.write_code()

1b) Types of Inheritance
  1b1) Single Inheritance
Meaning
When one child class inherits from one parent class, it is called Single Inheritance.
Parent
  │
  ↓
Child
  class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car = Car()
car.start()
car.drive()

1b2) Multiple Inheritance
Meaning
When one child class inherits from multiple parent classes, it is called Multiple Inheritance.
Parent 1      Parent 2
    \            /
     \          /
       ↓      ↓
        Child
  class Camera:
    def take_photo(self):
        print("Taking photo")
class Phone:
    def make_call(self):
        print("Making phone call")
class SmartPhone(Camera, Phone):
    def browse(self):
        print("Browsing internet")
phone = SmartPhone()
phone.take_photo()
phone.make_call()
phone.browse()

1b3) Multilevel Inheritance
Meaning
When inheritance happens in multiple levels, it is called Multilevel Inheritance.
Grandparent
     ↓
   Parent
     ↓
   Child
  class Person:
    def introduce(self):
        print("I am a person")
class Employee(Person):
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")
developer = Developer()
developer.introduce()
developer.work()
developer.write_code()

1b4) Hierarchical Inheritance
Meaning
When multiple child classes inherit from the same parent class, it is called Hierarchical Inheritance.
             Parent
            /      \
           ↓        ↓
        Child 1   Child 2
  class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
  dog = Dog()

dog.eat()
dog.bark()

1b5) Hybrid Inheritance
Meaning
Hybrid inheritance is a combination of two or more types of inheritance.
For example, we can combine:
Multiple inheritance
Hierarchical inheritance
Real-world example
Imagine:
                  Person
                 /      \
                ↓        ↓
           Employee     Student
                \        /
                 \      /
                   ↓
               WorkingStudent
With inheritance, we can move common functionality into a parent class.
