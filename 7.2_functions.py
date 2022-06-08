#fonksiyonlar def (define) yapılır.

# def sayHello():
#     print("Hello")

# sayHello()

# def sayHello(name):
#     print("Hello " + name)

# sayHello("Görkem")

# def sayHello(name = "User"):
#     print("Hello " + name)

# sayHello("Görkem")
# sayHello() #eğer parametrenin içi boş kalırsa üstteki parametrenin yanına bir varsayılan (örnekte user) kullanarak hata almayız

# def sayHello(name = "User"):
#     return "Hello " + name

# msg = sayHello("Görkem")
# print(msg)  # return fonksiyona gönderdiğmiiz bir bilgiyi geri döndürür.

# def total (num1, num2):
#     return num1 + num2

# result = total(100, 20)
# print(result) # return kullanırken bir değişken tanımlamalıyız ki returndeki bilgi o değişkene dönsün.

def yasHesapla (dogumYili):
    return 2022 - dogumYili

# ageGorkem = yasHesapla(1998)
# ageGozde = yasHesapla(1996)
# ageDilek = yasHesapla(1970)
# print(ageGorkem, ageGozde, ageDilek)

# def EmekliligeKacYilKaldi (dogumYili):
#     '''
#     Emekliliginize kac yil kaldigini ogrenmek ister misiniz?
#     DOGUM TARIHINIZI GIRIN VE EMEKLILIGINIZE KAC YIL KALDIGINI OGRENIN
#     '''
#     yas = 2022 - dogumYili
#     emeklilik = 65 - yas
#     if emeklilik > 0:
#         print (f"Emekliliğine {emeklilik} yıl kaldı.")
#     elif emeklilik == 0:
#         print("Emeklilik yılınız geldi.")
#     elif emeklilik < 0:
#         print("Siz emeklisiniz.")

# print(help(EmekliligeKacYilKaldi))
# EmekliligeKacYilKaldi(1957) #help metodu bir metod veya fonksiyonun nasıl, ne için kullanıldığını yazdırır. fonksiyon içindeki stringi yazdırıyor diye anladım?

# list = [1, 2, 3]
# print(help(list.append))



