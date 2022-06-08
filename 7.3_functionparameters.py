# def changeName(n):
#     n = "görkem"

# name = "Yılmaz"
# changeName(name)
# print(name) #tanımladığım name fonksiyon tarafından değiştirilemedi


# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]

# change(sehirler)
# print(sehirler)

# sehirler = ["ankara", "izmir"]
# n = sehirler[:] #slicing FARKLI LİSTELER MEYDANA GETİRİR VE ORİJİNAL LİSTEYE VB. DOKUNMAMIŞ OLURUZ. :'NIN SAĞ VE SOLUNA LİSTENİN KAÇINCI ELEMANLARINI KAPSAMASINI İSTEDİĞİNİ YAZ.
# n[0] = "istanbul"
# print(sehirler)
# print(n)

# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]

# change(sehirler[:]) #>>>> : LİSTENİN YENİ BİR KOPYASININ OLUŞMASINI SAĞLAR
# print(sehirler)

# change(sehirler)
# print(sehirler)

# def add(a, b, c = 0):
#     return sum((a, b, c)) # >>> 2 parantez koyduk sebebini anlamadım.

# print(add(10,20))
# print(add(10, 20, 30)) #>>> fonksiyon 2 değişken bekliyordu ancak biz 3 değişken yazdık ve hata verdi. Bunun için def'in yanındaki paranteze c = 0 yazarsak fonksiyonu hem 2 hem 3 değişkenle kullanabiliriz. ama aşağıya da c'yi eklemeyi unutma. YILDIZ...

# def add(*params):  #>>> parantezin başına * koymak eklediğimiz tüm değişkenleri kapsamasını sağlar.YILDIZ
    
#     return(sum(params))

# print(add(10,20,30,40,50,60))

# def add(*params):  
#     sum = 0
    
#     for n in params:
#         sum += n

#     return sum # >>> sum kullanmak istemezsek ?

# print(add(10,20))

def displayUser(**params): #>>> ** dıctıonary yapıyo kanka elleşme.
    for keys, value in params.items():
        print("{} is {}".format(keys,value))


displayUser(name = "görkem", age = 24,  city = "ankara")
displayUser(name = "göko", age = 25, city = "izmir", phone = "123123")
displayUser(name = "gökos", age = 31, city = "istanbul",  phone = "313131", email = "goko@gmail.com") #DAFUQ