from datetime import date, timedelta
import sqlite3


def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

def allsaturday(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 5 - d.weekday())  # First Saturday
   if d.year < year:
    d += timedelta(days = 7)
   while d.year == year:
      yield d
      d += timedelta(days = 7)
    

con = sqlite3.connect('calendar1.db')
cur = con.cursor()

start_year = 2018 ## Dien nam can import data

start_date = date(start_year, 1, 1) 
end_date = date(start_year, 12, 31)    # perhaps date.now()
delta = end_date - start_date   # returns timedelta

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    cur.execute("INSERT INTO DATE (DATEKEY, ISHOLIDAY) VALUES ('{}', 0)".format(day))
    con.commit()
    print("Done record {}".format(day))

for d in allsaturday(start_year):
    cur.execute("update date set isholiday='1' where datekey='{}' ".format(d))
    con.commit()
    print("Done update record {} Saturday".format(d))

for d in allsundays(start_year):
    cur.execute("update date set isholiday='1' where datekey='{}' ".format(d))
    con.commit()
    print("Done update record {} Sunday".format(d))


## Tham Khao lich nghi chinh thuc tu VSD
## https://vsd.vn/vi/lich-giao-dich?tab=LICH_NGHI_GIAODICH&date=12/04/2022&page=1&ks=2023

####### Tet Tay ##############
start_date_tettay = date(start_year, 1, 1) 
end_date_tettay = date(start_year, 1, 1)    # perhaps date.now()
delta_tettay = end_date_tettay - start_date_tettay   # returns timedelta

for i in range(delta_tettay.days + 1):
    day = start_date_tettay + timedelta(days=i)
    cur.execute("update date set isholiday='1' where datekey='{}'".format(day))
    con.commit()
    print("Done record National Holiday - Tet Tay {}".format(day))



####### Tet Ta #############
start_date_tetta = date(start_year, 2, 14) # Ngay bat dau tet ta
end_date_tetta = date(start_year, 2, 20)    # Ngay ket thuc tet ta
delta_tetta = end_date_tetta - start_date_tetta  

for i in range(delta_tetta.days + 1):
    day = start_date_tetta + timedelta(days=i)
    cur.execute("update date set isholiday='1' where datekey='{}'".format(day))
    con.commit()
    print("Done record National Holiday - Tet Ta {}".format(day))

###### Gio to vua Hung - Nghi le tu 2007 #######

start_date_gioto = date(start_year, 4, 25) 
end_date_gioto = date(start_year, 4, 25)    
delta_gioto = end_date_gioto - start_date_gioto   

for i in range(delta_gioto.days + 1):
    day = start_date_gioto + timedelta(days=i)
    cur.execute("update date set isholiday='1' where datekey='{}'".format(day))
    con.commit()
    print("Done record National Holiday - Go To Hung Vuong {}".format(day))


####### 30/04 va 01/05 ##############
start_date_30040105 = date(start_year, 4, 30) 
end_date_30040105 = date(start_year, 5, 1)    # perhaps date.now()
delta_30040105 = end_date_30040105 - start_date_30040105   # returns timedelta

for i in range(delta_30040105.days + 1):
    day = start_date_30040105 + timedelta(days=i)
    cur.execute("update date set isholiday='1' where datekey='{}'".format(day))
    con.commit()
    print("Done record National Holiday - 30/4 - 01/05 {}".format(day))

####### 02/09 ##############
start_date_0209 = date(start_year, 9, 3) 
end_date_0209 = date(start_year, 9, 3)    # perhaps date.now()
delta_0209 = end_date_0209 - start_date_0209   # returns timedelta

for i in range(delta_0209.days + 1):
    day = start_date_0209 + timedelta(days=i)
    cur.execute("update date set isholiday='1' where datekey='{}'".format(day))
    con.commit()
    print("Done record National Holiday - Quoc Khanh {}".format(day))
