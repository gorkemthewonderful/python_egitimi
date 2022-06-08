#VARSAYILAN MODÜLLERİN İSMİ (MATH,RANDOM VB.) AYNI OLMAMALI. _ O YÜZDEN VAR

import random

# result = dir(random)
# result = help(random) #CTRL + C YAPIP ÇIKABİLİRSİN TERMINALDE/ENTERE BASARAK DA DEVAM EDEBİLİRSİN,
# result = random.random() * 100 #varsayılan olarak 0.0 veya 1.0 arasında bir sayı bulur ve bunu 100'le çarpar
# result = random.uniform(1,10) #bu metod ise aralığı açar sadece. başına int koyarsan da sayı tam sayı olur
# result = random.randint(1,100) #randint de integer sayı sallıyo işte
names = ["ali","ahmet", "ayşe", "fatma", "göko<3"]
# result = names[random.randint(0,len(names)-1)] #oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy # -1 dedik .ünkü names listesinin uzunluğu 4 ama listede 0,3 arası eleman var
# result = random.choice(names) #yukarıdakinin aynısı EFSANE BİŞEY
# liste = list(range(10))
# random.shuffle(liste) # shuffle metodu liste vb. deki elemanları karıştırır.
# result = liste
liste = list(range(100))
result = random.sample(liste,3) #sample metodu bir liste vb. deki elemanlardan rastgele y tane almamızı sağlar
result = random.sample(names,2) #aynısını yukarıdaki names listesi için yaptık.
print(result)
