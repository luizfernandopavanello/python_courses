"""Quiz: List Indexing

Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

Remember to account for zero-based indexing!
"""
month = 8
days_in_month = [31, 28, 31,30,31,30,31,31,30,31,30,31]

num_days = days_in_month[month - 1]
print(num_days)

"""Quiz: Slicing Lists

Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
"""
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])

#This slice uses a negative index to begin slicing three elements from the end of the list. The end index can be omitted because this slice continues until the end of the list.

"""Suppose we have the following two expressions, sentence1 and sentence2:

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

Match the Python code below with the value of the modified sentence1 or sentence2. If the code results in an error, match it with “Error”.

- sentence2[6] = "!" → ["I", "wish", "to", "register", "a", "complaint", "!"]
- sentence2[0] = "Our Majesty" → ["Our Majesty", "wish", "to", "register", "a", "complaint", "."]
- sentence1[30] = "!" → Error() TypeError: 'str' object does not support item assignment
- sentence2[0:2] = ["We", "want"] → ["We", "want", "to", "register", "a", "complaint", "."]

→ sentence1 is a string, and is therefore an immutable object. That means that while you can refer to individual characters in sentence1 (e.g., you can write things like sentence1[5]) you cannot assign value to them (you cannot write things like sentence1[5] = 'a'). Therefore the third expression will result in an error.

→ sentence2 is a list, and lists are mutable, meaning that you can change the value of individual items in sentence2:

    - In the first expression we changed the value of the last item in sentence2 from "." to "!".
    - In the second expression we changed the value of the first item in sentence2 from "I" to "Our Majesty".
    - In the last expression we used slicing to simultaneously change the value of both the first and the second item in sentence2 from "I" and "wish" to "We" and "want".

"""
"""
Check for Understanding

Data types and data structures are tricky but important concepts to master! Let's pause and make sure you understand the distinction between them.

→ Data Structures arre containers tha can include different data types

→ A list is an example od a data structure

→ All data structure are data types

→ A data type is just a type that classifies data. This can include primitive (basic) data types like integers, booleans, and strings, as well as data structures, such as lists.

→ Data structures are containers that organize and group data types together in different ways. For example, some of the elements that a list can contain are integers, strings, and even other lists!

→ Properties os Lists: 
    - Mutable
    - Ordered data structures

"""