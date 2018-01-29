Python Syntax
===

Python syntax is thankfully very easy to understand while at the same time unfortunately obscure about types.

If you're coming from Java or other more 'explicit' programming langues where types have to be 'cast' before a variable can be used then this will look familiar.

C#:
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntroductionApp1
{
    class Program
    {
        static void introduction(string yourName, string yourHeight)
        {
            Console.WriteLine("Hello everyone my name is " + yourName);
            Console.WriteLine("Did you know " + yourName + " is " + yourHeight + " cm tall?");

            // Use this to keep the command prompt/terminal open
            Console.ReadLine();
        }

        static string getUserInput(string message) // Note that python's "input" does basically this:
        {
            Console.WriteLine(message);
            string userInput = Console.ReadLine();

            return userInput;
        }

        static void Main(string[] args)
        {
            // Get user name
            string userName = getUserInput("Enter your name:");

            // Get user hiehgt in cm
            string userHeight = getUserInput("Enter your height in cm:");

            // Pass data to 'introduction' method
            introduction(userName, userHeight);

        }
    }
}

```

Compare this code from C# to Python.  Both pieces of code do ***exactly*** the same thing (take a name and height from the console and print it out back to you) but C# requires far more explicit code than python.

Python:
```
def introduction (your_name, your_height):

    print("Hello everyone my name is", your_name)
    print("Did you know " +  your_name + " is " + your_height + " cm tall?")

# Get user name
user_name = input("Enter your name: ")

# Get user height in cm
user_height = input("Enter your height in cm: ")

# Pass data to 'introduction' method
introduction(user_name, user_height)
```

Or even more simply in python (not using a function):
```
# Get user name 
user_name = input("Enter your name: ")

# Get user height in cm
user_height = input("Enter your height in cm: ")

print("Hello everyone my name is", user_name)
print("Did you know " +  user_name + " is " + user_height + " cm tall?")
```

Also notice the differences in syntax.  In C# and Java a ';' signifies the end of a statement while in python no such marker is needed.  Instead python uses white spaces and indentation.  Curly braces and brackets are also restricted in python to define **Lists**, **Dictionaries** and **Arrays**.  While in C# and Java curly braces are used to seperate code blocks.

Additionally naming ***classes***, ***methods***, and ***variables*** is language dependent.  Those of you who are use to camel case (camelCaseLooksLikeThis) will be saddened to know that this is not used to name methods and variables and is technically not part of the 'best practicies' of python programming.  Instead python perfers underscores (variables_should_look_like_this).

For more details on the best practices of programming in python please visit:

https://www.python.org/dev/peps/pep-0008/

Note:  PEP8 is (for whatever reason) a controversial topic in python circles.  People get upset when you nit pick their code and how they name things.

Object Oriented Programming (OOP)
===

## Class:

An extensible program-code-template for creating objects and providing **methods** and initial values for state.

```
class MyClassName:

    def method_1(self, parameter_1):

        \\do work

    return work
```

## Method:

Like a function but specifically associated with an object.  Methods are "object functions".

```
def method _1(self, parameter_1):

    \\do work

return work
```

## Function:

Code that is passed data (parameters) and is worked on.

```
def function_1(parameter_1):
    
    \\do work

reutrn work
```

## Method vs. Function

A **function** is code that can be called by name and is passed data to operate on via parameters.

A **method** is code that called by name and is associated with an object (i.e. an instance of a class).

