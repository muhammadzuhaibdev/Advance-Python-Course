from datetime import date
d1 = date(2004, 12, 30)
d2 = date(2026, 12, 30)

print((d2 - d1).days)


# from datetime import date, timedelta
# today = date.today()
# future = today + timedelta(days=5)
# print("Today:", today)
# print("Future:", future)

# import calendar
# print(calendar.isleap(2026))
# print(calendar.month(2026, 3))
# print(calendar.calendar(2026))














# import time
# print(time.localtime())
# print(time.ctime())
# time.sleep(2)
# print(time.time())




# import datetime
# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)


# date_str = "30-03-2026"
# date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
# print(date_obj)


# formatted = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
# print(formatted)
# d = datetime.date(2026, 3, 30)
# dt = datetime.datetime(2026, 3, 30, 10, 30, 0)
# print(d)
# print(dt)

# today = datetime.date.today()
# print(datetime.datetime.now())

# from test import sum as add
# import test

# print(test.userName)

# result = add(10, 20)
# print(result)