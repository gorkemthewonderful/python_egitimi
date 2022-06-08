from selenium import webdriver
import time

hoko = webdriver.Chrome()

url = "http://github.com"

hoko.get(url) #tarayıcıda url içindeki site açılır
time.sleep(2) # 2 saniye bekler
hoko.maximize_window() # ve ekran büyütülür.
hoko.save_screenshot("github.com-homepage.png") # tarayıcıdan parantez içindeki isimde bir ekran görüntüsü alınır.(yeni dosyasında mevcut.)

url = "http://github.com/gorkemthewonderful" #url yeni sayfa olur

hoko.get(url) # tarayıcıda yeni bir sayfaya gider
print(hoko.title) #url deki title yazdırılır. #(gorkemthewonderful (Görkem Yılmaz) · GitHub)
if "gorkemthewonderful" in hoko.title:
    hoko.save_screenshot("gorkemthewonderful.png") # eğer title'da gorkemthewonderful stringi geçiyorsa ss alır(var.)
time.sleep(2) # 2 saniye bekler
hoko.back() # bi geri sayfaya gider abi
time.sleep(2) # 2 saniye bekler
hoko.close # ve tarayıcı kapanır.

