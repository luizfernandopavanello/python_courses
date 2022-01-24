# lists = - used to store multiple items in a single variable
#         - we can update and change the elements after declare

# food = ["rice", "beans", "egg", "tomato", "lettuce"]
#
# print(f"First food on our list is {food[0]}, it has the indes equals 0.")
# print(f"Second food on our list is {food[1]}.")
# print(f"Thirty food on our list is {food[2]}.")
# print(f"Fourth food on our list is {food[3]}.")
# print(f"Fifth food on our list is {food[4]}.")
#
# food[4] = "zucchini"
# food.append("ice cream")
# food.remove("rice")
# food.remove("beans")
# food.append('sushi')
# food.pop()
# food.insert(0, 'pasta')
# food.sort()
#
# for f in food:
#     print(f)

# 2D lists = a list os lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburguer", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food) # all together

for list in food:
    print(list) # eache list in a new line

# print one element inside your list in the foods list using the index for a list and food
print(food[0][0]) # drinks list
print(food[1][2]) # dinner list
print(food[2][1]) # dessert list

