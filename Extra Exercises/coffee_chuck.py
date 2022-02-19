# Let's start a coffe shop together. We're going to build a coffee shop using some new 
# Python programming concepts

# Let's build a robot Barista.

print('Hello, welcome to Nitnesiv Coffee Shop!')

name = input("What is your name?\n")

if name == 'Dev':
	print("You're not welcome here Dev!! Get out...")
	exit()
else:
	print(f'Hello {name}, thank you so much for coming in today.\n\n')

# Coffee Menu
menu = "Black Coffee, Espresso, Latte, Cappucino"

# Ask the customer what they would like from the menu 
# and store it in the variable order.
order = input(f"So, {name}, what would like from our menu today? Here is what we are serving: {menu}.\n\n")


# Ask the customer how many coffees they would like and store it in the variable quantity

quantity = input(f'How many {order} would you like?\n')

# Set the price for coffee
if order == 'Black Coffee':
	price = 5
elif order == 'Espresso':
	price = 3
elif order == 'Latte':
	price = 6
elif order == 'Cappucino':
	price = 8
else:
	price = 0
	print("Sorry, we don't have that here. Get out...")
	exit()

# Calculate the customer's total
total = price * int(quantity)

# Give the customer their total
print(f'Thank you. Your total is: ${str(total)}')


