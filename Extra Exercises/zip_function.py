"""
→ zip(*iterables) = aggregate elements from two  more iterables (list, tuples, sets, etc.);
                    creates a zip object with paired elements stored in tuples for each element
"""

usernames = ["Dude", "Trevi", "Mister"]
passwords = ["p@assords", "abc123", "guests"]
logins = ["1/1/2022", "8/1/2022", "25/1/2022"]

users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items():
    print(key + " : " + value)

users_two = (zip(usernames, passwords, logins))

print(type(users_two))

for i in users_two:
    print(f"The user {i[0]} with the password '{i[1]}', last login was at {i[2]}.")