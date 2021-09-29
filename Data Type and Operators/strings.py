"""Quiz: Fix the Quote

The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.
"""
# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

""" There are two ways to do this: 

with backslash escaping: ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

with double quotes: ford_quote = "Whether you think you can, or you think you can't--you're right."""

"""We’ve already seen that the type of objects will affect how operators work on them. What will be the output of this code?
"""

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
# >>> 3415 (and tropical_fruit is a string) → That’s because even though the characters inside the strings coconut_count and mango_count are numbers, the values of the variable coconut_count and mango_count are strings, and are treated as strings when it comes to the + operator being applied.

"""Quiz: Write a Server Log Message

In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.

You’ll be provided with example data for a user, the time of their visit and the site they accessed. You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

Use the Test Run button to see your results as you work on coding this piece by piece.
"""
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')

"""Quiz: len()

Use string concatenation and the len() function to find the length of a certain movie star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!
"""

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + middle_names + family_name)
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

"""We've just used the len function to find the length of strings. What does the len function return when we give it the integer 835 instead of a string?
 → Error
 - The error message generated reads: TypeError: object of type 'int' has no len(), which alludes to the fact that len only works on a "sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)," as per the Python documentation.
""" 

print(len(835)) #TypeError: object of type 'int' has no len()