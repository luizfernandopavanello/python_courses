"""Users API response

You have a users.json file which represents a response from an API with a list of users.

Read that file and store in a user_fullnames list the fullname (firstname + lastname, with a blank space in the middle) of every user on that file.

    Hint: you will need to read the file content before loading it as JSON.
"""

import json

user_fullnames = []

with open('users.json','r') as file:
    json_file = json.loads(file.read())
    
    for item in json_file:
        fullname = item['firstName'] + ' ' + item['lastName']
        user_fullnames.append(fullname)

print(user_fullnames)
