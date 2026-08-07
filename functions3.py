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

  Decorator with Parameters

Suppose your function accepts arguments.

def add(a,b):

    print(a+b)

The previous decorator won't work because wrapper() accepts no arguments.

Instead, use *args and **kwargs.

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper


@decorator
def add(a,b):

    print(a+b)


add(10,20)

Multiple Decorators

A function can have more than one decorator.

Example

def star(func):

    def wrapper():

        print("********")

        func()

        print("********")

    return wrapper


def hash_symbol(func):

    def wrapper():

        print("########")

        func()

        print("########")

    return wrapper


@star
@hash_symbol
def message():

    print("Hello")


message()
Execution Order
@star
@hash
↓
star(hash(message))

Timing Decorator
Used to calculate how much time a function takes.
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end-start)

        return result

    return wrapper


@timer
def square():

    total = 0

    for i in range(1000000):

        total += i


square()

Caching Decorator
Suppose a calculation is expensive.
Instead of calculating repeatedly,
store the answer.

def cache(func):
    memory = {}
    def wrapper(n):
        if n in memory:
            return memory[n]
        result = func(n)
        memory[n] = result
        return result
    return wrapper
@cache
def square(n):
    print("Calculating...")
    return n*n


print(square(5))
print(square(5))

GEnerators
A generator is a special type of function that returns values one at a time using the yield keyword, instead of returning all values at once.
A generator generates values one by one whenever they are requested.
Why Use Generators?
Suppose you need numbers from 1 to 1,000,000.
Using a List
numbers = list(range(1000000))
Python creates all one million numbers immediately.
This uses a lot of memory.
Using a Generator
numbers = (x for x in range(1000000))
Python creates only one number at a time.
This saves memory.
Generator Function

A normal function uses return.
def greet():
    return "Hello"
A generator uses yield.
def numbers():
    yield 1
  yield
What is yield?
yield is used to produce one value and pause the function.
Unlike return, it does not terminate the function completely.
Instead, it remembers its current state.
return	                           yield
Ends the function	                 Pauses the function
Returns one value                	Can produce many values
Function is destroyed           	Function remembers its state
def numbers():

    yield 1

generator = numbers()

print(generator)

def numbers():

    yield 1

generator = numbers()

print(next(generator))

def numbers():

    yield 10

    yield 20

    yield 30

generator = numbers()

print(next(generator))

print(next(generator))

print(next(generator))

next() is used to retrieve the next value from a generator.
Each call to next() resumes execution from where the previous yield paused.

Generator Expression
Just like list comprehensions, Python provides generator expressions.
List Comprehension
numbers = [x*x for x in range(5)]
print(numbers)
Output
[0, 1, 4, 9, 16]
Everything is stored in memory.

Generator Expression
numbers = (x*x for x in range(5))
print(numbers)
Output
<generator object ...>
Nothing is calculated yet.
Accessing Values
numbers = (x*x for x in range(5))
for num in numbers:
    print(num)

  Practical Example 1: Squares
def squares():
    for i in range(1,6):
        yield i*i
for num in squares():
    print(num)

  Disadvantages of Generators
Values cannot be accessed by index.
g = (x for x in range(5))

print(g[0])

Output

TypeError
Once a generator is exhausted, it cannot be reused.
g = (x for x in range(3))

for i in g:
    print(i)

for i in g:
    print(i)

Output

0
1
2

The second loop prints nothing because the generator has already been consumed.

What is a Higher-Order Function?
A Higher-Order Function (HOF) is a function that does at least one of these:
Takes another function as an argument, or
Returns another function.

Example 1: Function as an Argument
def greet():
    print("Hello Python")
def execute(func):
    func()
execute(greet)

Output
Hello Python

Higher-Order Function Returning a Function

A higher-order function can also return another function.

def outer():

    def inner():
        print("Hello")

    return inner

fun = outer()

fun()

Output

Hello

This is also an example of a closure.

Callback Functions
What is a Callback Function?
A callback function is a function that is passed as an argument to another function and is called later by that function.
Simple Definition:
A callback is a function that another function executes when needed.
