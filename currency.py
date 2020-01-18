import iso4217
from collections import defaultdict

class Currency:
    def __init__(self, code, name, region, exchangeRateToUSD):
        self.code = code
        self.name = name
        self.region = region
        self.exchangeRateToUSD = exchangeRateToUSD


    def getExchangeRate(self, otherCurrencyRate, amount):
        '''Calculate exchange rate between two currencies.
        Args:
            otherCurrencyRate (float): Exchange rate of other currency to USD.
            amount (int): Amount of the currency for which the exchange rate will be calculated.
        Returns:
            float: Exchange rate calculated between current currency and a base currency.
        '''
        return amount*self.exchangeRateToUSD/otherCurrencyRate


def getCurrencyList(data, region, worldwide):
    '''Get a list of all the available currencies or just from a specific region.
    Args:
        data (response): A response object from the GET request.
        region (int, NoneType): Region for which the currencies should be considered.
        worldwide (int, NoneType): Indicator if the most popular currencies will be appended to the list of currencies to be displayed.
    Returns:
        list: A list of currencies for which the exchange rates will be calculated.
    '''
    completeList = []
    regionalList = []
    shortlist = []

    for code, rate in data.json()["rates"].items():
        try:
            newCurrency = Currency(code, iso4217.currencies[code]["name"], iso4217.currencies[code]["region"], rate)
            completeList.append(newCurrency)
            if region is not None:
                if iso4217.currencies[code]["region"] == region:
                    regionalList.append(newCurrency)

            if worldwide is not None:
                if iso4217.currencies[code]["shortlist"] == 1:
                    shortlist.append(newCurrency)
        # Some obsolete currencies are not featured in the iso4217 dictionary.
        except KeyError:
            continue

    if region is not None:
        # Make sure to remove duplicate currencies.
        firstList = set(regionalList)
        secondList = set(shortlist)

        diffList = secondList - firstList

        completeList = regionalList + list(diffList)

    return completeList

def getSpecificCurrency(data, code):
    '''Get a specific currency object.
    Args:
        data (response): A response object from the GET request.
        code (string): An ISO 4217 code of the currency.
    Returns:
        Currency: Object representing the desired currency.
    '''
    currency = None

    for currencyCode, currencyRate in data.json()["rates"].items():
        if currencyCode == code:
            currency = Currency(code, iso4217.currencies[code]["name"], iso4217.currencies[code]["region"], currencyRate)
            break

    return currency
