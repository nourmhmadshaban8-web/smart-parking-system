import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().min)
print(datetime.datetime.now().max)


#====================================================================


print(datetime.datetime.now().time())
print(datetime.datetime.now().time().max)
print(datetime.datetime.now().time().min)


#====================================================================


my_birth_day=datetime.datetime(2007,1,21)
date_now=datetime.datetime.now()
print(f"i lived for {date_now-my_birth_day}")


#====================================================================


print(my_birth_day.strftime("%d / %b / %y")) # 14 / May / 07
print(my_birth_day.strftime("%d / %B / %Y")) # 14 / May / 2007
print(my_birth_day.strftime("%a")) # Mon
print(my_birth_day.strftime("%A")) # Monday