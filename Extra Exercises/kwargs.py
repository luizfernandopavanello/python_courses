# **kwargs = parameter that will pack all the arguments into a dictionary;
#                     usefull so that a function can accept a varying amount of keyword arguments.

def hello(**kwargs):
    if 'name' in kwargs:
        print('Hello ' + kwargs['name'] + '!')
    elif 'first_name' in kwargs and 'last_name' in kwargs:
        print('Hello ' + kwargs['first_name'] + ' ' + kwargs['last_name'] + '!')

hello(first_name='John', last_name='Doe')