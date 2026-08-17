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
