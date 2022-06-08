html_info = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id = "header">
        Python Kurs
    </h1> 
<div class="= "grup1">
    <h2>
        Programlama
    </h2>

    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
</div>
<div class="= "grup2">
    <h2>
        Modüller
    </h2>

    <ul>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </ul>
    <img src="Cat03.jpg" alt="">
</div>
</body>
</html>
"""

from bs4 import BeautifulSoup #bu böyle importlanıyo başka şekilde zort

soup = BeautifulSoup(html_info, "html.parser") #burada parantez içine paramtere(markup) koyacağız (no shit) ama parametre yerine bir önceki derste yaptığımız iskelet html dosyasını koyacağız. html.parser ise koyduğumuz html bilgisini denetlemeye yarar ve bu şekilde kullanılır.

result = soup.prettify #prettify karmaşık halde olan html metnini düzeltir(güzelleştirir.) mesela tablar kaydıysa falan.

result = soup.title #.x yaparak html metni içerisindeki x leri yazdırabiliriz.
result = soup.head #.x yaparak html metni içerisindeki x leri yazdırabiliriz.
result = soup.body #.x yaparak html metni içerisindeki x leri yazdırabiliriz.

result = soup.title.name # .x.name yaparak html içerisindeki x lerin isimlerini alabiliriz.
result = soup.title.string #.x.string diyerek de html içerisindeki x lerin içerisindeki string bilgiyi alırız.
result = soup.h1 #h1 gelir içeriği
result = soup.h2 #h2 yazdığımızda mesela yalnızca ik h2 gelir(başka h2 olsa dahi) 
result = soup.h2.string

result = soup.find_all("h2") #üsttekinden farklı olarak tüm h2'leri almak istediğimizde .findall ("x") kullanırız.
result = soup.find_all("h2")[0] 
result = soup.find_all("h2")[1] 

result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1].ul
result = soup.find_all("div")[1].ul.li
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren() #2 etiket arasında daha solda kalan(tab yapılmamış) yani daha geneli, daha büyüğü kapsayan etiket parenttır. onun altındakiler ise childrendır. üst üste olan etiketler ise siblingdir
result = soup.div.find_next_sibling() #grup 2 divi gelir. yani sonraki divi istedik find_next_sibling metodu ile. o anda hangi konumdaysak next ile sornaki konuma geçebiliriz.

# find.get metodu da var linklerdeki href lere uşalmak falan için for ile kullanılabilir.

print(result)