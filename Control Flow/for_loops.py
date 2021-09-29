cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    
print(capitalized_cities)

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
    
print(cities)

# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)
    
# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.

# >>> range(start=0, stop, step=1)
for num in range(5, 31, 5):
    print(num)

"""Create Usernames

Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores."""

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))
    
print(names)
print(usernames)

"""Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

>>> The printed output for the names list will look exactly like it did in the first line.
>>> During each iteration, the name variable is set to a string taken from the list. Then the assignment statement creates a new string (name.lower().replace(" ", "_")) and changes the name variable to that string. It doesn't modify the contents of the names list at all. To modify the list you must operate on the list itself, using range, as you saw earlier.
"""
"""Modify Usernames with Range

Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"""

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for name in range(len(usernames)):
    usernames[name] = usernames[name].lower().replace(' ', '_')

print('With range:',usernames)

"""Tag Counter

Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings."""

tokens = ['<greeting>', 'Hello World!', '</greeting>', '<Hello World>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

"""Create an HTML List

Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>

That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>."""

items = ['first string', 'second string']
html_str = "<ul>\n"  
# "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

for item in items:
    html_str += ' <li>{}</li>\n'.format(item)
html_str += '</ul>'

print(html_str)

"""
print(list(range(4))) >>> [0,1,2,3]
print(list(range(4, 8))) >>> [4,5,6,7]
print(list(range(4,10,2))) >>> [4,6,8]
print(list(range(0,-5))) >>> []
"""