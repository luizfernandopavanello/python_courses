# → map() = applies a function to each item in an iterable (list, tuple, etc.)
#
#  map(function, iterable)

store = [('shirt', 20.00),
         ('pants', 25.00),
         ('jacket', 50.00),
         ('socks', 10.00)]

to_euros = lambda data: (data[0], data[1]*0.89)
to_pounds = lambda data: (data[0], data[1]*0.74)

store_euros = list(map(to_euros, store))
print("Dolar to Euro")
for e in store_euros:
    print(e)

print("----------")

store_pounds = list(map(to_pounds, store))
print("Dolar to Pounds")
for p in store_pounds:
    print(p)