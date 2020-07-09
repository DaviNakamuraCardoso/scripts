import threading
import time
import datetime

print('Start of Program')


def take_a_nap(): # First we define a function
    time.sleep(5)
    print('Wake up!')


thread_object = threading.Thread(target=take_a_nap) # Then we create a threading object, with it's target. Note that you
# MUST NOT put () in the target
thread_object.start()

print('End of program. ')

thread_ob = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '}) # Passing arguments
# to a thread object, and the keyword argument sep
thread_ob.start()

