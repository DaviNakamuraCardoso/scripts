import time
import datetime

print(time.time()) # time.time() returns the time, in seconds, passed since 1º January 12 AM, 1970. It's usefull to
# calculate the time passed from the start to the end of a program


def calc_prod():
    start_time = time.time()
    product = 1
    for i in range(1, 100000):
        product = product * i

    end_time = time.time()
    print('The result is %s digits long.' % (len(str(product))))
    print('Took %s seconds to calculate.' % (end_time - start_time))


#calc_prod()
# Another way to profile your code is to use cProfile.run() function
print(time.ctime()) # The time.ctime function returns a string description of the current time.
this_moment = time.time()
print(time.ctime(this_moment))
for i in range(3):
    print('Tick') # If you want your program to stop for a while, call the time.sleep() function
    time.sleep(1)
    print('Tack')
    time.sleep(1)

# You can round numbers with the Python's round() function

now = time.time()
print(round(now, 2))
now_date = datetime.datetime.now()
now = now_date.strftime('%A %H:%M')
while now != 'Thursday 16:08' and now != 'Saturday 8:09' and now != 'Sunday 23:09':
    print('NOT')
    print(now)

print('finally')
