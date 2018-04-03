


import  datetime

unix_time = 1521281164

print(datetime.datetime.fromtimestamp(unix_time))

print(datetime.date.today()) # today's date

# creating a date
some_day = datetime.date(2017, 5, 22)

print(some_day) # 2017-05-22

print(str(some_day.day ) + '--' + str(some_day.month) + '--' + str(some_day.year))


# getting weekday of a date
# weekday() --> Monday = 0 & Sunday = 6
tday = datetime.date.today()
print(tday.weekday())





