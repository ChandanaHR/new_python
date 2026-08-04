1a) What is a Function?
A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you write it once inside a function and call it whenever needed.
Without function
print("Hello Chandana")
print("Welcome!")

print("Hello Rahul")
print("Welcome!")

print("Hello Priya")
print("Welcome!")

Example using function
def greet(name):
    print("Hello", name)
    print("Welcome!")

greet("Chandana")
greet("Rahul")
greet("Priya")

Function Syntax: 5 parts

1b) Different function types
def add(a, b):
    print(a + b)

answer = add(10, 20)

def add(a, b):
    return a + b

answer = add(10, 20)

print(answer)

Docstring
A docstring is a description of what a function does.

It is written inside triple quotes (""" """) immediately after the function definition.
print(answer)
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
Viewing a Docstring

Use the built-in help() function.

def greet():
    """
    Prints welcome message.
    """
    print("Welcome")

help(greet)

Or access it directly.

print(greet.__doc__)

    1c) Python provides different types of functions to perform various tasks. They are mainly classified into three types:

Built-in Functions
User-defined Functions
Anonymous (Lambda) Functions
print()

The print() function displays output on the screen.

print("Hello Python")

What is an Anonymous (Lambda) Function?

An Anonymous Function is a function without a name.

It is created using the lambda keyword.

Why is it called Anonymous?

Because it has no function name.

Normal function

def add(a, b):
    return a + b

Function name

add

Lambda function

lambda a, b: a + b
lambda parameters: expression
Example 1: Add Two Numbers

Normal Function

def add(a, b):
    return a + b

print(add(10, 20))

Lambda Function

add = lambda a, b: a + b

print(add(10, 20))

Output

30
Example 2: Square

Normal Function

def square(x):
    return x * x

Lambda Function

square = lambda x: x * x

print(square(6))

Output

36

Example 3: Cube
cube = lambda x: x ** 3

print(cube(4))

Output

64
Example 4: Find Larger Number
largest = lambda a, b: a if a > b else b

print(largest(10, 20))
