Parameters and arguments
2a) Positional Arguments

In positional arguments, values are assigned to parameters based on their position.

Syntax
def add(a, b):
    return a + b

Here

a → First parameter
b → Second parameter

Calling the function

print(add(10, 20))
def student(name, age):
    print("Name:", name)
    print("Age :", age)

student("Rahul", 22)
Wrong Position
student(22, "Rahul")

Output

Name: 22
Age : Rahul

Python only looks at the position, not the meaning.

2b Keyword Arguments

Instead of passing values by position, we pass them using parameter names.

Example

def add(a, b):
    return a + b

print(add(a=10, b=20))

Output

30

Order doesn't matter.
def student(name, age):
    print(name)
    print(age)

student(age=22, name="Rahul")

2c) Default Arguments

A default argument has a value already assigned.

If the user doesn't provide a value, Python uses the default.

Example

def greet(name="Guest"):
    print("Hello", name)

Calling

greet()
Providing a value

greet("Chandana")

Output

Hello Chandana

Python replaces "Guest" with "Chandana".

2d) Variable-Length Arguments
Sometimes we don't know how many arguments the user will pass.

Python provides

*args
**kwargs

*args

*args collects multiple positional arguments into a tuple.

Example1)

def total(*numbers):
    print(numbers)

total(10,20,30)

Output

(10, 20, 30)

Python creates a tuple automatically.

Example 2
def total(*numbers):
    print(sum(numbers))

total(10,20)
total(10,20,30)
total(10,20,30,40)

**kwargs

**kwargs collects multiple keyword arguments into a dictionary.

Example

def student(**data):
    print(data)

student(name="Rahul", age=22)

Output

{'name': 'Rahul', 'age': 22}

Example 2
def employee(**details):
    for key, value in details.items():
        print(key, ":", value)

employee(name="Chandana",
         salary=50000,
         city="Bangalore")

Output

name : Chandana
salary : 50000
city : Bangalore

Combining Arguments

Python allows all argument types in one function.

Example

def demo(a, b=5, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

demo(10,20,30,40,name="Rahul",city="Bangalore")

Output

a = 10
b = 20
args = (30, 40)
kwargs = {'name': 'Rahul', 'city': 'Bangalore'}

3) Return statements
Multiple Returns
Python can return multiple values separated by commas.
Example
def calculate(a,b):
    return a+b, a-b
result = calculate(20,10)
print(result)

Output

(30,10)

Python actually returns a tuple.

Unpacking
sum_result, diff_result = calculate(20,10)

print(sum_result)
print(diff_result)

Output

30
10

Returning a List
A function can return a list.
Example
def colors():
    return ["Red","Green","Blue"]
print(colors())
Output
['Red', 'Green', 'Blue']

Returning a Dictionary
A function can return a dictionary.
Example
def student():
    return {
        "name":"Rahul",
        "age":22,
        "city":"Bangalore"
    }

print(student())

Output

{'name':'Rahul','age':22,'city':'Bangalore'}

Returning Objects
A function can return an object created from a class.
Example
class Student:

    def __init__(self,name):
        self.name=name

def create_student():
    return Student("Rahul")

student = create_student()

print(student.name)

Returning Functions
In Python, a function can return another function.
Example
def outer():
    def inner():
        print("Hello Python")
    return inner
message = outer()
message()

Built - in functional programming
Functional programming is a programming style where functions are used to process data instead of writing long loops.
Python provides several built-in functions that make code shorter, cleaner, and easier to read.

map()
What is map()?
map() applies the same function to every element in a collection (like a list or tuple).
syntax: map(function, iterable)
Example 1: Square Every Number

Without map()
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    result.append(num * num)
print(result)
Output
[1, 4, 9, 16, 25]

Using map()
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x*x, numbers)
print(list(result))
Output
[1, 4, 9, 16, 25]

Example 2: Convert Names to Uppercase
names = ["rahul", "john", "chandana"]
upper = map(str.upper, names)
print(list(upper))

filter()
What is filter()?
filter() keeps only the elements that satisfy a condition.
Syntax
filter(function, iterable)
Example 1: Even Numbers
numbers = [1,2,3,4,5,6,7,8]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

Example 2: Marks Greater Than 50
marks = [35, 75, 40, 90, 60]
passed = filter(lambda x: x >= 50, marks)
print(list(passed))

reduce()
What is reduce()?
reduce() combines all elements into one final value.
It is available in the functools module.
        from functools import reduce
Syntax: reduce(function, iterable)
example1): from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda a,b: a+b, numbers)

