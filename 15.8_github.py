import requests
import json
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"

    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json() # burada neden loads kullanmadık (acaba böyle de oluyor mu loadsın yaptığı işlem?)
    
    def getRepository(self, username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()
    
    def createRepository(self,name): #bu fonksiyona kadar her fonksiyonda bilgi istemiştik ve dolayısıyla get metodunu kullanmıştık.ancak bu fonksiyonda bilgi göndereceğiz(repository YARATMAK) dolayısıyla bir token oluşturduk ve post metodu kullandık.
        response = requests.post(self.token + self.api_url + "/users/" + "/repos", json = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }) #ÖNEMLİ BURASI KOMPLE İPTAL ÇÜNKÜ BU FONKSİYONUN KULLANIMI TAMAMEN DEĞİŞMİŞ. BUNU YENİDEN ÖĞREN AMA BU FONKSİYON ŞU AN ÇALIŞMIYOR (İLGİLİ BAĞLANTILAR: https://developer.github.com/changes/2020-02-10-deprecating-auth-through-query-param/)

        return response.json()

#bu nesnede github sitesinde kullanıcı adını kullanarak çeşitli bilgilere eriştiğimiz url kodunu tanımladık ve username'i inputlayarak bu bilgilere erişebilmek adına bir fonksiyon yazdık.

github = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçiminiz: ")
    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Username: ") #username girme kısmı burası.
            result = github.getUser(username) #bilgileri result değişkeni içine aldığımız kısım (hepsini)
            print(f'Name: {result["name"]}\nPublic Repos: {result["public_repos"]}\nFollowers: {result["followers"]}') #istediğimiz spesifik bilgileri alıp yazdırdığımız kısım da burası
        elif secim == "2":
            username = input("Username: ")
            result = github.getRepository(username)
            for repo in result: #burada gelecek olan bilgi liste formatında olacağından for döngüsüne gideceğiz.
                print(repo['name']) #name kullandık çünkü repo isimleri name olarak gözüküyor linkte.
        elif secim == "3":
            name = input("Repository Name: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Yanlış bir seçim yaptınız.")

#ÖZETLE API KULLANIMINI ÖĞRENDİK. createRepository ÇALIŞMIYOR ÖÜNKÜ API KULLANIM BİÇİMİ DEĞİŞMİŞ BUNU ÖĞRENMELİYİZ.