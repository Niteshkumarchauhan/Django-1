from datetime import datetime

time_str = '2:40 PM'
date_str = '18-05-2022'
# datetime_str = '18 05 2022 5:40'
# date_obj = datetime.strptime(datetime_str,"%d %m %Y %H:%M")
# time_obj = datetime.strptime(time_str,"%H:%M")
# date_obj = datetime.strptime(date_str,"%d %m %Y")

# print(date_obj)
# print(time_obj)
d = datetime.strptime(date_str,'%d-%m-%Y')
t = datetime.strptime(time_str,'%I:%M %p')
print(d)
print(t)
print(datetime.combine(d.date(), t.time()))

