1) What is Class
A class is a blueprint/template used to create objects.
Think about a house blueprint.
A blueprint might say:
House has a color
House has number of rooms
House has a door
House has windows
But the blueprint itself is not the actual house.
Similarly:
class Employee:
    pass
Employee is a class.
It is a blueprint for creating employee objects.
The class describes what an employee has and what an employee can do.

2) What is an Object?
An object is an actual instance created from a class.
For example:
class Employee:
    pass
emp = Employee()
    You can think of it like:

              Class
          ┌─────────────┐
          │  Employee   │
          │  Blueprint  │
          └──────┬──────┘
                 │
          creates objects
        ┌────────┼────────┐
        ↓        ↓        ↓
      emp1     emp2     emp3


3) Class vs Object
This is one of the most important concepts.
Class	                       Object
Blueprint/template	      Actual instance
Defines structure	        Contains actual data
Logical concept	          Real entity in memory
Created using class	       Created by calling the class
Example: Employee	         Example: emp

Think about a Student ID card design.
The design/template:
Student ID Card
----------------
Name:
Roll No:
Department:
This is like a class.
Actual cards:
Name: Rahul
Roll No: 101
Department: CSE
Name: Priya
Roll No: 102
Department: CSE
These are like objects.

Each object is an individual employee.

4) Creating Multiple Objects
We can create many objects from the same class.
class Employee:
    pass
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
Now we have three different employee objects.
Employee Class
      │
      ├──────────> emp1
      │
      ├──────────> emp2
      │
      └──────────> emp3
They are created from the same blueprint, but they are different objects.

5) Object Identity
Every object has its own identity.
You can check an object's identity using Python's built-in id() function.
class Employee:
    pass
emp1 = Employee()
emp2 = Employee()
print(id(emp1))
print(id(emp2))
You will get different numbers, for example:
140234567890
140234567920

6) Object State
Object state means the data/values currently stored inside an object.
Let's make our Employee class more useful.
class Employee:
    pass
emp = Employee()
emp.name = "Rahul"
emp.salary = 50000
emp.department = "IT"
Now the object contains:
emp
│
├── name = "Rahul"
├── salary = 50000
└── department = "IT"
These values represent the state of the object.

7) Object Behavior
Behavior means what an object can do.
For example, an employee can:
work
calculate salary
introduce themselves
apply for leave
In Python, object behavior is usually represented using methods.
Example:
class Employee:
    def work(self):
        print("Employee is working")
Create an object:
emp = Employee()
Call the method:
emp.work()
Output:
Employee is working
Here:
work()
represents the behavior of the Employee object.

8) What is self?
You will see self everywhere in Python OOP.
For example:
class Employee:
    def work(self):
        print(self.name)
When we do:
emp.work()
Python knows that self refers to:
emp
So conceptually:
emp.work()
is similar to:
Employee.work(emp)
Therefore:
self.name
means:
"Access the name belonging to this particular object."

                            Constructors and self
1) __init__() — Initializing an Object
Consider a real-world Employee.
When an employee joins a company, we need to store information such as:
Name
Employee ID
Salary
Department
In Python:
class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
Now create an employee:
emp1 = Employee("Chandana", 101, 50000, "IT")
Python creates an object and initializes its data.
You can access the data:

print(emp1.name)
print(emp1.emp_id)
print(emp1.salary)
print(emp1.department)

__init__() is a special method that Python automatically calls after an object is created.
class Employee:
    def __init__(self, name):
        print("Employee object initialized")
        self.name = name
emp = Employee("Chandana")
You didn't explicitly write:
emp.__init__("Chandana")
Python effectively performs the initialization process for you.
Conceptually:
emp = Employee("Chandana")
Is __init__() Really a Constructor?
This is a very common interview question.
Strictly speaking:
__init__() is an initializer, not the actual constructor.
Python separates:
Object creation
      ↓
__new__()
      ↓
Object initialization
      ↓
__init__()
__new__()
Responsible for creating the object.
__init__()
Responsible for initializing the already-created object.

class Employee:
    def __new__(cls, name):
        print("__new__() called")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__() called")
        self.name = name
emp = Employee("Chandana")
__init__() is technically an initializer, not the object-creation constructor. __new__() creates the object,
while __init__() initializes it. However, __init__() is commonly referred to as the constructor in everyday Python discussions.

2) self 
Why is self required?
Consider:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
The two sides have different meanings:
self.name = name
Right side
nameis the local parameter.
Left sideself.name
is the instance variable.
What happens if we don't use self?
Consider:
class Employee:
    def __init__(self, name, salary):
        name = name
        salary = salary
This does not store the values in the object.
After:
emp = Employee("Chandana", 50000)
you cannot do:
print(emp.name)
because name was only a local variable inside __init__().
NOTE : self is NOT a Python keyword
This is another interview point.
self is a conventional parameter name, not a keyword.
Technically you could write:
class Employee:
    def __init__(abc, name):
        abc.name = name
This works:
emp = Employee("Chandana")
print(emp.name)
But don't do this in real projects.

3) Instance Method
An instance method works with a particular object's data.
Example:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
emp1 = Employee("Chandana", 50000)
emp2 = Employee("Rahul", 60000)
emp1.display()
emp2.display()
display() is an instance method
