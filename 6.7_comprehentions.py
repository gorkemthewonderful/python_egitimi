# for x in range(10):
#     print(x)

# numbers = [x for x in range(10)]
# print(numbers)

# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)

# for x in range(10):
#     print(x**2)

# numbers = [x**2 for x in range(10)]
# print(numbers)                #range(10) dan aldığımız her sayıyı x içerisine alıyoruz ve bu sayılar üzerinde işlem yapmak için de x'i tekrar kullanıyoruz.

# numbers = [x**2 for x in range(10) if x % 3 == 0 ]
# print(numbers)

# goko = "Hello"
# string = []

# for x in goko:
#     string.append(x)
# print(string)  ===========>

# string = [x for x in goko]
# print(string)

# years = [1998, 1996, 1970, 1963]

# age = [2022 - year for year in years]
# print(age)

# results = [x if x%2 == 0 else "TEK" for x in range(10)]
# print(results)                   # for'dan sonra gelen diziye for'dan önce istediğimiz işlemi yaptırabiliriz.

# result = []
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)              =====================>

# result = [(x,y) for x in range(3) for y in range(3)]
# print(result)