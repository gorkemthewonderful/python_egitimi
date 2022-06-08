#selenium bir web otomasyon kütüphanesidir. web sitesini ziyaret edip etkileşimde bulunulabilir.

#selenium'un çalışması için bir web tarayıcı seçmeliyiz. buna seleniumda driver denir(chrome?)

#bize uygun driver'ı indirdikten sonra driver'ı Yeni klasörün(bu dosyaların olduğu klasör) içine attık (adı chromedriver.exe)

from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()

url = "http://google.com"

driver.get(url)

#selenium bir websitesi yaptığımızda onu test etmeye veya yaptığımız uygulamada bir web sitesini ziyaret etmeye yarayabilir.


