import datetime
import time
print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(1_000_000_000))
print(datetime.datetime.fromtimestamp(time.time()))
today = datetime.datetime.now()
next_year = datetime.datetime(2021, 1, 1, 0, 0, 0)
time2021 = datetime.datetime(2021, 1, 1, 0, 0, 0)
print(today > next_year) # The greater (later) datetime in this case is next_year, so expression is False
print(next_year == time2021) # next_year and time2021 are the same, and the exp is True
print(today < time2021) # The expression is True, for time2021 is greater(later) than today
print(next_year != time2021)
print(today != time2021)
# The timedelta type
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print(delta.total_seconds())
print(str(delta))
dt = datetime.datetime.now()
thousand_days = datetime.timedelta(days=1000)
print(dt + thousand_days)
dark_delta = datetime.timedelta(days=365*33)
dark_present = datetime.datetime(2020, 9, 21, 19, 30, 0)
dark_past = dark_present - dark_delta
dark_future = dark_present + dark_delta

print(dark_past)
print(dark_present)
print(dark_future)

# Pausing until a specific date
today_meeting = datetime.datetime(2020, 7, 9, 19, 30, 0)
#while datetime.datetime.now() < today_meeting:
 #   time.sleep(1)

print(dark_past.strftime('%I:%M%p')) # You can use the strftime method to convert datetime objects to single-quoted
# readable strings
print(today_meeting.strftime("%B of %Y"))
print(today_meeting.strftime('%A %H:%M'))

# The strptime is the inverse: it converts a string to a datetime object
print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))


