# def square(number): return number ** 2

# numbers = [1,3,4,9]

# result = list(map(square,numbers))# ya liste metoduyla ya da for kullanarak (result) içerisine atılmalı

# print(result) #map metodu dizi içerisindeki her bir elemanı bir fonksiyon üzerinden geçirebilir.

# for item in map(square,numbers):
#     print(item) #for kullandık

# numbers = [1,3,5,7,9]

# result = (list(map(lambda num: num ** 2, numbers)))

# print(result) # lambda expression, isimsiz bir fonksiyon tanımlamamızı sağlar.

# square = lambda num : num ** 2

# numbers = [1,3,5,7,9]

# result = (list(map(square,numbers)))

# print(result) #aynı sonuç

# numbers = [1,3,5,7,9,10,12,4]

# # def checkEven(num): return num%2 == 0 

# # result = list(filter(checkEven,numbers))

# # print(result) #filter metodu bir dizideki elemanları belirtilen işlemden geçirip true sonucunu verenleri yazdırır.

# result = (list(filter(lambda num : num%2 == 0,numbers)))

# print(result) #üstteki işlemin lambdalısı YILDIZ