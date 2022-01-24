# dictionary = A changeable, unordered collection of unique key: value pairs;
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(capitals['Russia'])
print(capitals['India'])

capitals.update({'Germany': 'Berlin'})
print(capitals.keys())
print(capitals.values())
# print(capitals.items())
capitals.update({'China': 'Hong Kong'})
capitals.pop('China')
# capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany')) # will return None if isnt in th dictionary

for key,value in capitals.items():
    print(f'The capital of {key} is {value}.')

