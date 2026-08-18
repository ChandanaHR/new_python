import sys
What is the sys module?

sys stands for system.

It provides functions and variables that interact with:
Python interpreter
Command-line arguments
Python path
Standard input/output/error
Program termination
Recursion limit
Module information
Python version
Runtime configuration

  a) sys.version
Returns detailed information about the Python version.
import sys
print(sys.version)
  hich Python version is currently running this program?

  b) sys.version_info
Provides Python version information in a structured form.
import sys
print(sys.version_info)
Example:
sys.version_info(major=3, minor=13, micro=5, ...)
You can access individual values:
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.version_info.micro)

  c) sys.platform
Returns information about the operating system/platform.
import sys
print(sys.platform)
          import sys
if sys.platform == "win32":
    print("Windows")
elif sys.platform == "linux":
    print("Linux")
elif sys.platform == "darwin":
    print("macOS")

  d) sys.executable
Returns the path of the Python interpreter currently running your program.
import sys
print(sys.executable)
          This is particularly useful when you have multiple Python installations.

e) sys.argv
This is one of the most important sys features.
sys.argv stores command-line arguments.
Suppose you create:
hello.py
with:
import sys
print(sys.argv)
Run:
python hello.py Chandana 26
Command-line calculator
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
Everything inside sys.argv is a string.

f) sys.path
sys.path contains the directories Python searches when importing modules.
import sys
print(sys.path)
Adding your own directory
You can add a directory:
import sys
sys.path.append("/my/project")
import mymodule
Now Python can search that directory for modules.
sys.path is a list.
print(type(sys.path))
Output:
<class 'list'>
Therefore list methods can be used:
sys.path.append(...)
sys.path.insert(...)
sys.path.remove(...)

g) sys.stdin
sys.stdin represents standard input.
Normally, this is your keyboard.
Instead of:
name = input("Enter name: ")
you can use:
import sys
name = sys.stdin.readline()
print("Hello", name)
sys.stdin.readline()

Reads one line from standard input.
import sys
name = sys.stdin.readline()
print("Name:", name)
If you don't want the newline:
name = sys.stdin.readline().strip()

h) sys.stdout
sys.stdout represents standard output.
Normally:
print("Hello")
prints to sys.stdout.
You can directly write:
import sys
sys.stdout.write("Hello")
Output:
Hello
Difference
print("Hello")
automatically adds a newline.
But:
sys.stdout.write("Hello")
doesn't.
Example:
import sys
sys.stdout.write("Hello")
sys.stdout.write("World")
Output:
HelloWorld
You can add the newline yourself:
sys.stdout.write("Hello\n")


i) sys.exit(): Terminates the python program
import sys
print("Program started")
sys.exit()
print("This will not execute")
You can provide an exit status:
sys.exit(0)  # Successful
sys.exit(1)  # Error

j) sys.modules
Contains all modules currently loaded by Python.
import sys
print(sys.modules)
You can check whether a module has already been imported:
import sys
if "math" in sys.modules:
    print("math is already loaded")
else:
    print("math is not loaded")

k) sys.stderr
Represents standard error output.
import sys
sys.stderr.write("Something went wrong\n")
Usually:
stdout → normal output
stderr → error/warning output
Example:
import sys
print("Normal message")
sys.stderr.write("Error message\n")

l) sys.getsizeof()
Returns the memory size of an object in bytes.
import sys
x = 100
print(sys.getsizeof(x))
Example output:
28
Another example:
import sys
numbers = [1, 2, 3, 4, 5]
print(sys.getsizeof(numbers))
getsizeof() gives the size of the object itself, not necessarily the total memory consumed by objects referenced inside it.

m) sys.getrecursionlimit()
Returns the maximum recursion depth Python allows.
import sys
print(sys.getrecursionlimit())
Typical output:
1000

n) sys.setrecursionlimit()
Changes the recursion limit.
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
Output:
2000
Warning
Don't increase this unnecessarily. A very high recursion limit can cause a stack overflow or crash.

o) sys.getdefaultencoding()
Returns Python's default text encoding.
import sys
print(sys.getdefaultencoding())

  p) sys.getfilesystemencoding()
Returns the encoding used by Python for filesystem operations.
import sys
print(sys.getfilesystemencoding())

q) sys.getswitchinterval()
Returns the interpreter's thread switching interval.
import sys
print(sys.getswitchinterval())
Example:
0.005
This is related to how often the Python interpreter checks for thread switching.

r) sys.setswitchinterval()
Changes the thread switching interval.
import sys
sys.setswitchinterval(0.01)
print(sys.getswitchinterval())

s) sys._getframe()
Returns the current execution frame.
import sys
frame = sys._getframe()
print(frame)
You can inspect information about the current function:
import sys
def test():
    frame = sys._getframe()
    print(frame.f_code.co_name)
test()

t) sys.maxsize
Returns the largest value a Python int-related platform size commonly uses.
import sys
print(sys.maxsize)
On a typical 64-bit system:
9223372036854775807

u) sys.hash_info
Provides information about Python's hash implementation.
import sys
print(sys.hash_info)
You can inspect individual values:
print(sys.hash_info.width)
print(sys.hash_info.modulus)
Useful for advanced work involving Python hashing.

v) sys.implementation
Provides information about the Python implementation.
import sys
print(sys.implementation)
Example:
print(sys.implementation.name)
Output:
cpython
Other Python implementations include things such as PyPy.
