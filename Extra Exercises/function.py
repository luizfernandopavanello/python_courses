# function = a block of code which is executed only when it is called

name = input("What's your name? ")
age = str(input("What is your age? "))

def trevi(name, age):
    print(f'Hello {name}!')
    if age == "0":
        print(f'Keep Pounding {name}!')
    elif age == "1":
        print(f'Proud of you {name}. Keep going!')
    else:
        print(f'Awesome {name}!That\'s the way!')


trevi(name, age)
print('--------')

# return statement = Functions send Python values/objects back to the caller;
#                    These values/objects are known as the function's return value

def multiply(number_one, number_two):
    return number_one * number_two

multi = multiply(3, 7)

print(multi)

# keyword arguments = arguments proceded by an identifier when we pass then to a function
#                     The order of the arguments doest matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")


def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}. Welcome to the new world.")


# hello(last=last, first=first, middle=middle)

# nested functions calls = function inside other function calls;
#                          innermost functin calls are resolved first;
#                          returned values is used as argument for the next outer function


# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))