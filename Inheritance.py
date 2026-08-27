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

1c) Constructor Inheritance in Python
Let's understand this carefully because constructor inheritance can be confusing at first.
1. First: What is a constructor?
In Python, __init__() is commonly called the constructor.
It is automatically executed when we create an object.
class Student:
    def __init__(self):
        print("Student constructor called")
s1 = Student()
Output:
Student constructor called
When we write:
s1 = Student()
Python automatically calls:
Student.__init__()
2. What happens when inheritance is used?
Consider:
class Person:
    def __init__(self):
        print("Person constructor")
class Student(Person):
    pass
s = Student()
Output:
Person constructor
But notice:
class Student(Person):
    pass
Student doesn't have its own __init__().
So what happens?
Python looks for a constructor in Student.
It doesn't find one.
Then it looks in the parent class:
Student
   ↓
Does Student have __init__()? ❌
   ↓
Look in Person
   ↓
Person has __init__()? ✅
   ↓
Call Person.__init__()
Therefore:
Person constructor
is printed.
Important rule
If the child class doesn't define its own __init__(), the parent's __init__() can be used.
ex2) class Person:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
class Student(Person):
    pass
student = Student("Chandana")
student.display_name()

What if the child has its own constructor?
Now consider:
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, roll_no):
        self.roll_no = roll_no
student = Student(101)

1d) super() in Python
super() is mainly used in inheritance to access the parent class's methods and constructor from the child class.
The easiest way to remember it is:
super() means "go to the parent class and use its functionality."
Why do we need super()?
Consider this example:
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display_student(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

So:
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

ex2) class Parent:
    def show(self):
        print("Parent show method")
class Child(Parent):
    def display(self):
        super().show()
obj = Child()
obj.display()
ex3) super with constructor
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        print("Student constructor")
student = Student("Chandana", 101)
print(student.name)
print(student.roll_no)

ex4) class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        print("Employee constructor")
class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language
        print("Developer constructor")
developer = Developer(
    "Chandana",
    101,
    "Python"
)

1e) isinstance() and issubclass()
Very important for interviews.
isinstance()
Checks whether an object belongs to a class or its subclasses.
dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
issubclass()
Checks the relationship between classes.
print(issubclass(Dog, Animal))

super() vs Direct Parent Class Call
Without super()
Employee.work(self)
With super()
super().work()

IS-A → Inheritance
HAS-A → Composition / Association

IS-A Relationship
An IS-A relationship means one class is a type of another class.
For example:
Dog IS-A Animal
Car IS-A Vehicle
Developer IS-A Employee
Student IS-A Person
IS-A Relationship
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog = Dog()
dog.eat()
dog.bark()

HAS-A Relationship
A HAS-A relationship means one object/class contains or uses another object.
For example:
Car HAS-A Engine
House HAS-A Room
Computer HAS-A Keyboard
University HAS-A Students
The important question is:
Does one object have/use another object?


Association means:
Two objects are related to or interact with each other, but neither object necessarily owns the other.
In simple words:
"They know/use each other."
Real-world example
A:
Teacher
and:
Student
have a relationship.
class Student:
    def study(self):
        print("Student is studying")
class Teacher:
    def teach(self, student):
        print("Teacher is teaching")
        student.study()
student = Student()
teacher = Teacher()
teacher.teach(student)
Another Association Example
Consider:
Doctor ───── Patient
A doctor treats a patient.
But:
Doctor can exist without a particular patient.
Patient can exist without a particular doctor.
The doctor doesn't own the patient's lifecycle.

Composition is a strong HAS-A relationship.
It means:
One object strongly owns another object, and the contained object's lifecycle is tied to the owner.
The easiest real-world example is:
Car HAS-A Engine
When we design the Car to create and own its Engine:
Car
 |
 └── Engine
The Engine is a component of that particular Car.

class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
        print("Car started")
car = Car()
car.start()
