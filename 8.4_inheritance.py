# # Inheritance = Kalıtım (miras alma)

# Person => name, surname, age, eat(), run(), drink()

# student(Person), teacher(Person) (PERSON İÇERİSİNDEKİ ATTRIBUTE(ÖZELLİK)LER STUDENT VE TEACHERIN DA İÇİNDE OLACAK YANİ TEACHER VE STUDENT İÇİN YİEN AYNI ÖZELLİKLERİ OLUŞTURMAYA GEREK KALMAYACAK

# PERSON BURADA TEMEL SINIF. YANİ STUDENT VE TEACHERDAKİ ÖZELLİKLER PERSONA GİTMEYECEK.

# Animal => Dog(Animal), Cat(Animal)

# class person():
#     def __init__(self):
#         print("Person Created")

# class Student(person):
#     pass

# p1 = person()
# p2 = Student() #STUDENT DA PERSONDAN MİRAS ALDIĞI İÇİN YİNE PERSON CREATED YAZDIRACAK. ÇÜNKÜ STUDENT FONKSİYONUNUN İÇİ BOŞ

class person():
    def __init__(self):
        print("Person Created")

class Student(person):
    def __init__(self):
        person.__init__(self) #student classının içine farklı bir metod yazıp ayrıca yine de miras alsın istiyorsak bunu yazarız
        print("Student Created") #bu sefer student classının içi dolu olduğundan burada miras alınmaz 

p1 = person()
p2 = Student()

class person():
    def __init__(self,fname,lname): # person classının içine farklı değişkenler ekledik...
        self.firstName = fname
        self.lastName = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a Person")

class Student(person):
    def __init__(self,fname,lname):
        person.__init__(self, fname, lname) # ...ve student, bu değişkenleri aldı, değişkenleri tek tek tanımlamamız gerekmedi (mirasın özelliği gereği)
        print("Student Created")
    
    #override (aynı isimli bir metod temel sınıftaki metodu ezer. buna overriding denir. )
    def who_am_i(self):
        print("I am a Student")

class Teacher(person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")

p1 = person("Görkem", "Yılmaz")
p2 = Student("Göko", "Yılmaz")
t1 = Teacher("Süpergöko", "Çüklo", "Math") # FARKLI BİR CLASS TANIMLAYIP ORAYA BRANCH DİYE FARKLI BİR METOD DA TANIMLADIK.

print(p1.firstName + " " + p1.lastName)
print(p2.firstName + " " + p2.lastName)

p1.who_am_i()
p2.who_am_i() #p2 student classını çağırmasına rağmen burası yine de çalıştı.çünkü kalıtım ehe
t1.who_am_i()