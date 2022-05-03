import datetime
import pytz

# d = datetime.date(2016,7,24)
# # print(d)
# tday = datetime.date.today()
# # print(tday.weekday())
# # print(tday.isoweekday())

# tdelta = datetime.timedelta(days=7)
# # print(tday - tdelta)

# # date2 = date1 + timedelta
# # timedelta = date1 + date2

# bday = datetime.date(2023,4,14)
# till_bday = bday - tday
# print(till_bday)

# t = datetime.time(12,30,45,100)
# td = datetime.timedelta(hours=12)
# print(t.hour)

# dt = datetime.datetime(2016,7,26,12,30,45,1000)
# tdelta = datetime.timedelta(days=7)
# print(dt + tdelta)


# dt_today  = datetime.datetime.today()
dt_utcnow =  datetime.datetime.now(tz=pytz.UTC)
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2022,4,27,2,47,30, tzinfo=pytz.UTC)
# print(dt_utcnow)

dt_accra = dt_utcnow.astimezone(pytz.timezone('Africa/Accra'))
# print(dt_accra)

# for tz in pytz.all_timezones:
    # print(tz)

# dt_str = 'July 26, 2016'

# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)

dt = datetime.date(2022,4,20)
t_delta = datetime.timedelta(days=29)
dt2 = dt + t_delta
print(dt2)