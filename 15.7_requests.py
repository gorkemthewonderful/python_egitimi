import requests
import json

url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=USD&amount=5"

payload = {}
headers= {
  "apikey": "GAahCHFC6YeFQhCbFALrYeB7yJOBsQLp"
}

response = requests.request("GET", url, headers=headers, data = payload)

result = response.text

buyukoran = json.loads(result)["info"]["rate"]
#######################################################################
url2 = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=TRY&amount=5"

payload = {}
headers= {
  "apikey": "GAahCHFC6YeFQhCbFALrYeB7yJOBsQLp"
}

response2 = requests.request("GET", url2, headers=headers, data = payload)

result2 = response2.text

kucukoran = (json.loads(result2)["info"]["rate"])


def usdToTry(buyukoran):
    dolar = int(input("TL'ye çevirmek istediğiniz Amerikan Doları miktarını giriniz: "))
    print(f"{dolar} USD, {dolar * buyukoran} TL'ye eşit.")

def tryToUsd(kucukoran):
    tl = int(input("Amerikan Doları'na çevirmek istediğiniz TL miktarını giriniz: "))
    print(f"{tl} TL, {(tl * kucukoran)} USD'ye eşit.")

while True:
    print("Menü" .center (30,"-"))
    secim = input("1-USD/TL\n2-TL/USD\n3-Çıkış\nSeçiminiz: ")
    if secim == "3":
        break
    else:
        if secim == "1":
            usdToTry(buyukoran)
            break
        elif secim == "2":
            tryToUsd(kucukoran)
            break







