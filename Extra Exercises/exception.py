'''exception => events detected during execution that interrupt the normal flow of the program'''

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You must enter only number!")
except Exception:
    print("Numerator and denominator must be valid numbers!")
else:
    print(result)
