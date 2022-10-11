from datetime import date, timedelta

def allsaturday(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 5 - d.weekday())  # First Sunday
   if d.year < year:
    d += timedelta(days = 7)
   while d.year == year:
      yield d
      d += timedelta(days = 7)

def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

for d in allsaturday(2023):
   print(d)

# for d in allsaturday(2023):
#     print(d)
