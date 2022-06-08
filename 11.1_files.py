#Dosya açmak için open() metodu kullanılır. Kullanımı > open(Dosya_adi, dosya_erisme_modu)
#dosya_erisme_modu dosyayı ne amaçla açtığımızı belirtir.

#"w" > (write) yazma modu.Dosyayı konumda oluşturur 

# file = open("newfile.txt","w") 
# file.close() #dosyayı kapatmak için

# file = open("C:/Users/gorke/OneDrive/Masaüstü/goko.txt","w")
# print(file) #<_io.TextIOWrapper name='C:/Users/gorke/OneDrive/Masaüstü/goko.txt' mode='w' encoding='cp1254'>

# file = open("newfile.txt","w",encoding= "utf-8") #encoding utf 8 türkçe karakterler o ü birçok karakteri görünür yapar.
# # file.write("selam ben göko") # bu kısmı yorum satırı yapıp çalıştırdığımızda bütün veriler gider. çünküwrit komutu farklı giriyle bir daha kullanıldığında dosyadaki mevcut giriler silinir.
# file.close()

#"a" > (append) ekleme. Dosya konumda yoksa oluşturur. (write ile farkı write dosyanın üstüne veriyi yazarken append veriyi mevcut dosyanın üstüne ekler.)

# file = open("newfile.txt","a",encoding= "utf-8")
# file.write("Görkem Yılmaz\n") #bu kodu tekrar tekrar çalıştırdığımızda write'ın aksine üstüne yazmaz bilgiyi. tekrar tekrar yazar. cursor varolan bilginin başında değil, sonunda yazmaya devam eder.
# file.close()

#\metnin başına \n(newline) yazmak ise bilginin alt satıra yazılmasını sağlar. sonuna yazmak ise metnin bir kereliğine mahsus alt satırdan birleşik olarak yazılmasını sağlar

#"x" > (Create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt","x",encoding= "utf-8")#w ile aynı bok aslında gereksiz.

#"r" > (Read) okuma. varsayılan. dosya konumda yoksa hata verir.



# print(file) > <_io.TextIOWrapper name='newfile.txt' mode='w' encoding='cp1254'> buradaki encoding kısmı bizim işletim sistemimizde bu dosyanın hangi konumda olduğunu ifade ediyor.
# bu işlemi bir değişken içine atayarak bu dosya üzerinde işlemler yapabiliriz.(file)


open("15.3_re.py","w")
open("python")