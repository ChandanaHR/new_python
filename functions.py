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
