# 1- Göderilen bir kelimeyi belirtilen kez ekrana yazdıran fonksiyon.
# 2- Kendine gönderilen sınırsız parametreyi listeye çeviren fonksiyon.
# 3- Gönderilen 2 sayı arasındaki tüm asal sayılar.
# 4- Kendisine gönderilen bir sayının tam bölenlerini çıkaran fonksiyon.


# def kelime(keli, x):
#     print(keli * x)

# kelime("görkem\n", 10) #>>> \n (new line) girilen veriyi alt alta yazar.


# def words(*kelimeler):
#     liste = []

#     for param in kelimeler:
#         liste.append(param)

#     return liste

# result = words(1, 2, 23)
# print(result)

# def words(*word):
#     list = []

#     list.append(word)

#     return list

# asd = words(1,2,3)
# print(asd) >>> BENİM YORUMUM :(


# def asalSayilar(a, b):
#     for i in range(a, b + 1):
#         if i > 1:
#             for sayi in range(2, i):
#                 if (i % sayi == 0):
#                     break
#             else:
#                 print(f"{i} asal sayıdır. ")

# a = int(input("1. Sayı: "))
# b = int(input("2. Sayı: "))

# asalSayilar(a,b)


# def bolen(a):
#     tamBolenler = []
    
#     for i in range(1, a):
#         if a % i == 0:
#             tamBolenler.append(i)
#         else:
#             continue
        
#     print(tamBolenler)

# a = int(input("Sayı: "))

# bolen(a)


