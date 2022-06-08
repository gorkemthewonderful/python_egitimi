# x = 10

# if x > 5:
#     raise Exception("x, 5 den büyük değer alamaz.") #raise metodu bize hata fırlatmasını sağlar kodun.

# def check_password(psw):
#     import re
#     if len (psw) < 7:
#         raise Exception("Parolanız en az 8 karakter olmalıdır.")
#     elif not re.search ("[a-z]", psw):
#         raise Exception("Parolanız küçük harf içermelidir.")
#     elif not re.search ("[A-Z]", psw):
#         raise Exception("Parolanız büyük farf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parolanız bir rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parolanız alpha numeric karakter içermelidir.")
#     elif re.search("\s", psw): #\s regular expressionda boşluk demek
#         raise Exception("Parolanız boşluk içermemelidir.")
#     else:
#         print("Parolanız oluşturuldu.")

# password = "12345678aA@ "

# try:
#     check_password(password)
# except Exception as ex:
#     print (ex)
# else:
#     print("Parolanız oluşturuldu2.") #bunu fonksiyonun içine de buraya da yazabiliriz yani :)
# finally:
#     print("Validation tamamlandı.") #niceeee

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception ("İsminiz fazla karakter içeriyor.")
        else:
            self.name = name


p = Person ("GÖKOOOOOgggggO", 1984) #isminiz fazla karakter içeriyor hatası.