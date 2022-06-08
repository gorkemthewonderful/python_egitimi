import requests
from bs4 import BeautifulSoup

link = "https://www.n11.com/bilgisayar"
html = requests.get(link).content
soup = BeautifulSoup(html,"html.parser")

product = soup.find("div",{"id":"view"}).find_all("h3",{"class": "productName"})
price = soup.find("li",{"class":"column"}).find("div", {"class":"proDetail"}).find("a")

for res in product,price:
    urun = res.text.strip().strip("REKLAM")
    fiyat = res
    print(urun,fiyat)

#####################################################################################
 ################### ZORT######################
