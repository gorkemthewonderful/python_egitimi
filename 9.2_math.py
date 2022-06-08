#Yöntem 1
# import math 
# import math as islem #as komutu modülün ismini değiştirir

# # value = dir(math)
# # help(math) #bununla math modülü içerisindeki tüm fonksiyonlar hakkında bilgi al
# # value = (help(math.factorial)) #bununla da modül içerisindeki spesifik bir fonskiyon hakkında bilgi al.
# value = math.factorial(5)
# value = math.sqrt(49)
# value = math.floor(5.6)
# value = math.ceil(5.6)
# print(value)

# #işlem yaptıktan sonra mathin ismini

# value = islem.floor(5.5)
# print(value)

#Yöntem 2 

# from math import * #from kullandığımızda math. kullanmamıza gerek kalmaz bu örnekte (sanırım)
from math import factorial,sqrt,pi #import sonrası yalnızca kullanacağımız fonksiyonları yazarak da kullanabiliriz metodu
# EĞER BİZ HAZIR BİR MODÜLÜN İÇİNDEKİ HAZIR BİR FONKSİYONLA AYNI İSİMLİ BİR FONKSİYON TANIMLARSAK EN SON HANGİSİ YAZILMIŞSA (YANİ IMPORT MU YOKSA BİZİM YAZDIĞIMIN FONKSİYON MU) O GEÇERLİDİR
value = factorial(5)
value = sqrt(pi)

print(value)




