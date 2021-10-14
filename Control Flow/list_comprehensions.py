squares = []

for x in range(9):
    squares.append(x**2)
print(squares)

squares2 = [x**2 for x in range(9)]
print(squares2)

squares3 = [x**2 for x in range(9) if x % 2 != 0]
print(squares3)

squares4 = [x**2 if x % 2 != 0 else x + 3 for x in range(9)]
print(squares4)

"""Quiz: Extract First Names

Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
"""

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]# write your list comprehension here
print(first_names)

"""Quiz: Multiples of Three

Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
"""

multiples = [x for x in range(1, 21) if x % 3 == 0]
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples)
print(multiples_3)

"""Quiz: Filter Names by Scores

Use a list comprehension to create a list of names passed that only include those that scored at least 65.
"""

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
