#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

"""
Practice: Which Prize

Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.
Points 	Prize
1 - 50 	wooden rabbit
51 - 150 	no prize
151 - 180 	wafer-thin mint
181 - 200 	penguin

All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Oh dear, no prize this time."

Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. You can hide your other inputs by commenting them out.
"""

points = 174

if points <= 50:
    result = 'Congratulations! You won a wooden rabbit!'
elif points <= 150:
    result = 'Oh dear, no prize this time.'
elif points <= 180:
    result = 'Congratulations! You won a wafer-thin mint!'
else:
    result = 'Congratulations! You won a penguin!'
    
print(result)

"""We use <= instead of the < operator, since it was stated that the upper bound is inclusive. Notice that in each condition, we check if points is in a prize bracket by checking if points is less than or equal to the upper bound; we didn't have to check if it was greater than the lower bound. Let's see why this is the case.

    When points = 174, it first checks if points <= 50, which evaluates to False. We don't have to check if it is also greater than 0, since it is stated in the problem that points will always be a positive integer up to 200.

    Since the first condition evaluates to False, it moves on to check the next condition, points <= 150. We don't need to check if it is also greater than 50 here! We already know this is the case because the first condition has to have evaluated to False in order to get to this point. If we know points <= 50 is False, then points > 50 must be True!

    Finally, we check if points <= 180, which evaluates to True. We now know that points is in the 151 - 180 bracket.

    The last prize bracket, 181-200, is caught in the else clause, since there is no other possible value of the prize after checking the previous conditions.
"""

"""Quiz: Guess My Number

You decide you want to play a game where you are hiding a number from someone. Store this number in a variable called 'answer'. Another user provides a number called 'guess'. By comparing guess to answer, you inform the user if their guess is too high or too low.

Fill in the conditionals below to inform the user about how their guess compares to the answer.
"""
answer = 35
guess = 30 # just a sample answer and guess

if guess < answer:
    result = 'Oops! Your guess was too low.'
elif guess > answer:
    result = 'Oops! Your guess was too high.'
elif guess == answer:
    result = 'Nice! Your guess matched the answer!'
print(result)

"""Quiz: Tax Purchase

Depending on where an individual is from we need to tax them appropriately. The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.
"""

state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)