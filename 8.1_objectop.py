#OBJECT ORIENTED PROGRAMMING

# class
#instance (object) > bir class içerisinde belli özellikleri vb. verilecek nesneler

# lst = [1,2,3]

# result = type(lst)

# print(result)

# #class > person (name, surname, birthday, calculateAge()) 
# #metodlar ise üstteki calculateAge gibi nesnelere hizmet eden kod bloklarıdır. fonksiyonlardan farkı bir nesneye bağlı olmalarıdır.

# #class tanımlamada class ismi büyük harfle başlar
# class Person:
#     #pass #pass keywordü boş bir class tanımlamak için kullanılır.
# #attributes

#     #class attributes #her zaman kullanmayacağımız özellikler class attribute olarak tanımlanabilir.(bizim için)
#     address = 'no information'

#     #constructor(yapıcı metod)
#     def __init__(self,name,year): #self parametresinin anlamı classtan türetmiş olduğumuz herhangi bir objeyi temsil etmesi (?) yani obje üzerine bir değer atmaak istediğimizde self'i kullanırız.
#         #object attributes # her zaman kullanacağımız bilgileri de object attribute(class içindeki olmazsa olmaz bilgiler) olarak tanımlarız.
#         self.name = name
#         self.year = year
#         print('init metodu çalıştır.') #__init__() missing 2 required positional arguments: 'name' and 'year'
        
#     #methods
#     def intro(self):
#         print("Hello there. I am " + self.name)
    
#     def calculate(self):
#         return 2022 - self.year

# #object(instance)
# p1 = Person(name = 'görkem',year = 1998)
# p2 = Person(name = 'göko', year = 1998)

# # updating 

# p1.name = 'ahmet' #görkem ahmet olarak değişti.
# p1.address = 'kocaeli' #no info bilgisi kocaeli olarak değişti.

# # print(p1)
# # print(p2) #farklı adreslere tanımlanmış iki obje (hata farklı)

# # print(type(p1))
# # print(type(p2)) #ikisi de person tipinde

# #accesing object attributes
# # print(f'name: {p1.name}, year: {p1.year}, address: {p1.address} ')
# # print(f'name: {p2.name}, year: {p2.year}, address: {p2.address} ') #YILDIZ # address stringinde p1 ve p2 yerine persond a yazabiliyoruz aslında ama selfin işlevi bu işte.

# p1.intro() #bu instance method olduğu için hata alırız o yüzden intro fonksiyonunun içine self yazmalıyız
# p2.intro()

# print(f'adım {p1.name} ve yaşım {p1.calculate()}.')
# print(f'adım {p2.name} ve yaşım {p2.calculate()}.') #metodda da fonksiyonda olduğu gibi return kullanırsak metod dışında print kullanmalıyız.


class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    #methods
    def cevreHesapla(self): #self parametresi classın içerisindeki bilgilere ulaşmak için kullanılır özetle.
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle () #yarıçap 1'e eşitlenecek
c2 = Circle (5)

print(f'c1: alan = {c1.alanHesapla()}, çevre = {c1.cevreHesapla()} ')
print(f'c2: alan = {c2.alanHesapla()}, çevre = {c2.cevreHesapla()} ')