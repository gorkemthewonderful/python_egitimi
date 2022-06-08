#generators bellekte yer tutmayan iteratorlardır :D

# def cube():
#     result = []
#     for i in range(5):
#         result.append(i**3)
#     return result
# print(cube()) #yukarıdaki lsite şu an bellekte yer tutuyor. kullandığımız değerler küçük olunca problem olmasa da büyük verilerle işlem yaptığımızda bu sıkıntı yaratabilir. generatorlar bu yüzden var.
######################################################################
# def cube():
#     for i in range(5):
#         yield i ** 3 #yield burada değer gönderir ve du değer bir yerde saklanmaz.

# print(cube())
######################################################################
from email import generator, iterators


# def cube():
#     for i in range(5):
#         yield i ** 3 

# kupler = cube()
# print(kupler) #burada bize veri yollamaz. iter yoluyla iterate edebileceğimiz bir nesne yollar. ama içeride yield değil de return kullansaydık veriler yazılırdı.

# generator = cube()

# iterator = iter(generator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) #burada olduğu gibi iter yoluyla iterate edebiliyoruz.


# def cube():
#     for i in range(500000):
#         yield i ** 3 

# iterator = cube()

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) #generate edilmiş bir fonksiyon iterable olduğu için iter fonksiyonuna da gerek yokmuş :D

# def cube():
#     for i in range(5):
#         yield i ** 3 

# for i in cube():
#     print (i)

#oluşturduğumuz değer bir liste vb. içinde saklamamız gerekmiyorsa, o listeyi sadece o an kullanacaksaki başka bir zaman kullanmamız gerekmeyecekse generatorları kullanabiliriz.

# liste = [i**3 for i in range(5)] #python comprehension
# print(liste) #[0, 1, 8, 27, 64]

# liste = (i**3 for i in range(5)) #bir comprehension'u generatora dönüştürmek istiyorsak KÖŞELİ PARANTEZ YERİNE NORMAL PARANTEZ KULLANIRIZ.
# print(liste) #<generator object <genexpr> at 0x00000264576057B0>

# print(next(liste))
# print(next(liste))
# print(next(liste))
# print(next(liste))
# print(next(liste)) #0 1 8 27 64

# for i in liste:
#     print(i) #0 1 8 27 64


