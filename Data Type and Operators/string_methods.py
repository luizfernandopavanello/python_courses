"""Question 1 of 3

What happens when you call a string method like islower() on a float object? For example, 13.37.islower().

→ An error occurs. The islower() method is an attribute of string methods, but not floats. Different types of object have methods specific to their type. For example, floats have the is_integer() method which strings don't have.
"""
# print(13.37.islower()) #AttributeError: 'float' object has no attribute 'islower'

"""Quiz: String Methods Coding Practice

Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling. Remember, \n is a special sequence of characters that causes a line break (a new line).

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

    What is the length of the string variable verse?
    What is the index of the first occurrence of the word 'and' in verse?
    What is the index of the last occurrence of the word 'you' in verse?
    What is the count of occurrences of the word 'you' in the verse?

"""

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))

"""
What is the length of the string variable verse? 362

What is the index of the first occurrence of the word 'and' in verse? 65

What is the index of the last occurrence of the word 'you' in verse? 186

What is the count of occurrences of the word 'you' in the verse? 8
"""
