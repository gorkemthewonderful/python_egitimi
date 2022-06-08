# mylist = [1,2,3]
# myString = "my string"

# print(len(myString))
# print(type(myString))
# print(len(mylist))
# print(type(mylist))

# class movie():
#     pass

# m = movie()
# print(type(m))

# print(len(m)) #class'ın uzunluğu (length) yok

# myList = [1, 2, 3]

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self): #YAZDIRMAK İÇİN METOD BU ÖNEMLİ BABACIM # AYRICA BURAYI YAZMASAYDIK <__main__.Movie object at 0x000001967FB1FFD0> YAZIYORDU 
        return f"{self.director} tarafından yönetilen {self.title} adlı film {self.duration} dakikadır. "

    def __len__(self):
        return self.duration #ÖNEMLİ BU SELF OLAYINI KAVRA

    def __del__(self):
        print("film objesi silindi")

m = Movie("Dark Knight", "Cristopher Nolan", 130) 
# print(myList)
print(m)
print(len(m))
del m
print(m)
##NameError: name 'm' is not defined hatası verir çünkü del metodu ile m objesini sildik abi

