Dictionaries and Identity Operators

Dictionaries

A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key.

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.

print("carbon" in elements)
print(elements.get("dilithium"))

This would output:

True
None

Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.
Identity Operators
Keyword 	Operator
is 	evaluates if both sides have the same identity
is not 	evaluates if both sides have different identities

You can check if a key returned None with the is operator. You can check for the opposite using is not.

n = elements.get("dilithium")
print(n is None)
print(n is not None)

This would output:

True
False

get with a Default Value

Dictionaries have a related method that's also useful, get(). get() looks up values in a dictionary, but unlike looking up values with square brackets, get() returns None (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.

>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

In the last example we specified a default value (the string 'There's no such element!') to be returned instead of None when the key is not found.

When to use Dictionaries?

Let's revisit our Wall Street example from before. Previously we created a list for the index fund, Vanguard Institutional Index Fund, because we wanted to print the names of the holdings (or stocks) in the index fund.

Now, let's say as the investment fund manager for VINIX, you also want to print a few more details for each holding. For e.g., what is your rate of return on each of the holdings?

A dictionary will work well here as there is a key: value association. In other words, there is a linkage between each holding and the information (e.g., rate of return), and it can be organized under one index fund, VINIX.

VINIX =  {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85, 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 'INTC': 1.0, 'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05, 'CVX': 1.05, 'BAC': 1.15, 'JNJ': 1.41, 'GOOGL': 1.46, 'GOOG': 1.47, 'BRK.B': 1.5, 'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02, 'AMZN': 2.96, 'MSFT': 3.28, 'AAPL': 3.94}

You can add even other details, such as rate of return YTD. For that we can add the details into the value associated with the key, i.e., the ticker symbol for the holding.
Like this:

VINIX = {'C': [0.74, -6.51],  'MA': [0.78, 34.77],  'BA': [0.79, 17.01],  'PG': [0.85, -8.81],  'CSCO': [0.88, 18.56],  'VZ': [0.9, 2.16],  'PFE': [0.92, 13.96],  'HD': [0.97, 3.2],  'INTC': [1.0, 2.61],  'T': [1.01, -15.19],  'V': [1.02, 24.0],  'UNH': [1.02, 19.32],  'WFC': [1.05, -3.59],  'CVX': [1.05, -5.77],  'BAC': [1.15, 4.27],  'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],  'JPM': [1.53, 7.66],  'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}

​
As you can see, data structures are very useful in collecting, storing and working with more information than simple strings or integers.

You will soon learn how to use dictionary methods to perform tasks, such as pull values from keys, sort values by keys, add values to the dictionary, and many other tasks that make data structures critical for data science.

 - A Tuple is an ordered data structure and can be indexed and sliced like a list;
 - A Set is a mutable data structure and does not contain duplicate elements;
 - A set is defined with curly braces, {}, but it isn't the only data structure that does; dictionaries do as well! However, the difference is that a set is defined as a sequence of elements separated by commas:

    set_example = {element1, element2, element3}
    while a dictionary is defined as a sequence of key, value pairs marked with colons, separated by commas:
    dict_example = {key1: value1, key2: value2, key3: value3}.

    → Note: if you define a variable with an empty set of curly braces like this: a = {}, Python will assign an empty dictionary to that variable. You can always use set() and dict() to define empty sets and dictionaries as well.

 - A Dictionary is mutable data structure, can be indexed using keys and the keys of a dictionary are unique.

 Identify the problem:
 
 room_numbers = {
    ['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zach']: 395
} # → TypeError: unhashable type: 'list'

    - The error you saw was TypeError: unhashable type: 'list'. In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime. This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. This is why Python requires us to use immutable datatypes for the keys in a dictionary.The lists used in the code above are NOT immutable, and thus cannot be hashed and used as dictionary keys.

