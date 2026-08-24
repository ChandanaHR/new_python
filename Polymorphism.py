1a)) The word polymorphism means:
“One interface, many forms.”
In Python, polymorphism allows the same method/function/operator to behave differently depending on the object or data involved

Think about a payment system.
You have:
Google Pay
PhonePe
Credit Card
UPI
All of them have a common operation:
pay()
But each payment method performs it differently.
pay()
  ↓
GooglePay  → Pay using Google Pay
PhonePe     → Pay using PhonePe
CreditCard  → Pay using Credit Card
The caller doesn't need to know the internal implementation.
That's polymorphism.

1b) Polymorphism in Python
Python supports polymorphism in several ways:
1b1) Duck typing
“If it behaves like a duck, treat it like a duck.”
Python usually cares about what an object can do, rather than what class it belongs to.
  class Dog:
    def speak(self):
        print("Dog says Woof")
class Cat:
    def speak(self):
        print("Cat says Meow")
def make_sound(animal):
    animal.speak()
dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)
The function doesn't care whether animal is a Dog or Cat.
It only cares:
Does this object have a speak() method?
That's duck typing.

1b2) Method Overriding
Method overriding happens when a child class provides its own implementation of a method inherited from the parent class.
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
The same method:
sound()
has different implementations.
That's polymorphism.

1b3) Polymorphism Through Inheritance
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
animals = [
    Dog(),
    Cat(),
    Animal()
]
for animal in animals:
    animal.sound()
    We don't write:
We donnt write
if isinstance(animal, Dog):
    ...
elif isinstance(animal, Cat):
    ...
Instead, Python automatically calls the appropriate implementation.
This is runtime polymorphism.

1b4) Runtime polymorphism
class Payment:
    def pay(self, amount):
        print(f"Processing payment of ₹{amount}")
class GooglePay(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Google Pay")
class PhonePe(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PhonePe")
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
def checkout(payment_method, amount):
    payment_method.pay(amount)
checkout(GooglePay(), 500)
checkout(PhonePe(), 1000)
checkout(CreditCard(), 2000)
.........Why Polymorphism Is Useful
Suppose you initially support:
GooglePay
PhonePe
Later you add:
PayPal
CreditCard
Stripe
AmazonPay
Without polymorphism, you might write:

if payment == "googlepay":
    ...
elif payment == "phonepe":
    ...
elif payment == "paypal":
    ...
elif payment == "creditcard":
    ...
This becomes difficult to maintain.
With polymorphism:
payment.pay()
Every payment class handles its own implementation.

1b5) Operator Overloading
Python allows you to define how operators work for your own classes.
class Student:

    def __init__(self, marks):
        self.marks = marks

    # +
    def __add__(self, other):
        return self.marks + other.marks

    # -
    def __sub__(self, other):
        return self.marks - other.marks

    # *
    def __mul__(self, other):
        return self.marks * other.marks

    # /
    def __truediv__(self, other):
        return self.marks / other.marks

    # //
    def __floordiv__(self, other):
        return self.marks // other.marks

    # %
    def __mod__(self, other):
        return self.marks % other.marks

    # ==
    def __eq__(self, other):
        return self.marks == other.marks

    # !=
    def __ne__(self, other):
        return self.marks != other.marks

    # <
    def __lt__(self, other):
        return self.marks < other.marks

    # >
    def __gt__(self, other):
        return self.marks > other.marks

    # <=
    def __le__(self, other):
        return self.marks <= other.marks

    # >=
    def __ge__(self, other):
        return self.marks >= other.marks


student1 = Student(80)
student2 = Student(40)


print("Addition:", student1 + student2)
print("Subtraction:", student1 - student2)
print("Multiplication:", student1 * student2)
print("Division:", student1 / student2)
print("Floor Division:", student1 // student2)
print("Modulus:", student1 % student2)

print("Equal:", student1 == student2)
print("Not Equal:", student1 != student2)

print("Less Than:", student1 < student2)
print("Greater Than:", student1 > student2)

print("Less Than or Equal:", student1 <= student2)
print("Greater Than or Equal:", student1 >= student2)
Internally: student1.__add__(student2)

1b6) Method overloading in python how to achieve it
Method overloading means having multiple methods with the same name but different parameters.
For example, in Java:
add(int a, int b)
add(int a, int b, int c)
add(double a, double b)
The compiler chooses the appropriate method based on the arguments.
How to Achieve Method-Overloading-Like Behavior in Python
a) Using Default Arguments
This is the simplest approach.
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
calculator = Calculator()
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))

b) Using *args
If you don't know how many arguments you'll receive, use *args.
class Calculator:
    def add(self, *numbers):
        return sum(numbers)
calculator = Calculator()
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))
print(calculator.add(10, 20, 30, 40))

c) Using **kwargs
You can also achieve flexible behavior using keyword arguments.
class Student:
    def display(self, **details):
        for key, value in details.items():
            print(key, ":", value)
student = Student()
student.display(
    name="Chandana",
    age=26
)

d) Method Overloading Based on Data Type
Sometimes you want different behavior depending on the type.
For example:

class Calculator:

    def process(self, value):

        if isinstance(value, int):
            return value * 2

        elif isinstance(value, str):
            return value.upper()

        elif isinstance(value, list):
            return len(value)

        else:
            return "Unsupported type"


calculator = Calculator()

print(calculator.process(10))
print(calculator.process("python"))
print(calculator.process([10, 20, 30]))

e) functools.singledispatch
Python also provides a more formal way to dispatch based on the type of the first argument.
from functools import singledispatch
@singledispatch
def process(value):
    print("Unknown type")
@process.register
def _(value: int):
    print("Processing integer:", value)
@process.register
def _(value: str):
    print("Processing string:", value)
@process.register
def _(value: list):
    print("Processing list:", value)
process(10)
process("Python")
process([1, 2, 3])
