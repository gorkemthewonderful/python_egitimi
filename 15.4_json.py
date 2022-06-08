#cihazlar arasında ortak bir veri taşınmasına yarayan modül.

import json
from unittest import result
#dict

person = {"name": "Görkem", "languages": ["Python", "C#"]}

# result = person["name"]
#Görkem
# result = person["languages"]
#"Python", "C#"
# result = person["languages"][0]
#Python

print(result)
#json
# person = '{"name": "Görkem", "languages": ["Python", "C#"]}'

# result = person["name"]

# print(result)#Traceback (most recent call last):
# #File "C:\Users\gorke\OneDrive\Masaüstü\Yeni\15.4_json.py", line 19, in <module>
#     #result = person["name"]
# #TypeError: string indices must be integers
import json

#json string to Dict
person_string = '{"name": "Gorkem", "languages": ["Python", "C#"]}'
# result = json.loads(person_string) #burada json stringi dictionary'e çevirdik.#>>>
# print(type(result)) #>>> <class 'dict'>
# print(result) #>>>
#<module 'unittest.result' from 'C:\\Users\\gorke\\AppData\\Local\\Programs\\Python\\Python39\\lib\\unittest\\result.py'>
#{'name': 'Gorkem', 'languages': ['Python', 'C#']}

# result2 = json.loads(person_string)["name"] #json.loads(string ismi) şeklinde kullanılmalı hep.
# print(result2) #Gorkem

# with open("person.json") as f:
#     data = json.load(f) #bu da sanırım farklı bir dosyadaki bilgiyi alıyor. .load yani
#     print(data) #{'name': 'Gorkem', 'languages': ['Python', 'C#']}
#     print(data["name"]) #Gorkem

#dictionary to json string
person_dict = {
    "name": "Gorkem",
    "Languages": ["Python", "C#"]
}

# result = json.dumps(person_dict) #.dumps ise .loads ın tam tersi olarak dictionary bir ifadeyi stringe çevirir.
# print(result) #{"name": "Gorkem", "Languages": ["Python", "C#"]}
# print(type(result)) #<class 'str'>

# with open("person.json","w") as f:
#     json.dump(person_dict, f) 

# print(f) #burada person.json'un içini silmemize rağmen bilgiler yine yazıldı. dict olarak.

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)

print(result)