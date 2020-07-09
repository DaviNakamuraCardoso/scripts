import time

print('Press ENTER to begin. Afterward, press ENTER  to "click" the stopwatch. Press Crtl+C to quit.')
input() # Press enter to begin
print('Started')
start_time = time.time() # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #%s: %s (%s)' % (lap_num, total_time, lap_time))
        lap_num += 1
        last_time = time.time() # reset the lap time

except KeyboardInterrupt:
    # Handle the Crtl+C exception to keep its error message from displaying
    print('\nDone.')

