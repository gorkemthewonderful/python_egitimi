def not_hesapla(satir):
    satir = satir [:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 80 < ortalama <= 100:
        harf = "AA"
    elif 60 < ortalama <= 80:
        harf = "BB"
    elif 40 < ortalama <= 60:
        harf = "CC"
    elif 20 < ortalama <= 40:
        harf = "DD"
    elif 0 < ortalama <= 20:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    not1 = input("1. Not: ")
    not2 = input("2. Not: ")
    not3 = input("3. Not: ")

    with open("sinav_notlari.txt", "a", encoding= "utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1+"," + not2 + "," + not3 + "\n")

def notlari_kaydet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == 3:
        notlari_kaydet()
    else:
        break

# BU UYGULAMADA NOTLARI KAYDETME (notlari_kaydet()) FONSKİYONU ÇALIŞMADI. BUNUN SEBEBİNİ ÖĞREN!!!!!!
