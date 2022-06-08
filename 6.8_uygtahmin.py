# 1-100 arasından rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile bulmaya çalış (hak = 5)
# **random modülü** için python random diye arama yap
# 100 üzerinden puanlama her soru 20 puannnm
# hak bilgisini kullanıcıdan al ve her soru belirtilen can sayısı üzerinden hesaplansın.

import random
hak = int(input("Kaç deneme hakkınız olsun?: "))
y = 1
list1 = [z for z in range(100)]
z = random.choice(list1)
p = 0

while y <= hak:
    
    y += 1
    puanMatrahi = (100 / hak) * (y - 1)
    p = 100 - puanMatrahi
    
    x = int(input("1 ile 100 arası bir sayı yaz: "))

    if x > z:
        print("Sayın sayıdan büyük. Aşağı in.")
    elif x == z:
        print("Tebrikler. Sayın doğru")
        break
    elif x < z:
        print("Sayın sayıdan küçük. Yukarı çık.")

print(f"Sayı {z}'di")
print(f'Puanın {p}')
    