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

