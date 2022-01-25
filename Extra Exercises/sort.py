"""
→ sort() method = used with lists
→ sort() function = used with iterables
"""

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

# students.sort()
# sorted_students = sorted(students)
#
# for i in sorted_students:
#     print(i)

# sort the list of tuples

age = lambda ages:ages[2]

students.sort(key=age, reverse=True)

for i in students:
    print(i)

students_tuple = (("Squidward", "F", 60),
                ("Sandy", "A", 33),
                ("Patrick", "D", 36),
                ("Spongebob", "B", 20),
                ("Mr. Krabs", "C", 78))

name = lambda names:names[0]
sorted_students_tuple = sorted(students_tuple, key=name)
print("---------------------")
print("Students Tuple:")

for i in sorted_students_tuple:
    print(i)



