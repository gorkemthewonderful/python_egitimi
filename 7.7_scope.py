from unicodedata import name


gorkemHesap = {
    "ad": "Görkem Yılmaz",
    "hesap no": "123654789",
    "bakiye": 3000,
    "ekHesap": 2000,
}

gokoHesap = {

    "ad": "Göko Yılmaz",
    "hesap no": "123456789",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(gorkemHesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesabınız kullanılsın mı? (e/h)")
            
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(gorkemHesap)
            else:
                print(f'{hesap["hesap no"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır.')

        else:
            print("Hesabınızda yeterli bakiye bulunmamaktadır.")
            bakiyeSorgula(gorkemHesap)


# BURADA DİKKAT EDİLMESİ GEREKEN ŞEY OBJELERİN(REFERANS) İÇİNDEKİ BİLGİLER BİR FONKSİYONUN İÇİNDE DEĞİŞİME UĞRADIĞI ZAMAN KALICI OLARAK DEĞİŞİR. ANCAK BİZ BU DEĞİŞKENLERİ (BAKİYE,HESAP NO VB.) REFERANS TÜRÜNDE DEĞİL DE NORMAL OLARAK DIŞARIDA TANIMLASAYDIK FONKSİYON İÇİNDEKİ DEĞİŞİMLER KALICI OLMAYACAKTI.

def bakiyeSorgula(hesap):
    print(f'{hesap["hesap no"]} nolu hesabınızda {hesap["bakiye"]} TL vardır. Ek hesap limitiniz ise {hesap["ekHesap"]} TLdir.')

paraCek(gorkemHesap,4500)

