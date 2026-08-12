Module
A module is a single Python file (.py) that contains variables, functions, classes, or executable code.
Example
math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

main.py
import math_operations
print(math_operations.add(5, 3))
print(math_operations.subtract(10, 4))

You can also import specific functions:
from math_operations import add
print(add(2, 3))


Package
A package is a directory that contains multiple related modules. It helps organize large projects.
Example Directory Structure
myproject/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py
  addition.py
def add(a, b):
    return a + b
subtraction.py
def subtract(a, b):
    return a - b

main.py
from calculator.addition import add
from calculator.subtraction import subtract
print(add(10, 5))
print(subtract(10, 5))

Module	Package
A single .py file	                            A directory containing related modules
Contains functions, classes, and variables	  Contains multiple modules (and possibly subpackages)
Easier for small programs	                    Better for organizing larger projects
Imported using import module_name	             Imported using import package.module

common built in modules
a) math Module
The math module provides mathematical functions and constants.
import math
a1) math.sqrt()
Finds the square root.
import math
print(math.sqrt(25))
print(math.sqrt(49))
a2) math.pow()
Raises a number to a power.
print(math.pow(2, 3))
Output:
8.0
a3) math.factorial()
Calculates factorial.
print(math.factorial(5))
  a4) math.ceil()
Rounds a number upward.
print(math.ceil(4.2))
print(math.ceil(4.9))
  a5) math.floor()
Rounds a number downward.
print(math.floor(4.2))
print(math.floor(4.9))
  a6) math.fabs()
Returns absolute value as a float.
print(math.fabs(-10))
print(math.fabs(-5.5))
  a7) math.gcd()
Finds Greatest Common Divisor.
print(math.gcd(12, 18))
  a8) math.lcm()
Finds Least Common Multiple.
print(math.lcm(4, 6))
  a9) math.isqrt()
Returns the integer square root.
print(math.isqrt(25))
print(math.isqrt(26))
  a10) math.sin()
print(math.sin(math.pi / 2))
Output:
1.0
a11). math.cos()
print(math.cos(0))
Output:
a12). math.tan()
print(math.tan(0))
a13) math.radians()
Converts degrees → radians.
print(math.radians(180))
Output:
3.141592653589793
a14). math.degrees()
Converts radians → degrees.
print(math.degrees(math.pi))
Output:
180.0
  Constants
  math.pi
print(math.pi)
Approximately:
3.141592653589793
23. math.e
print(math.e)
24. math.tau
print(math.tau)
tau = 2π
25. math.inf
Represents infinity.
print(math.inf)
26. math.nan
Represents "Not a Number".
print(math.nan)


Random module
   import random
   Generates a random floating-point number between 0.0 and 1.0.
The range is:
0.0 <= number < 1.0
   1. import random
number = random.random()
print(number)

import random
number = random.random()
print(number)

2. random.randint()
Purpose
Generates a random integer between two values, including both values.
Remove duplicates while preserving order
import random
number = random.randint(1, 10)
print(number)

3. random.randrange()
      Generates a random number from a range.
      random.randrange(start, stop, step)
number = random.randrange(1, 10)
print(number)

      4. random.uniform()
      Generates a random floating-point number between two values.
number = random.uniform(1, 10)
print(number)

5. random.choice()
      Selects one random element from a sequence.
Usually used with:
Lists
Tuples
Strings
    students = ["Alice", "Bob", "Charlie", "David"]
student = random.choice(students)
print(student)

6. random.choices()
       Selects multiple elements randomly.
The important point is:
Duplicates are allowed.
Syntax:
random.choices(sequence, k=number)
       students = ["Alice", "Bob", "Charlie", "David"]
result = random.choices(students, k=3)
print(result)
choices() with weights
One very useful feature is giving different probabilities.
colors = ["Red", "Green", "Blue"]
result = random.choices(
    colors,
    weights=[70, 20, 10],
    k=10
)
print(result)

7. random.sample()
      Selects multiple unique elements.
Unlike choices():
Duplicates are NOT allowed.
      students = ["Alice", "Bob", "Charlie", "David"]
result = random.sample(students, k=2)
print(result)

8. random.shuffle()
Purpose
Randomly rearranges the elements of a list.
Example
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
       shuffle() modifies the original list

9. random.seed()
This one is slightly different.
Normally:

import random
       random.seed(10)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
can produce different results every time.
But sometimes we want the same random sequence every time.
That's where seed() is useful.

Datetime module
      
