
from selenium import webdriver
from selenium.webdriver.common.keys import Keys         #space,enter gibi tuşları almamızı sağlayan modül
import time

driver = webdriver.Chrome() #tarayıcıyı tanımaldık

url = "http://github.com" #urlyi tanımladık
driver.get(url) #driver ile urlyi birleştirdik

# driver.maximize_window() #ekranı büyüttük
# seacrhInput = driver.find_element_by_name("q") #q adındaki elementi tanımladık(a burada arama çubuğu)
# time.sleep(1)
#alternatif(üst satır(11)dekine...)
driver.maximize_window() #ekranı büyüttük
seacrhInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]") #burada ise incele menüsünden(tarayıcıda) sağ tıklayıp copy ve copy xcode seçeneğini seçerek kopyaladığımız kaynak dizinini paranteze koyarak aynı kutucuğa gidebildik. alternatif yol yani
time.sleep(1)
seacrhInput.send_keys("python") # arama çubuğuna python yazmasını söyledik(find keys buna yarıyor diye yorumladım.)
time.sleep(1)
seacrhInput.send_keys(Keys.ENTER) #Keys modülü böyle kullanılır. # sayfada ENTERe bastı (otomatik ve arama yaptı.)
time.sleep(3)
result = driver.page_source #üstteki aşamalardan sonra geldiğimiz sayfanın kaynak kodunu aldık...
print(result) #... ve yazdırdık. bu kodu alarak soup modülüyle işlemler yapabiliriz.

# result = driver.find_elements_by_css_selector(".repo-list-item h3 a")

# for element in result:
#     print(element.text) #burası çalışmadı neden acaba

driver.close()

#16. satırda yaptığımız işlem önemli. istediğimizi urldeki html kodundan sitedeki istediğimiz spesifik bir yerin kaynak kodunu kolayca alıp işlem yapabiliriz.##########