"""
Scope = The region that a variable is recognized;
        A variable is only available from inside the region it is created;
        A global and locally scoped versions of a variable can be created
"""

name = "Trevi" # global scope (available inside & outside functions)
print(f"Global Scope: {name}")

def display_name():
    name = "Python" # local scope (available only inside this function)
    print(f"Local Scope: {name}")


display_name()
print(f"Global Scope: {name}")

"""
→ LEGB rule: L=local; E=Enclosing; G=Global; B=Built-in
The order how functions use the variables...
"""

