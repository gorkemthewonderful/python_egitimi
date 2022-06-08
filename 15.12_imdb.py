from urllib import response
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/" #buradan tbody kısmını ayıracağız 250 film için

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# print(html)
# print(soup)

#ÖNCE FİLM İSİMLERİ ####################################################################
# result = soup.find("tbody", {"class": "lister-list"}).find_all("tr", limit= 1) #html içindeki class ismi "lister-list" olan İLK class'ın içindeki ismi tr olan İLK(limit =) metni aldık.
# print(result)

#DAHA FAZLA ELEMAN ALMACA ##############################################
# for tr in result:
#     title = tr.find("td", {"class":"titleColumn"}).find("a").text #result içerisinde (yukarıda) class ismi titleColumn olan tüm 'td' leri alıp a etiketinin içerisindeki text bilgisini for döngüsü ile alıyoruz.
#     print(title)

# result = soup.find("tbody", {"class": "lister-list"}).find_all("tr", limit= 10)

# for tr in result:
#     title = tr.find("td", {"class":"titleColumn"}).find("a").text #result içerisinde (yukarıda) class ismi titleColumn olan tüm 'td' leri alıp a etiketinin içerisindeki text bilgisini for döngüsü ile alıyoruz.
#     print(title)

#yukarıdakine ek olarak limiti 10 yaparak ilk 10 filmin title'ını aldık.

#FİLMLERİN YILLARINI ALMA ####################################################
# result = soup.find("tbody", {"class": "lister-list"}).find_all("tr", limit= 10)

# for tr in result:
#     title = tr.find("td", {"class":"titleColumn"}).find("a").text #result içerisinde (yukarıda) class ismi titleColumn olan tüm 'td' leri alıp a etiketinin içerisindeki text bilgisini for döngüsü ile alıyoruz.
#     yil = tr.find("td", {"class", "titleColumn"}).find("span").text.strip("()")
#     print(title,yil) #burada ise html'den yıl bilgilerini alıp strip metoduyla parantezleri silip film isimleri ve tarihlerini yazdırdık.

# SON OLARAK FİLMLERİN PUANLARINI ALARAK NİHAİ SONUÇ ####################################################
result = soup.find("tbody", {"class": "lister-list"}).find_all("tr")

for tr in result:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text #result içerisinde (yukarıda) class ismi titleColumn olan tüm 'td' leri alıp "a" etiketinin içerisindeki text bilgisini for döngüsü ile alıyoruz.
    yil = tr.find("td", {"class", "titleColumn"}).find("span").text #result içerisinde (yukarıda) class ismi titleColumn olan tüm 'td' leri alıp "span" etiketinin içerisindeki text bilgisini alıyoruz.
    score = tr.find("td", {"class", "ratingColumn"}).find("strong").text #result içerisinde (yukarıda) class ismi ratingColumn olan tüm 'td' leri alıp "strong" etiketinin içerisindeki text bilgisini alıyoruz.
    print(title, yil, score) 

#Imdb sitesindeki en iyi 250 film listesinden film isimleri, çıkış yılları ve puanları bilgilerini tek tek alarak yazdırdık özetle.
