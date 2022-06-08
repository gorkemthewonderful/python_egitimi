#decorator fonksiyonları bir fonksiyona bir özellik eklemek istediğimizde kullanırız.
# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan çnceki işlemler")
#         func()
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# def sayHello():
#     print("Hello.")

# def sayGreeting():
#     print("Greetings")

# def sayHello():
#     print("Hello.")

# sayHello = my_decorator(sayHello)
# sayHello() ######bu üstteki 2 satırın aynısı aşağdıaki

# @my_decorator #@ bir decoratorın altındaki tüm fonksiyonları o decoratora eşitler...

# def sayHello():
#     print("Hello.")

# sayHello()
###############################################################################################
# def my_decorator(func):
#     def wrapper(name): #<<<<<<<<<<<
#         print("fonksiyondan çnceki işlemler")
#         func(name) #<<<<<<<<<<<
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name): #sadece buraya name yazarsak...
#     print("Hello.", name)

# sayHello("Görkem") #...burada hata alırız çünkü bu fonksiyon aslıdna yukarıda okla gösterdiğim tarafa geldi ve orası boş. yani oraya da name parametresini eklediğimde bu komut hata vermez.
##############################################################################
import math
import time


# def usalma(a,b):
#     start = time.time()
#     time.sleep(1) #.sleep fonksiyonu bekletir.

#     print(math.pow(a,b))
    
#     finish = time.time()
#     print("fonksiyon " + str(finish - start) + " saniye sürdü")

# def faktoriyel(num):
#     start = time.time()
#     time.sleep(1)

#     print(math.factorial(num))
    
#     finish = time.time()
#     print("fonksiyon " + str(finish - start) + " saniye sürdü")


# usalma(3,4)
# faktoriyel(5)
#########################BURASI KOMPLE AŞAĞIYA EŞİT##############################

def calculate_time(func):
    def inner(*cukubik, **fikibok):
    
        start = time.time()
        time.sleep(1)
        func(*cukubik, **fikibok) #YILDIZLAR HATIRLAYACAĞIMIZ ÜZERE FONKSİYON PARAMETRE SAYISININ ESNEKLİĞİNE YARIYORDU YANİ YILDIZ KOYDUĞUMUZDA İSTEDİĞMİİZ KADAR PARAMETRE KOYDUĞUMUZ İÇİN DAHA ESNEK BİR YAPI HALİNE GELİYOR BÖYLECE.
        finish = time.time()
        print(func.__name__ +" adlı fonksiyon " + str(finish - start) + " saniye sürdü")    
    return inner
#buralardaki ahenklere imzalara dikkat abi çok iyi yani:D BURASI ASIL OLAY YANİ DECORATIVE FONKSİYON BURASI ASIL

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    
usalma(3,4)
faktoriyel(5)

#ÖZETLE BURADA BİR ÖZELLİK(DECORATOR) FONKSİYONU (BU ÖRNEKTE TIME) YAZIP YALNIZCA @ İŞARETİ İLE ONU BAŞKA FONKSİYONLARIN İÇİNE DAHİL EDEREK DAHA AZ KOD YAZIP AYNI İŞİ YAPABİLDİK. 