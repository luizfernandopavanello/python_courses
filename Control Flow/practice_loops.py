"""Coding Quiz: Check for Prime Numbers

Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.
1 X 6 = 6
2 X 3 = 6
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

    If the numbers are prime, the code should print "[number] is a prime number."
    If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".

Example output:

7 IS a prime number
26 is NOT a prime number, because 2 is a factor of 26
"""

check_prime = [26, 37, 39, 51, 53, 57, 73, 79, 85]

# iterate through the check_prime list
for num in check_prime:
# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):
# number is not prime if module is 0
        if (num % i) == 0:
            print('{} is not a prime number, because {} is a factor of {}'.format(num, i, num))
            break
# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:
            print('{} is a prime number'.format(num))
        
""" Logic for our solution:

    We loop through each number in the check_prime list.
    Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
    Use a conditional statement with the modulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
    If we ever find one factor, we can declare that the number is not prime, and state the factor we found. Then we can break out of the loop for that number.
    If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime.
"""