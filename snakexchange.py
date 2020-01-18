import iso4217
import argparse
import datetime
import report
import sys

def main():

    #sys.tracebacklimit = 0

    parser = argparse.ArgumentParser(description="SnakeXchange - A python currency conversion utility.", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-b", "--base", default="USD", help="Base currency for comparison. Default is USD.", required=False)
    parser.add_argument("-a", "--amount", type=int, default=1, help="Amount of money you are interested in exchanging.", required=False)
    parser.add_argument("-r", "--region", type=int, help="Internal number representing a region. Regions are based on the United Nations geoscheme. List of regional codes:\n1 - Europe\n2 - Western Asia\n3 - Central and Eastern Asia\n4 - South and Southeastern Asia\n5 - North and Central America\n6 - The Caribbean\n7 - South America\n8 - Oceania\n9 - North Africa\n10 - West and Central Africa\n11 - South and Eastern Africa\n0 - Non-regional Goods.")
    parser.add_argument("-w", "--worldwide", action="store_const", const=1, help="Append worlds most popular currencies to the regional list.", required=False)
    parser.add_argument("-d", "--date", help="Date of comparison of currencies in YYYY-MM-DD format. If ignored, today's date.", required=False)
    parser.add_argument("-c", "--currency", help="Currency, or list of coma separated currencies, for direct conversion. If set, regional comparison is ignored.", required=False)


    args = parser.parse_args()

    if args.base:
        if args.base not in iso4217.currencies:
            parser.error("Please enter a valid ISO-4217 code.")

    if args.region and (args.region < 0 or args.region > 11):
        parser.error("Unknown region code. Please consult the documentation.")

    if args.date:
        try:
            year, month, day = args.date.split("-")
            date = datetime.datetime(int(year), int(month), int(day))
            today = datetime.datetime.today()
            if date > today:
                parser.error("Future is changing and we can't be sure what it holds. Please enter a date before today's.")
            elif date == datetime.datetime(today.year, today.month, today.day):
                date = "latest"
            elif date < datetime.datetime(int(1999), int(1), int(1)):
                parser.error("Unfortunately, we are unable to provide data for such a distant past. Please try date from year of 1999 and forward.")
        except ValueError:
            parser.error("Please enter a valid date in YYYY-MM-DD format.")

    baseCurrency = args.base
    amount = args.amount
    regionCode = args.region
    if args.date is None:
        date = "latest"
    else:
        date = "historical/"+str(date.year)+"-"+"{:02d}".format(date.month)+"-"+"{:02d}".format(date.day)
    worldwide = args.worldwide

    if args.currency:
        currencyList = args.currency.split(",")
        for currency in currencyList:
            if currency.strip() not in iso4217.currencies:
                print(currency.strip())
                parser.error("Please enter a valid ISO-4217 code.")
        region = None
        regionCode = None
        worldwide = None

    report.report(baseCurrency, amount, regionCode, worldwide, date, currencyList)


if __name__ == "__main__":
    main()
