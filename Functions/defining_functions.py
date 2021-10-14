"""Print vs. Return in Functions

Here are two valid functions. One returns a value and one simply prints a value, without returning anything. Test run this code and experiment to understand the difference.
"""

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))


"""Quiz: Population Density Function

Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. I've included two test cases that you can use to verify that your function works correctly. Once you've written your function, use the Test Run button to test your code."""

# write your function here
def population_density(population, land_area):
    density = population / land_area
    return(density) 



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))