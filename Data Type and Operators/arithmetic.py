"""Quiz: Average Electricity Bill

It's time to try a calculation in Python!

My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result.
"""

bill_1 = 23
bill_2 = 32
bill_3 = 64

bill_avg = (bill_1 + bill_2 + bill_3) / 3
print('The average monthly electricity bill are $', format(bill_avg, ".2f"))

"""Quiz: Calculate

In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

    How many tiles are needed?
    You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
"""

tiles1 = 9 * 7
tiles2 = 5 * 7
tiles_needed = tiles1 + tiles2
print('How many tiles are needed:', tiles_needed)

tiles_bought = 17 * 6
print('How many tiles will be left over:', (tiles_bought - tiles_needed))

"""Question 3 of 3

Which of these lines of Python code are well formatted? How would you improve the readability of the codes that don't use good formatting? (Choose all that apply)
"""

#  - print(((3 + 32)) + -15//2)
#  - print((17 - 6) % (5 + 2)) X
#  - print ((1 + 2 + 4) / 13)
#  - print(4/2 - 7*7) X

"""Practicing good formatting when coding is the best way to get good at it. Here is what we thought:

- The first one isn't well formatted; it has some extra spaces, extra parentheses and an extra +. It would look much clearer as print((3 + 32) - 15//2)
- The second one looks good, it's got extra spaces around the - and + to help with readability.
- The third one looks quite clear, though it could be a bit better by removing the space between print and ( and the spaces around the / )
- The final one looks fine 
"""