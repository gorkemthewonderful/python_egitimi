# from datetime import date
# from datetime import time
# from datetime import datetime
##########################################################################
# import datetime
# result = (dir(datetime))
# result2 = dir(datetime.datetime)
# result3 = dir(datetime.time)
# result4 = dir(datetime.date)
# print(result)
# print(result2)
# print(result3)
# print(result4)

from datetime import date, datetime
from datetime import timedelta

# result = dir(datetime)
# print(result)
##########################################################################
# result = datetime.now()
# print(result)
##########################################################################
# simdi = datetime.now() #now yerine today de kullanılabilir.
# result = simdi.day
# result = simdi.month
# result = simdi.second 
# print(result)
##########################################################################
# simdi = datetime.now()
# result = datetime.ctime(simdi)
# print(result) #daha açıklayıcı bilgi için ctime kullanılabilir.
##########################################################################
# simdi = datetime.now()
# result = datetime.strftime(simdi,"%Y") #strftime ctime ile gelen string bilgiden spesifik bir bilgiyi yazdırmamızı sağlar. %Y yılı, %X saati, %d günü vs.
# result = datetime.strftime(simdi,"%a")
# result = datetime.strftime(simdi,"%b") 
# result = datetime.strftime(simdi,"%Y %B %A %H %M") 
# print(result)
##########################################################################
# t = "25 Mayıs 2022"
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)
##########################################################################
# t = "25 May 2022 hour 12:28:49" #burada ayı türkçe girmemeliyiz...
# dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S") #sözün özü strptime metodu bizim default olarak string girdiğimiz bir ifadeyi doğru %'li ifadelerle eşleştirerek tarih formatına dönüştürmemizi sağlar.
# print(dt)
# print(dt.year)
# print(dt.second)
##########################################################################
# birthday = datetime(1998,6,18,18,30,00)
# print(birthday)
##########################################################################
# birthday = datetime(1998,6,18,18,30,00)
# result = datetime.timestamp(birthday) #saniye
# result2 = datetime.fromtimestamp(result) #saniye to datetime
# result3 = datetime.fromtimestamp(0) #buradaki parantez içi saniye abi.
# print(result)
# print(result2)
# print(result3) #1970-01-01 03:00:00 bu tarih bilgisayarlar için milat kabul edilir :O
##########################################################################
# simdi = datetime.now()
# birthday = datetime(1998,6,18,18,30,00)
# result = datetime.fromtimestamp(0)
##########################################################################
# yas = simdi - birthday #timedelta > 2 tarih arasındaki fark
# yas = yas.days
# yas = yas.seconds
# yas = yas.microseconds
# print(yas)
#from datetime import timedelta
##########################################################################
# simdi = datetime.now()
# result = simdi + timedelta(days = 10) #burası mevcut güne(simdi) 10 gün ekledi abi.
# result = simdi + timedelta(minutes = 10) #burası mevcut güne(simdi) 10 dakika ekledi.
# result = simdi + timedelta(days = 730, minutes=10) #burası mevcut güne(simdi) 2 yıl 10 dakika ekledi.

# print(result)



