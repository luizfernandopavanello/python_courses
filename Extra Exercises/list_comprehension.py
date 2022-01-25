# → list comprehension = a way to create a new list with less syntax;
#                        can mimic certain lambda functions, easier to read;
#                        list = [expression for item in iterable]
#                        list = [expression for item in iterable if conditional]
#                        list = [expression if/else for item in iterable]

squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

squares_2 = [i * i for i in range(1, 11)] # list cromprehension
print(squares_2)
print("-----------------")

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)
passed_students = [i for i in students if i >= 60] # list comprehension
print(passed_students)
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)