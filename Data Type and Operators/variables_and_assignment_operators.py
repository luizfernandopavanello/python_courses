"""Quiz: Assign and Modify Variables

Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.

Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.
"""
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5 

# print the new value of the reservoir_volume variable
# print(reservoir_volume)

"""Quiz: Changing Variable Values

How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.

We're intentionally not providing a place to execute the code here, because we want to help you practice the important skill of walking through lines of code by hand.

Each line of code executes in order, one at a time, with control going from one line to the next. 

>>> carrots = 24
>>> rabbits = 8
>>> crs_per_rab = carrots/rabbits

Now we add a new 4th line to this code, that assigns a new value to the rabbits variable:

>>> rabbits = 12

If we now add this new 5th line of code to the above, what will the output be?

>>> print(crs_per_rab)  → 3  

→→→ Solution: Changing Variables

For the first multiple choice quiz, the correct answer is that the value of crs_per_rab has not changed. That is, it is still 3.0.

This is because when a variable is assigned, it is assigned to the value of the expression on the right-hand-side, not to the expression itself. In the line:

>>> crs_per_rab = carrots/rabbits    

Python actually did the calculation to evaluate the expression on the right-hand-side, carrots/rabbits, and then assigned the variable crs_per_rab to be the value of that expression. It promptly forgot the formula, only saving the result in the variable.

In order to update the value of crs_per_rab to take into account the change in rabbits, we need to run this line again:

>>> crs_per_rab = carrots/rabbits
>>> print(crs_per_rab)    
2.0

That’s the new number of carrots per rabbit after the increase in the number of rabbits. All of our variables have been updated to take this into account.


"""

"""Here is a list of U.S. states in order of the date they entered the Union. Say you wanted to create a variable for Delaware and assign it a value to signify that it joined the Union first. Which of the following are valid variable names and assignments in Python?

delaware = 1
de = 1
"""
