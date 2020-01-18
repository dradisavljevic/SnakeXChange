import requests
import auth
from currency import Currency, getCurrencyList, getSpecificCurrency

def report(baseCurrency, amount, regionCode, worldwide, date, currencyList):
        response = requests.get("https://openexchangerates.org/api/" + date + ".json?app_id="+auth.API_KEY)

        base = getSpecificCurrency(response, baseCurrency)
        if base is None:
            raise ValueError("Base currency with that code does not exist for desired date.")

        if currencyList is None:
            completeList = getCurrencyList(response, regionCode, worldwide)
            completeList.sort(key=lambda x: x.name)
            print("Exchange rates for " + str(amount) + " " + base.name + " are as follows:")
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")
            for curr in completeList:
                if (curr.code == base.code):
                    continue
                print(str(amount) + " " + base.code + " is worth " + str(curr.getExchangeRate(base.exchangeRateToUSD, amount)) + " " + curr.name + " (" + curr.code + ")")
                print("-----------------------------------------------------------------------------")
        else:
            for currency in currencyList:
                exchangeCurrency = getSpecificCurrency(response, currency.strip())
                if exchangeCurrency is None:
                    raise ValueError("Exchange currency with that code does not exist for desired date.")
                print("-----------------------------------------------------------------------------")
                print(str(amount) + " " + base.name + " is worth " + str(exchangeCurrency.getExchangeRate(base.exchangeRateToUSD, amount)) + " " + exchangeCurrency.name + " (" + exchangeCurrency.code + ")")
                print("-----------------------------------------------------------------------------")
