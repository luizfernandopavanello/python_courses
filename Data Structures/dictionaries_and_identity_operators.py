"""Quiz: Define a Dictionary

Define a dictionary named population that contains this data:
Keys 	    Values
Shanghai 	17.8
Istanbul 	13.3
Karachi 	13.0
Mumbai 	    12.5
"""

population = { 'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}

print(population)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True
print(a == c) # True
print(a is c) # False

# - List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. That is the difference between checking for equality vs. identity.

animals = {'dogs': [20, 10, 15, 8, 32, 15], 
 'cats': [3,4,2,8,2,4], 
 'rabbits': [2, 3, 3], 
 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

"""data type of the keys in the dictionary → string"""
"""data type of the values in the dictionary → list"""
print(animals['dogs']) # [20, 10, 15, 8, 32, 15]
print(animals['dogs'][3]) # 8
print(animals['fish']) # [0.3, 0.5, 0.8, 0.3, 1]
print(animals[3]) # Error