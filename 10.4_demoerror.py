# from operator import contains


# liste =["1","2","5a","10b","abc","10","50"]

#Liste elemanlarındaki sayısal değerleri bul.
#BENİM YORUMUM
# def check_list(lst):
#     import re
#     if re.search (["0-9"],lst):
#         print()

# while True:
#     try:
#         check_list(liste)
#     except Exception as ex:
#         print(ex)
#     else:
#         print("İşlem tamam.")
# check_list(liste)
#DOĞRU CEVAP
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue
        

#Kullanıcı 'q' değerlerini girmedikçe aldığınız her inputun sayı olduğundan emin olun yoksa hata mesajı alın.
#BENİM YORUMUM
# def qyok(deger):
#     import re
#     if re.search(("q",deger)):
#         raise Exception ("orda dur lan")

# deger = input("Değer: ")

# while True:
#     try:
#         qyok(deger)
#     except Exception as ex :
#         print(ex)
#DORĞUSU
# while True:
#     sayi = input("Sayı: ")
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print("Girdiğiniz değer bir sayı.")
#     except ValueError:
#         print("Girdiğiniz değer bir sayı değil.")
#         continue


#Girilen parola içinde türkçe karakter hatası veriniz.
#BENİM YORUMUM :D
# def tr_psw(passw):
#     import re
#     if not re.search("[ğ,ü,ı,ş,ö,ç]",passw):
#         print("Parolanız başarıyla oluşturuldu.")
#     else:
#         raise Exception("Parolanız türkçe karakter içeremez.")

# while True:
#     try:
#         passw = input("Parola giriniz: ")
#         tr_psw(passw)
#     except:
#         break
#     finally:
#         print("Parola oluşturma tamamlandı.")

#DOĞRU CEVAP
# turkce_karakterler = "ğşlıçöİ"
    
# parola = input("Password: ")
# for i in parola:
#     if i in turkce_karakterler:
#         raise TypeError("Parolanız türkçe karakter içeremez.")
#         continue
#     else:
#         pass

# print("Geçerli parola.")
#Faktöriyel fonksiyonu oluşturup fonksiyona gelen her değer için hata mesajı verin.


