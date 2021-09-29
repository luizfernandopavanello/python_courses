Integers and Floats

There are two Python data types that could be used for numeric values:

    int - for integer values
    float - for decimal or floating point values

You can create a value that follows the data type by using the following syntax:

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0

You can check the type by using the type function:

>>> print(type(x))
int
>>> print(type(y))
float

Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them together we can see the difference between the mathematically correct answer and the one that Python creates.

>>> print(.1 + .1 + .1 == .3)
False

Python Best Practices

For all the best practices, see the PEP8 Guidelines.

You can use the atom package linter-python-pep8 to use pep8 within your own programming environment in the Atom text editor, but more on this later. If you aren't familiar with text editors yet, and you are performing all of your programming in the classroom, no need to worry about this right now.

Follow these guidelines to make other programmers and future you happy!
Good

print(4 + 5)

Bad

print(                       4 + 5)

You should limit each line of code to 80 characters, though 99 is okay for certain use cases. You can thank IBM for this ruling.

Why are these conventions important? Although how you format the code doesn’t affect how it runs, following standard style guidelines makes code easier to read and consistent among different developers on a team.
