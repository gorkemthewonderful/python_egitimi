# def greeting(name):
#     print("Hello", name)

# print(greeting("Görkem"))
# print(greeting)

# sayHello = greeting

# print(sayHello)
# print(greeting)

#<function greeting at 0x0000017D8B86DF70>
#<function greeting at 0x0000017D8B86DF70>
# sayHello = greeting

# print(sayHello("Görkem"))
# print(greeting("Görkem"))

# Hello Görkem
# None
# Hello Görkem
# None

# sayHello = greeting

# del sayHello #sayHelloyu değil, tanımlamayı siliyoruz(bellekte hala yer kaplıyor).
# print(sayHello) #NameError: name 'sayHello' is not defined
# print(greeting) #<function greeting at 0x000001B759A5DF70>
#encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner") #outer (inner yok)
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2) 

# outer(10) #biz dıştaki fonksiyonu (outer) yazarsak sadece dıştaki fonksiyon çalışır (outer)

# num2 = inner_increment(num1)
#     print(num1,num2) #bu kısmı yazdıktan sonra...
#outer(10)... bu komutu yazdığımızda...

# outer
# inner
# 10 11 ...bu kısım yazılır.

# inner_increment(10) #NameError: name 'inner_increment' is not defined #YANİ bu fonksiyon outer fonksiyonu hariç herhangi bir yerde tanımlanamaz çünkü outer fonksiyonu içinde tanımlanan farklı bir fonksiyondur.!!!

# def factorial(number):
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)

# print(factorial(8))

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number > 0:
        raise ValueError("number must be positive or zero")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)

# print(factorial(-5)) ValueError: number must be positive or zero
# print(factorial("4")) TypeError: number must be an integer

# try:
#     print(factorial("4"))
# except Exception as ex:
#     print(ex) #number must be an integer
