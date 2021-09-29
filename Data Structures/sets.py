numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums) # {1, 2, 3, 6}

"""What would the output of the following code be?"""

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b)) # 6 List a has 10 elements, while the set b (created from the list a) has 4 elements because the are 4 unique elements in a.

"""will the number 5 be a part of the set b?"""

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b) # Maybe - When you pop an element from a set a random element is removed (remember that sets, unlike lists, are unordered so there is no "last element"). The number 5 may or may not be removed.
