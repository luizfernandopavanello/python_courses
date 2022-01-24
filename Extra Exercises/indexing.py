# index operator [] = gives acces to a sequences element (str, list, tuples)

name = "trevi IT"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper() # start at 0 and go on
last_name = name[6:].lower() # start at the number and go to the last one
last_character = name[-1] # the negative sign gives the power to start at the end

print(name)
print(first_name)
print(last_name)
print(last_character)