print(result)

example2: from functools import reduce

numbers = [15, 25, 8, 90, 40]

largest = reduce(lambda a,b: a if a>b else b, numbers)

print(largest)

zip()
What is zip()?
zip() combines two or more lists element by element.
ex1: names = ["Rahul", "John", "Anu"]
marks = [80,90,70]
result = zip(names, marks)
print(list(result))

ex2: names = ["A","B","C"]
marks = [90,80,70]
cities = ["Delhi","Mumbai","Bangalore"]
print(list(zip(names, marks, cities)))

enumerate()
What is enumerate()?
Adds an index number to each element.
a Without enumerate()
fruits = ["Apple","Banana","Orange"]
for fruit in fruits:
    print(fruit)

Output
Apple
Banana
Orange

With enumerate()
fruits = ["Apple","Banana","Orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

Output
0 Apple
1 Banana
2 Orange

Start Index from 1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
Output
1 Apple
2 Banana
3 Orange


any()
What is any()?
Returns True if at least one value is True.
Think of it as "Is anyone successful?"

Example
numbers = [False, False, True]
print(any(numbers))

Output
True
Because at least one value is True.


Another Example
numbers = [0,0,5]
print(any(numbers))
Output
True
Because 5 is considered True.

all()
What is all()?
Returns True only if every value is True.
Think of it as "Did everyone pass?"
Example
numbers = [True, True, True]
print(all(numbers))


sorted()
What is sorted()?
Returns a new sorted list.
Original list remains unchanged.
Example
numbers = [5,2,8,1]
print(sorted(numbers))
Output
[1,2,5,8]
Descending Order
print(sorted(numbers, reverse=True))
Output
[8,5,2,1]
Sorting Strings
names = ["John","Anu","Rahul"]
print(sorted(names))
Output
['Anu', 'John', 'Rahul']

reversed()
What is reversed()?
Returns elements in reverse order.
Example
numbers = [1,2,3,4]
print(list(reversed(numbers)))
Output
[4,3,2,1]
Reverse String
name = "Python"
print("".join(reversed(name)))
Output
nohtyP

Math functions
abs()
What is abs()?
The abs() function returns the absolute (positive) value of a number.
abs(number)

round()
What is round()?
round() rounds a number to the nearest integer or to a specified number of decimal places.
print(round(4.7))
Output
5
Example 3
print(round(3.14159, 2))

pow()
What is pow()?
pow() calculates the power (exponent) of a number.
Syntax
pow(base, exponent)
Example 1
print(pow(2, 3))
Output
8

divmod()
What is divmod()?
divmod() returns both:
Quotient
Remainder
after division.
Instead of calculating them separately, Python gives both at once.
Syntax
divmod(a, b)
Example 1
print(divmod(17, 5))
Output
(3, 2)


sum()
What is sum()?
sum() adds all numbers in an iterable (such as a list or tuple).



Recursion
Recursion is a programming technique where a function calls itself to solve a problem.
Instead of using loops (for or while), the function repeats its own execution until a stopping condition is met.
Components of Recursion
Every recursive function has two important parts:
Base Case
Recursive Case
Without these, recursion will not work correctly.
The base case is the stopping condition.
It tells the function:
"Stop calling yourself."
def countdown(n):

    if n == 0:      # Base Case
        print("Done")
        return

    print(n)
    countdown(n-1)

What Happens Without a Base Case?
def hello():
    print("Hello")
    hello()

hello()

Output

Hello
Hello
Hello
Hello
Hello
...
RecursionError

Because there is no condition to stop.

Factorial: def factorial(n):

    if n == 1:             # Base Case
        return 1

    return n * factorial(n-1)   # Recursive Case


print(factorial(5))

Closures
A closure is a function that remembers the variables of its outer function even after the outer function has finished executing.
In simple words,
A closure is an inner function that "remembers" the data of the outer function.
Normal Function
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

Output

Hello

Here,

outer() creates message
inner() uses message
inner() is called before outer() ends

This is NOT a closure because the inner function is not returned.

Closure Example
def outer():

    message = "Hello Python"

    def inner():
        print(message)

    return inner


greet = outer()

greet()

Output

Hello Python
Closure with Arguments

Closures become more useful when the outer function accepts arguments.

Example

def multiplier(n):

    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)

print(double(10))

ex2): def greeting(name):

    def message():

        print("Welcome", name)

    return message


greet1 = greeting("Rahul")

greet2 = greeting("Chandana")

greet1()

greet2()
