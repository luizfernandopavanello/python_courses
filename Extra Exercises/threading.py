# → thread =  a flow of execution, Like a separate order of instructions;
#             However each thread takes a turn running to achieve concurrency;
#             GIL = global interpreter lock;
#             allows only one thread to hold the control of the Python interpreter at any time.

# cpu bound = program/task spends most of its time waiting for internal events
#             (CPU intensive) use multiprocessing
#
# io bound = program/task spends most of its time waiting for external events
#            (user input, web scraping) use multithreading

import threading
import time

def  eat_breakfast():
    time.sleep(3)
    print('You eat your breakfast.')

def drink_coffee():
    time.sleep(4)
    print('You drink coffe.')

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

# eat_breakfast()
# drink_coffee()

print(threading.active_count())
print(threading.enumerate())

