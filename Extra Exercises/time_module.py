import time

print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
                        # epoch = when your computer thinks time began(reference point)
#                                 a date and time from which a computer measures system time

print(time.time()) # return current seconds since epoch
print(time.ctime(time.time())) # will get the current time

# time.strftime(format, time_object) = formats a time_object to a string
time_object = time.localtime()
time_object = time.gmtime() # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = '23 January, 2022'
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2021, 1, 23, 4, 34, 0, 0, 0, 0)
time_String = time.asctime(time_tuple)
print(time_String)