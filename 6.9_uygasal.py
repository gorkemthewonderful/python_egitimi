# Girilen bir sayı asal sayı mıdır? Uygulaması...

x = int(input("Asal sayı olup olmadığını sorgulamak istediğiniz sayı kaçtır?: " ))
asalmi = True

if x == 1:
    asalmi = False

for i in range(2, x):
    if (x % i == 0):
        asalmi = False
        break
if asalmi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")



