file = open("newfile3.txt","r",encoding= "utf-8")
content = file.read()
print(content)
file.close()

with open("newfile3.txt","r",encoding= "utf-8") as file:
     content = file.read()
     print(content) # with komutu ile close komutuna gerek kalmaz. dosya otomatik olarak kapanır. kodun yaşam süresi kod bloğu bitene akdardır çünkü
     file.seek(10) #seek komutu ile okume esnasında cursoru hangi birime götürmek istediğimizi belirleyebiliriz.
     print(file.tell()) #tell komutu bize okuma esnasında cursorun kaçıncı birimde olduğunu yazar.
     content2 = file.read()
     print(content2) #burada boşluk yazar çünkü content ile file dosyasını tamamen okuduk ve 45. birime geldik(tell)
