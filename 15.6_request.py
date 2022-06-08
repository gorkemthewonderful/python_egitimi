#requests yüklü değildi pip install requests yazarak(alta) indirdik.

from cgitb import reset
import requests
import json

# print(dir(requests))

# result = requests.get("https://jsonplaceholder.typicode.com/todos")

# print(result) #<Response [200]> #bu başarılı olduğumuz anlamına gelir.
##########################################################################################
result = requests.get("https://jsonplaceholder.typicode.com/todos")
rextt = result.text

# print(rextt) #adres üzerinden gelen json bilgi yazdırıldı.
# print(type(rextt)) #<class 'str'>
# print(rextt[0]["title"]) #bu hata verir çünkü string bilgi üzerinden dictionary bilgi gibi bilgi alamayız.

jsongoko = json.loads(rextt)
print(jsongoko[0]["title"]) #delectus aut autem önce loads ile string bilgiyi dictionary e çevirdik ve ilk bilgideki title bilgisini yazdırdık.
print(jsongoko[0]) #şimdi de ilk bilgi olduğu gibi geldi.

# for i in jsongoko:
#     print (i) #bilgi daha düzenli bir şekilde yazıldı.
# for i in jsongoko:
#     print (i["title"]) #sadece latince sözler yazdı.
# print(type(i)) #<class 'dict'>

for i in jsongoko:
    if i["userId"] == 8:
        print(i["title"]) #sadece userId bilgisi 8 olan bilgilerin title kısmı yazdırıldı.

#requests modülü bir web sitesindeki bilgileri kullanmak istediğimizde ya da onları değiştirmek istediğmiizde kullanılabilecek şeker bir modüldür.
