1. Decorator
A decorator is a function that adds extra functionality to another function without changing its original code.
In simple words:
A decorator wraps an existing function and adds new behavior before or after it runs.

  Why Do We Need Decorators?
Suppose you have 100 functions.

def login():
    print("Login Successful")

def payment():
    print("Payment Done")

def logout():
    print("Logged Out")

Now your manager says:

"Print 'Application Started' before every function."

Without decorators:

def login():
    print("Application Started")
    print("Login Successful")

def payment():
    print("Application Started")
    print("Payment Done")

def logout():
    print("Application Started")
    print("Logged Out")

The same code is repeated many times.

Basic Decorator Structure
def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

Notice
wrapper()

↓

calls

↓

func()

The wrapper adds new behavior.

Example 1: Simple Decorator
def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
def greet():
    print("Hello Python")

greet = decorator(greet)
greet()

Wrapper Function
The wrapper function is the function inside the decorator.
Its job is to:
execute code before the original function
call the original function
execute code after the original function

Example
def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper

  @decorator Syntax
Instead of writing
greet = decorator(greet)
Python provides a shortcut.

@decorator
def greet():

    print("Hello")
This is exactly the same as
def greet():
    print("Hello")
greet = decorator(greet)

ex1: def decorator(func):
    def wrapper():

        print("Welcome")

        func()

        print("Thank You")

    return wrapper
@decorator
def greet():
    print("Python")
greet()



Instead, we use one decorator.
