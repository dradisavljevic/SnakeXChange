import requests
import auth
from currency import Currency, getCurrencyList, getSpecificCurrency

def report(baseCurrency, amount, regionCode, worldwide, date, currencyList):
    '''Print out a report on the exchange rates to the user.
    Args:
        baseCurrency (string): Base currency for which exchange rates should be provided.
        amount (int, NoneType): Amount of the base currency for which the exchange rate will be calculated.
        regionCode (int, NoneType): Internal code of the region for which the exchange rates will be calculated.
        worldwide (int, NoneType): Indicator if the most popular currencies will be appended to the list of currencies to be displayed.
        date (string): Date for which the exchange rates should be calculated.
        currencyList (list, NoneType): List of currencies for which the exchange rates should be calculated.
    '''
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
            # Skip printing out base currency.
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
