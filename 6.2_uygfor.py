from ast import Div
from re import X


sayilar = [1,3,5,7,9,12,19,21]

# 1- sayılardan hangisi 3'ün katıdır?
# 2- sayıların toplamı kaçtır?
# tek sayıların karesi?

# 1- for th in sayilar:
#     if(th%3 == 0):
#         print(th)

# 2- toplam = 0
# for sayi in sayilar:
#     toplam += sayi               # =+ olmaz ve bunun anlamı > toplam = toplam + sayi
#     print(toplam)

# 3- for t in sayilar: 
#    if(t % 2 == 1):
#        print(t**2)
        
    
sehirler = ["kocaeli", "istanbul", "ankara", "izmir","rize"]

# şehirlerden hangisi max 5 harflidir?

# for five in sehirler:
#     if len(five) <= 5:
#         print(five)


urunler = [
     {"name": "samsung s6", "price": "3000"},
     {"name": "samsung s7", "price": "4000"},
     {"name": "samsung s8", "price": "5000"},
     {"name": "samsung s9", "price": "6000"},
     {"name": "samsung s10", "price": "7000"},
 ]

# 1-Ürünler fiyatları toplamı?
# zero = 0
# for prices in urunler:
#     fiyat = int(prices["price"])
#     zero += fiyat
# print(zero)
    
        
# 2-Ürün fiyatı max 5000 olanları yazdır?

# for urun in urunler:
#     if(int(urun["price"]) <= 5000):
#         print(urun["name"])