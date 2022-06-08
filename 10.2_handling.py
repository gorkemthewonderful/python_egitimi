#error handling


# try:   #try metodu hata gelebilecek kod blokları için kullanılır.
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError: #except (dışında) hata bilgisi yanına yazılarak o hata bilgisi geldiğinde uygulama durması yerine seçilen işlem yapılır.
#     print("y için 0 girilemez")
# except ValueError: #istenilirse bir exceptin yanına error türlerini virgülle ayırarak tek bir işlem yapılması sağlanabilir.
#     print("Sayı yerlerine harf veya işaret konulamaz.")

# except (ZeroDivisionError,ValueError) as hata1: #hatalar da as komutu ile isimlendirilebilir
#     print("yanlış değer girilemez")
#     print(hata1)

# except: #exceptin tüm hatalar için tek bir işlem yapmasını istiyorsak yanı boş bırakılabilir.ç
#     print("yanlış değer girilemez")




# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except: 
#     print("yanlış değer girilemez")
# else: #else ile (bu kodda herhangi bir hatanın olmadığı bir durum) except'teki durum haricinde yapılacak bir işlem seçilebilir.
#     print("Her şey yolunda.")


# while True:
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x/y)
#     except: 
#         print("yanlış değer girilemez")
#     else:
#         break # bu şekilde bir kod yazıldığında bu işlem hatasız olana kadar kod bize x ve y sayılarını sormaya devam eder. x ve y yi hatasız yazdığımızda ise break komutu devreye girer ve kod bize x ve y yi sormayı keser.

#Exception sınıfı bir ana sınıftır ve hataları kapsar. hataların topuna isim koymak istediğimizde (except Exception as ...) diyerek hataya ... ismini verebiliriz yani




while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except: 
        print("yanlış değer girilemez")
    else:
        break
    finally: #finally komutu gerek try gerek except gerek else kullanılsın her türlü çalıştırılır.
        print("Try except sonlandı.")