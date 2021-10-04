For Loops Vs. While Loops

Now that you are familiar with both for and while loops, let's consider when it's most helpful to use each of them.

for loops are ideal when the number of iterations is known or finite.

Examples:

    When you have an iterable collection (list, string, set, tuple, dictionary)
        for name in names:
    When you want to iterate through a loop for a definite number of times, using range()
        for i in range(5):

while loops are ideal when the iterations need to continue until a condition is met.

Examples:

    When you want to use comparison operators
        while count <= 100:
    When you want to loop based on receiving specific user input.
        while user_input == 'y':
