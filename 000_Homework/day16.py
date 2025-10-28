# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

import datetime

now = datetime.datetime.now()
# print(now)

day = now.day
print(day)
month = now.month
print(month)
year = now.year
print(year)
hour = now.hour
print(hour)
minute = now.minute
print(minute)
timestamp = now.timestamp()
print(timestamp)


# 1. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
cur_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(cur_date)

# 1. Today is 5 December, 2019. Change this time string to time.

todayz = "5 December, 2019"
print(todayz)

time = datetime.datetime.strptime(todayz, "%d %B, %Y")
print("time is:", time)

# 1. Calculate the time difference between now and new year.
now = datetime.datetime(2025, 10, 27, 9, 45, 00)
new_year = datetime.datetime(2026, 1, 1, 00, 00)
days_rem = new_year - now
print(days_rem)

# 1. Calculate the time difference between 1 January 1970 and now.

old = datetime.datetime(1970, 1, 1, 00, 00, 1)
now2 = datetime.datetime(2025, 10, 27, 9, 45, 00)

diff = now2 - old
print(diff)

#
