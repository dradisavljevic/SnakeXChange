import iso4217
from collections import defaultdict

class Currency:
    def __init__(self, code, name, region, exchangeRateToUSD):
        self.code = code
        self.name = name
        self.region = region
        self.exchangeRateToUSD = exchangeRateToUSD


    def getExchangeRate(self, otherCurrencyRate):
        return otherCurrencyRate/self.exchangeRateToUSD


def getCurrencyList(data, region, worldwide):
    completeList = []
    europe = []
    westernAsia = []
    centralAndEasternAsia = []
    southAndSouthEasternAsia = []
    northAndCentralAmerica = []
    southAmerica = []
    carribean = []
    oceania = []
    northAfrica = []
    westernAndCentralAfrica = []
    easternAndSouthernAfrica = []
    nonRegional = []
    shortlist = []
    currencyLists = defaultdict(list)

    currencyLists: {
        0: nonRegional,
        1: europe,
        2: westernAsia,
        3: centralAndEasternAsia,
        4: southAndSouthEasternAsia,
        5: northAndCentralAmerica,
        6: carribean,
        7: southAmerica,
        8: oceania,
        9: northAfrica,
        10: westernAndCentralAfrica,
        11: easternAndSouthernAfrica
    }

    for code, rate in data.json()["rates"].items():
        try:
            newCurrency = Currency(code, iso4217.currencies[code]["name"], iso4217.currencies[code]["region"], rate)
            completeList.append(newCurrency)
            if region is not None:
                if iso4217.currencies[code]["region"] == region:
                    currencyLists[region].append(newCurrency)

            if worldwide is not None:
                if iso4217.currencies[code]["shortlist"] == 1:
                    shortlist.append(newCurrency)
        except KeyError:
            continue

    if region is not None:
        firstList = set(currencyLists[region])
        secondList = set(shortlist)

        diffList = secondList - firstList

        completeList = currencyLists[region] + list(diffList)

    return completeList
