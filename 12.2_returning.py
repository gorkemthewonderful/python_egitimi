# def usalma(number):
#     def inner(power):
#         return number ** power

#     return inner #FONKSİYONU DÖNDÜRMEK ZORUNDAYIZ BU TARZ FONKSİYONLARDA YANİ OFNKSİYONUN İÇİNDE FONKSİYONU DİREKT KULLANMA.

# two = usalma(2)
# three = usalma(3) # bu ikisi bizim inner fonksiyonumuzu temsil ediyor. bu işlemlerle fonksiyonu başka bir değere eşitleyip iç içe fonksiyon kullandık yani ÇOK ÖNEMLİ
# print(two(3))
# print(three(3))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "admin":
#             return "{0} rolü {1} sayfasına ulaşabilir." .format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz." .format(role,page)
#     return(inner)

# user1 = yetki_sorgula("Product Edit")
# print(user1 ("admin")) #admin rolü Product Edit sayfasına ulaşabilir.
# print(user1 ("User")) #User rolü Product Edit sayfasına ulaşamaz.


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam #buradaki her toplam fonksiyon adıyla aynı olmak zorunda ??

    def carpma(*args):
        carpma = 1
        for i in args:
            carpma *= i
        return carpma #buradaki her carpma fonksiyon adıyla aynı olmak zorunda ??

    if islem_adi == "toplam":
        return toplam
    elif islem_adi == "çarpma":
        return carpma
   
toplam = islem("toplam")
print(toplam(1,3,5,6,19))

carpim = islem("toplam")
print(carpim(6,9,3,4,5))

carpma = islem("çarpma")
print(carpma(6,9,3,4,5))







