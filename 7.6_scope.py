# #global scope
# x = 'global x'

# def function():
#     #local scope
#     x = 'local x'  #fonksiyon içerisinde olan değişkenler dışarıyı etkilemiyor.

# function()
# print(x) #scope(kapsam) fonksiyonu ayrı dışarıdaki değeri ayrı alır. yani bu örnekte dışarıdaki x değeri ile içerideki x değeri ayrıdır.

# x = "görkem"

# def nameBaba (name):
#     x = name
#     print(name)

# nameBaba("gökorello")
# print(x)

#İÇ İÇE OLAN FONKSİYONLAR İÇİN GLOBAL FONKSİYON BİR ÜSTTEKİ FONKSİYONDUR.
# name = 'Görkem Yılmaz'

# def greeting():
#     name = "Görkem"
    
#     def hello():
#         name = "göko"
#         print("hello " + name)

#     hello()

# greeting() # fonksiyon olabildiğince içerideki değişkeni kabul eder. yani göko olmasa Görkem'i, Görkem olmasa Görkem Yılmaz'ı alır name olarak.

# x = 50

# def test(x):
#     print(f'x : {x}')
    
#     x = 100

#     print(f'x changed to {x}')

# test(x)
# print(x) #fonksiyon ilk başta dışarıdaki 50'yi aldı ve fonksiyon içerisindeki x değişimini aldı ve x 100 oldu. ancak fonksiyon dışında x global olarak hep 50 kaldı.

# x = 50 

# def test():
#     global x #fonksiyon içerisindeki bir parametrenin global olarak tanımlanması için global keyword'ü kullanılır.

#     print(f'x : {x}')
    
#     x = 100

#     print(f'x changed to {x}')

# test()
# print(x)
