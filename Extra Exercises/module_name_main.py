# ******************************
# if __name__ == '__main__'
# ******************************

# y tho?
# 1. Module can be run as a standalo program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables" , one of which is __name__
# then Python will execute the code found within __main__

if __name__ == '__main__':
    print('Running this module directly')
else:
    print('Running other module indirectly')
