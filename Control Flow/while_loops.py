"""
Practice: Factorials with While Loops
Find the factorial of a number using a while loop.

A factorial of a whole number is that number multiplied by every whole number between itself and 1. For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

We can write a while loop to take any given number and figure out what its factorial is. If number is 6, your code should compute and print the product, 720.
"""
# number to find the factorial of
number = 6
#start with our product equal to one
product = 1
#track the current number being multiplied
current = 1

while current <= number:
    #multiply the product so far by the current number
    product *= current
    #increment current with each iteration until it reaches number
    current += 1
    
print(product)
    
"""Practice: Factorials with For Loops

Now use a for loop to find the factorial!"""

#number to find the factorial of
number = 6
#start with our product equal to one
product = 1

for num in range(2, number + 1):
    # print(num)
    product *= num
    
print(product)

"""Quiz: Count By

Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num.
"""

start_num = 5
end_num = 100
count_by = 3

break_num = 1
while break_num < end_num:
    break_num += count_by
print(break_num)

"""Quiz: Nearest Square

Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.
"""

limit = 40
num = 1

while (num + 1)**2 < limit:
    num += 1
nearest_square = num ** 2

print(nearest_square)

"""Question: What type of loop should we use?

You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

Would you use a while or a for loop to write this code?

→ We would write a while loop to write this code for the following reasons:

    - We don't need a break statement that a for loop will require. Without a break statement, a for loop will iterate through the whole list, which is not efficient.
    - We don't want to iterate over the entire list, but only over the required number of elements in the list that meets our condition.
    - It is easier to understand because you explicitly control the exit conditions for the loop.
    
- Consider this: If the question was to identify if each number in the list is an odd or even number, then a for loop makes better sense. In that case, you need to loop through each element in the list. However, in the question above, as long as you have the sum of the first five odd numbers (the condition), you can stop going through the list and don't need to go through the rest of the elements.

"""

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

