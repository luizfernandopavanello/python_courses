""" Imagine an air traffic control program that tracks three variables, altitude, speed, and propulsion which for a particular airplane have the values specified below.

altitude = 10000
speed = 250
propulsion = "Propeller"

For each of the following boolean expressions, work out whether it evaluates to True or False and match the correct value.

- altitude < 1000 and speed > 100  >>> False
- (propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000 >>> False
- not (speed > 400 and propulsion == "Propeller")   >>> True
- altitude > 500 and speed > 100) or not propulsion == "Propeller"  >>> True
"""

"""Using Truth Values of Objects

The code below is the solution to the Which Prize quiz you've seen previously. You're going to rewrite this based on what you've learned about truth values.

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.

1st conditional statement: update prize to the correct prize name based on points.
2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.

    If prize is None, result should be set to "Oh dear, no prize this time."
    If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.

At the beginning of your code, set prize to None, as the default value."""

points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit!"
elif 151 <=points <= 180:
    prize = "wafer-thin mint!"
elif points > 181:
    prize = "penguin!"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = 'Congratulations! You won a {}!'.format(prize)
else:
    result = 'Oh dear, no prize this time.'

print(result)

# We first set prize to None and then update it only if falls into a bracket that results in winning a prize. This is accomplished in the first if statement. We then use the truth value of prize to assign result to a message based on whether a prize was won. Remember when prize = "penguin", or any other non-empty string, then the if prize condition is True!