#iterator yineleyici demek iterate den geliyor.
# liste = [1,2,3,4,5]

# for i in liste:
#     print(i) #buradaki liste bir iterable obje olduğu için for döngüsünü kullanabildik. yani aslında iteratorları çok kez kullandık şu ana kadar.

# print(dir(liste)) #burada __iter__ de var mesela 

# liste = [1,2,3,4,5]

# iterator = iter(liste)

# print(next(iterator)) #1
# print(next(iterator)) #2
# print(next(iterator)) #3
# print(next(iterator)) #4
# print(next(iterator)) #5
# # print(next(iterator)) #StopIteration

# for i in liste:
#     print(i)

liste = [1,2,3,4,5]

iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

for x in list:
    print(x)

# ????????????????????????????????????????????????????????????????????????????????????bunun anlamı ne şimdi?