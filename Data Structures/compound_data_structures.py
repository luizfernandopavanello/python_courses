"""Quiz: Adding Values to Nested Dictionaries

Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:"""

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol':'H',  'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

# Notice the last two lines are the solution necessary to add the is_noble_gas key to each of the dictionaries, so the final result would be correct after running these two lines.

"""Collections

When we have a group of data we can think about it as a collection (of data elements). In this lesson, we have seen many different data structures that Python provides for storing, accessing and manipulating collections of data. In particular, we have seen lists, sets, and dictionaries.

In the next few quizzes, you will have a chance to practice and review the properties of lists, sets, and dictionaries.

    → Attributes of a collection for which using a Python list would be appropriate:
    
        - Items are always indexed with numbers starting at 0;
        - Sortable;
        - Add items with .append  

    → Attributes of a collection for which using a Python set would be appropriate:
        - Order in which items appear can be inconsistent;
        - Mutable;
        - Add items with .add;
        → Sets are not ordered, so the order in which items appear can be inconsistent and you add items to sets with .add. Like dictionaries and lists, sets are mutable. You cannot have the same item twice and you cannot sort sets. For these two properties a list would be more appropriate.    
    
    → Attributes of a collection for which using a Python dictionary would be appropriate:
        - Each item contains two parts;
        - Order in which items appear can be inconsistent;
        - Each item in a dictionary contains two parts (a key and a value), the items in a dictionary are not ordered, and we have seen in this lesson examples of nested dictionaries. Because dictionaries are not ordered, they are not sortable. And you do not add items to a dictionary with .append.
"""

