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
