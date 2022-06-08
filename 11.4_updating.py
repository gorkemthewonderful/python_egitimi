# with open("newfile3.txt","r+",encoding="utf-8")as file: #r+ hem okumayı hem yazmayı sağlar.
#     print(file.read())

# with open("newfile3.txt","r+",encoding="utf-8")as file: 
#     file.write("deneme")

# with open("newfile3.txt","r+",encoding="utf-8")as file: #r+ hem okumayı hem yazmayı sağlar.
#     print(file.read())

#deneme7890abcdefgğhıijklmnoöpresştuüvywz r+ yerine write deseydik (w) sadece deneme yazardı. ama r+ dediğimiz için 0. karakterden başlayarak deneme yazdı.

# with open("newfile3.txt","r+",encoding="utf-8")as file: 
#     file.seek(20)
#     file.write("deneme")

# with open("newfile3.txt","r+",encoding="utf-8")as file: #r+ hem okumayı hem yazmayı sağlar.
#     print(file.read()) #01234567890abcdefgğdenemelmnoöpresştuüvywz böyle de 20. elemandan itibaren deneme yazdı.

#******** Sayfa sonunda güncelleme**************
# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("siüüüüüüüüüüüüüüüü") #a (append) cursoru sayfanın sonuna getirir. dolayısıyla write yanına yazdığımız şey sayfanın sonuna eklenir. mevcut yazan şeyler yerine gelmez.
# with open("newfile.txt","r",encoding="utf-8")as file:
#     print(file.read()) 

#******** Sayfa başında güncelleme**************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Gökoş\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)w

#******** Sayfa ortasında güncelleme**************


# with open("newfile.txt","r+",encoding="utf-8")as file: 
#     list = file.readlines()
#     list.insert(3, "Gökomuz")
#     file.seek(0)
#     file.writelines(list)
    
# with open("newfile.txt","r",encoding="utf-8")as file:
#     print(file.read()) 