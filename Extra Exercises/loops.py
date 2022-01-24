# → Loops

# while loop = a statement that will execute its block of code, as long as it's condition remains true

# while 1==1:
#     print("Help! I'm stuck in a loop.")

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello "+name)

# while not name:
#     name = input("Enter your name: ")
#
# print("Hi "+name+ "!")

# for loops = A statement that will execute it is block of code a limited amount of times
#   while loop = unlimited
#   for loops = limited

# for i in range(10):
#     print(i+1)

# for i in range(50,101):
#     print(i)

# for i in 'TreviIT':
#     print(i)

# import time
#
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Your time is Over!")

# nested loops = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# Loop Control Statements = change a loops executions from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
