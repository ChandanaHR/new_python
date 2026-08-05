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
