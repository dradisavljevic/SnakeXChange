import requests
import iso4217
import auth

response = requests.get('https://openexchangerates.org/api/latest.json?app_id='+auth.API_KEY)
# print(response.json()["rates"])

for test, rate in response.json()["rates"].items():
    try:
        print(iso4217.currencies[test])
    except KeyError:
        print('NEMA GA JBG')
