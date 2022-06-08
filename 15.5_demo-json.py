import json
import os
#os'yi import ettik çünkü loadtofile dosya yükleme esnasında users.jsonda bilgi olmazsa dosya yükleyemez. users.json'da bilgi olup olmadığını anlamak için de os modülünü kullanacağız

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = [] # bir kullanıcı veritabanı oluşması için boş bir liste oluşturduk.
        self.isLoggedin = False #kullanıcının kullanıcı adını ve şifresini sorması için buraya false olarak varsayıyoruz
        self.currentUser = {} #logged in olmuşsa logged in durumunda kullanıcınını bilgilerini kullanmak için bu dicti oluşturduk.

        #load users from .json file
        self.loadUsers() #burada dosya okuma işlemi yapacağız. bilgiyi ise tepedeki self.users'dan alacak.
    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding= "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user["username"], password = user["password"], email = user["email"])
                    self.users.append(newUser)
            print(self.users)        
    def register(self, user: User):
        self.users.append(user)
        self.saveToFile() #bunu çağırmamızın sebebi kaydedilen tüm kullanıcı bilgilerinin bu dosyaya kaydedilmesi.
        print("Kullanıcı oluşturuldu.")
    def login(self, username, password):
       for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedin = True
                self.currentUser = user
                print("Giriş yapıldı.")
                break
    def logout(self):
        self.isLoggedin = False
        self.currentUser = {}
        print("Çıkış yapıldı.")
    def identity(self):
        if self.isLoggedin:
            print(f'username: {self.currentUser.username}')
        else:
            print("Giriş yapılmadı.")
    def saveToFile(self):
        list = [] #

        for user in self.users:
            list.append(json.dumps(user.__dict__)) #__dict__ metodu burada user yapısını komple dicte çeviriyor.
        with open("users.json","w") as file: #w yazdık çünkü zaten bilgiler users klasörüne gidecek (?)
            json.dump(list, file) #dosyayla çalışacağımız için dumps değil dump kullandık. ama burada bize hata verecek çünkü json modülü classı desteklemiyor. 

repository = UserRepository() #döngü (while True) dışına yazdık.

while True:
    print("Menü" .center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            #register
            username = input("Kullanıcı Adı: ")
            password = input("Şifre: ")
            email = input("E-Mail: ")

            user = User(username = username,password = password ,email = email)
            repository.register(user) 
        elif secim == "2":
            #login
            if repository.isLoggedin:
                print("Zaten giriş yapılmış.")
            else:
                username = input("Username: ")
                password = input("Password: ")

            repository.login(username,password)
        elif secim == "3":
            #logout
            repository.logout()
        elif secim == "4":
            #identity
            repository.identity()
        else:
            print("Yanlış seçim.")
