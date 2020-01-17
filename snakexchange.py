import requests
import iso4217
import auth
from currency import Currency
import argparse
import datetime
import report

def main():

    parser = argparse.ArgumentParser(description="SnakeXchange - A python currency conversion utility.")
    parser.add_argument("-b", "--base", default="USD", help="Base currency for comparison. Default is USD.", required=False)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--region", type=str, help="Name of the region for regional list.")
    group.add_argument("-r", type=int, help="Internal code of the region for regional list.")
    parser.add_argument("-w", "--worldwide", action="store_const", const=1, help="Append worlds most popular currencies to the regional list.", required=False)
    parser.add_argument("-d", "--date", help="Date of comparison of currencies in YYYY-MM-DD format. If blank, today's date.", required=False)
    parser.add_argument("-c", "--currency", help="Currency for direct conversion. If set, regional comparison is ignored.", required=False)


    args = parser.parse_args()

    if args.base:
        if args.base not in iso4217.currencies:
            parser.error("Invalid enter a valid ISO-4217 code.")

    if args.r and (args.r < 0 or args.r > 11):
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
        except ValueError:
            parser.error("Please enter a valid date in YYYY-MM-DD format.")

    baseCurrency = args.base
    regionCode = args.r
    region = args.region
    if args.date==None:
        date = "latest"
    worldwide = args.worldwide

    if args.currency:
        if args.currency not in iso4217.currencies:
            parser.error("Invalid enter a valid ISO-4217 code.")
        else:
            region = None
            regionCode = None
            worldwide = None
    currency = args.currency

    report.report(baseCurrency, regionCode, region, worldwide, date, currency)


if __name__ == "__main__":
    main()
