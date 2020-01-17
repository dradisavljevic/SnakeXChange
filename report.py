import requests
import auth
from currency import Currency, getCurrencyList

def report(baseCurrency, regionCode, region, worldwide, date, currency):
        response = requests.get("https://openexchangerates.org/api/" + date + ".json?app_id="+auth.API_KEY)
        # print(response.json()["rates"])

        completeList = getCurrencyList(response, regionCode, worldwide)
        for curr in completeList:
            print(curr.name)
            #if (curr.code == baseCurrency):
            #    print(curr.getExchangeRate(0.90))
