import itertools

str = input('String a ser permutada: ')

result = itertools.permutations(str, len(str))

for i in result:
	print(''.join(i))