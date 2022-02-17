dogNames = []

while True:
    print('Enter the name of dog ' + str(len(dogNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dogNames = dogNames + [name]  # list concatenation
print('The dog names are:')
for name in dogNames:
    print('  ' + name)
