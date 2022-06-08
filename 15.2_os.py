import os
import datetime
# print(dir(os)) #işletim sistemi ile ilgili bir çok işlemi yapmamızı sağlar.

# print(os.name) #nt windows işletim sistemi demek

#etkin dizin öğrenme
# print(os.getcwd()) #mevcut dosyanın konumunu bildirir.

# os.mkdir("newdirectory") #mevcut dosyada yeni bir dosya açar.

#dizin değiştirme
# os.chdir("..") #bu bir üst dosyaya geçmemizi sağlar.
# os.chdir("../..") #bu da iki üst dosyaya geçmemizi sağlar.

# os.chdir("C:\\")
#klasör oluşturma
# os.mkdir("newgoko") #chdir(change direction) mkdir ile oluşturacağımız dosyanın yerini belirlememizi sağlar.

#iç içe klasörler oluşturma.
# os.makedirs("newdirectory/klasörööörör")

#listeleme
# print(os.listdir()) #mevcut dizin içindeki klasör/dosyaları listeler.
# print(os.listdir("C:\\")) #parantez içindeki dizin içindeki klasör/dosyaları listeler.

# for dosya in os.listdir():
#     print (dosya) #same shit.

# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya) #sadece py uzantılı dosyaları listeledik.

#dosya hakkında bilgi alma
# print(os.stat("newfile.txt")) #dosyanın büyüklüğü, son erişilme zamanı, oluşturulma zamanı vb. gibi bilgiler.

# print(os.stat("newfile.txt").st_size) #sadece dosyanın büyüklüğü (bit cinsinden)
# print(os.stat("newfile.txt").st_ctime) 
# print(datetime.datetime.fromtimestamp(os.stat("newfile.txt").st_ctime)) #dosyanın oluşturulduğu spesifik tarih fromtimestamp aracılığıyla yazdırıldı. :O #create
# print(datetime.datetime.fromtimestamp(os.stat("newfile.txt").st_atime)) #dosyaya son erişilen spesifik tarih fromtimestamp aracılığıyla yazdırıldı. :O #access
# print(datetime.datetime.fromtimestamp(os.stat("newfile.txt").st_mtime)) #dosyanın son değiştiği spesifik tarih fromtimestamp aracılığıyla yazdırıldı. :O #modify

#çalıştırma

# os.system("6.8_uygtahmin.py") #parantez içine yazdığımız program çalışıyor abi :D
# os.system("notepad") not defteri çalıştı 

#dosya ismi değiştirme
# os.rename("newfilegoko.txt", "newfile.txt")
# os.rename("newfile.txt", "newfilegoko.txt") #soldakinin ismi sağdaki oldu ehe :D
# os.rename("newfilegoko.txt", "newfile.txt")

#dosya silme
# os.remove("silinecekklasör.txt")#rmdir de olur ... (alt dizinleri varsa rmdirs yaz)

#path(dosyanın uzantısıyla ilgili işlemler)
# print(os.path.abspath("15.2_os.py")) #dosyanın tam konumunu verir(bu daha iyiymiş üsttekini siktir et)
# print(os.path.dirname("C:/Users/gorke/OneDrive/Masaüstü/Yeni/15.2_os.py")) #bu da aynısı yani amelelik baya :( #dizin ismiymiş bu yani yukarıdakine göre dosyanın ismi yok bunda #bunu kullanırken slahsları ters yapmak önemli
# print(os.path.dirname(os.path.abspath("15.2_os.py"))) #doyanın yolunu değil, sadece ismini biliyorsak bu kodu yazabiliriz de ne gerek var üssteki daha iyi yani
# print(os.path.exists("15.2_os.py")) #bool şekilde nesnenin orada olup olmadığnıı sorar (True/False) başka bir konumdaki dosyanın oradaki varlığını sorgulamak istediğimizde de dizin(yol) kullanabiliriz. bir dosyanın yerine geçip silmemesini istediğmiiz başka bir dosyanın varlığı takdirinde kullanılabilir.
# print(os.path.isdir("C:/Users/gorke/OneDrive/Masaüstü/Yeni")) #isdir yine bool olarak bir dizinin sonundaki dosyanın bir klasör olup olmadığını sorgular.
# print(os.path.isfile("C:/Users/gorke/OneDrive/Masaüstü/Yeni/15.2_os.py")) #isfile ise isdirin dosya versiyonu yani klasör ise false.
#join ve split metodları da bir dizin oluşturmaya ve bölmeye yarar(sanırım?)
#splitext de bir dosya veya klasörün ismiyle uzantısını bölüp liste biçimine çevirir.

print(os.path())