# filter() = creates a collection of elements from an iterable for which a function returns true
#  filter(function, itereable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for f in drinking_buddies:
    print(f[0])

