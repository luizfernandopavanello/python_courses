"""Quiz Question

Read through this code snippet:"""

# egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()

"""What is the result of running this code? If you aren't sure, try running it on your own computer!

This causes an UnboundLocalError, since Python doesn't allow functions to modify variables that are outside the function's scope. A better way would be to pass the variable as an argument and reassign it outside the function.
The variable egg_count in the first line has global scope. Note that it is not passed as an argument into the function, so the function assumes the egg_count being referred to is the global variable.

we can print a global variable's value successfully without an error. This worked because we were simply accessing the value of the variable. If we try to change or reassign this global variable, however, as we do in this code, we get an error. Python doesn't allow functions to modify variables that aren't in the function's scope.

A better way to write this would be:
"""

egg_count = 0

def buy_eggs(count):
    return count + 12 # purchase a dozen eggs

egg_count = buy_eggs(egg_count)