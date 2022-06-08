import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=USD&amount=5"

payload = {}
headers= {
  "apikey": "GAahCHFC6YeFQhCbFALrYeB7yJOBsQLp"
}

response = requests.request("GET", url, headers=headers, data = payload)


result = response.text
print(result)