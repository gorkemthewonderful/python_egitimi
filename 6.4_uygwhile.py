

from bisect import bisect_right
from hmac import compare_digest


sayilar = [1,3,5,7,9,12,19,21]

# 1- sayıalrı while ile ekrana yazdır.

# i = 0
# while len(sayilar) > i:
#     print(sayilar[i])
#     i += 1

# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tek sayıları ekrana yazdır.

# bas = int(input("Başlangıç sayısı: "))
# bit = int(input("Bitiş sayısı: "))

# i=bas
# while i<bit:
    
#     if i % 2 == 1:
#         print(i)
#     i += 1

# 3- 1-100 arasındaki sayıları düşüğe doğru yazdır.

# i = 100

# while i > 0:
#     print(i)
#     i -= 1

# 4- kullanıcıdan alacağınız 5 sayıyı sıralı şekilde yazdırın.

# numbers = []

# i = 0

# while i < 5:
#     sayi = int(input("Sayı: "))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)



# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde 

# - ürün sayısını kullanıcıya sor
# - dictionary listesi yapısı (name,price) şeklinde olsun
# - ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin.

# urunler = []

# adet = int(input("Kaç adet ürün girmek istiyorsunuz?"))

# i = 0

# while i < adet:

#     name = input("ürün ismi: ")
#     price = int(input("ürün fiyatı: "))
#     urunler.append({"name": name,"price": price})
#     i+=1

# print(urunler)


