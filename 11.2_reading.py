# file = open("newfile.txt")

# print(file) #<_io.TextIOWrapper name='newfile.txt' mode='r' encoding='cp1254'>(varsayılan mod r dir)

# try:
#     file2 = open("newfile3.txt","r")
#     print(file2)
# except FileNotFoundError:
#     print("Dosya bulunamadı.")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file = open("newfile.txt", "r", encoding= "utf-8")

# #for döngüsü

# for i in file:
#     print (i, end="\n") # normal for ile bir satır boşluk ekler. end = "\n" bunun olmamasını sağlar.

#read fonksiyonu

# content1 = file.read()

# print("içerik1")
# print(content1)

# content2 = file.read()

# print("içerik2")
# print(content2) #bunun sonucunda içerik2 yazısının altı boş kalır çünkü dosyada imleç en sona gelir ve dosya kapanmadığı için hiçbir şey okunmaz. ÖNEMLİ



# file = open("newfile.txt", "r", encoding= "utf-8") #imlecin başa dönmesini sağlamak için file içeriğini yeniden tanımlayabiliriz.

# content2 = file.read()

# print("içerik2")
# print(content2) şimdi yine okur yani file'ı bir daha tanımladığımız için.

# content = file.read(6) 
# print(content) #(Görkem) yani read komutunun sağına bir size yazarsak o size kadar içerik yazılır.

# content = file.read(5) #1.
# content = file.read(3) #3.

# print(content) # 2. #4.

#bu durumda print komutu ilk content komutundan sonra ilk kez yazıldığında ilk 5 karakter, sonra 2. content komutu yazıldıktan sonra print komutuyla sonraki 3 karakter yazdırılır. komutundan son imlein yeri sabit kalacağından metinin her seferinde farklı kısımları okutulur. ;)

#**********readline() fonksiyonu


# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")#readline fonksiyonu metindeki yalnızca bir satırın okunmasını sağlar. end="" ise boşluğu siler satırlar arasındaki.

#**********readlines() fonksiyonu

liste = file.readlines()
print(liste) #readlines her bir satır bilgiyi bir liste elemanına çevirir.

print(liste[0])
print(liste[2])
print(liste[1])
print(liste[3])

file.close() 


