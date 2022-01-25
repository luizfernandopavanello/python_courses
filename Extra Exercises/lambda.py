"""
→ lambda function = function in 1 line using lambda keyword;
                    accepts any number of arguments, but only has one expression;
                    (think of it as s shortcut);
                    (useful if needed for a short period of time, throw-away)
"""
# lambda parameters: expression

def double(x):
    return x * 2

print("Double function:",double(5))

double = lambda x: x * 2
print("Double Lambda function:",double(5))

multiply = lambda x, y: x * y
print("Multiply Lambda function:",multiply(3, 7))

add = lambda x, y, z: x + y + z
print("Add Lambda function:",add(3, 5, 7))

full_name = lambda first_name, last_name: first_name +" "+last_name
print("Fullname Lambda function:",full_name("Trevi", "IT"))

age_check = lambda age: True if age >= 18 else False
print("Age Checker Lambda function:",age_check(18))
