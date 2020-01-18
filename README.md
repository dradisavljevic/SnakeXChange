# SnakeXChange
Python package used for checking exchange rates of currencies worldwide using the [OpenExchangeRates API](https://docs.openexchangerates.org/).

It is possible to get exchange rates for a single currency, custom group of currencies or for a list of currencies from certain geographical regions. Groups of currencies are divided using the [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme#cite_note-Elborgh-WoytekNewiak2013-4), but some regions have been grouped together for convenience. Regions are as follow:

* 1 - Europe
* 2 - Western Asia
* 3 - Central and Eastern Asia
* 4 - South and South-eastern Asia
* 5 - North and Central America (Without the Caribbeans)
* 6 - Caribbeans
* 7 - South America
* 8 - Oceania (Australia, Melanesia, Polynesia, Micronesia and New Zealand)
* 9 - North Africa
* 10 - West and Central Africa
* 11 - East and Southern Africa
* 0 - For non regional goods such as gold and silver

Individual currencies can be accessed using their [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code.

## Dependencies
Package relies on the [request](https://requests.readthedocs.io/en/master/) package for communication with the API.

## Prerequisites

Project is written using python 3.7.3 with Pipenv as packaging tool. So before running the project, make sure your pip is up to date by running:

```
python3 -m pip install --user --upgrade pip
```

After that, install the pipenv with the following command:

```
pip install pipenv
```

Following successful installation, navigate to project's root and run:

```
pipenv install
```

This should install all the necessary packages.

After this it is necessary to obtain API key for the OpenExchangeRates API. Registering for a [free plan](https://openexchangerates.org/signup/free) should be sufficient, as it is highly unlikely the traffic within a month will ever exceed 1000. After that, creating auth.py file after the auth.template.py template is necessary, and setting the API key as the constants value. After this, you are all set to go

## Usage

After setting up, you can run the script using the

```
pipenv run python snakexchange.py
```

command. This will get a list of all the available currencies for today's date for the US Dollar (USD). For a more advanced usage, you can set the command line arguments. For example:

```
pipenv run python snakexchange.py -b=GBP
```

 Will provide exchange rates of all the available currencies for the Pound Sterling (GBP).

 It is possible to get exchange rate for a single currency by calling:

```
 pipenv run python snakexchange.py -b=GBP -c=UZS
```

This will get exchange rates of Pound Sterling to Uzbekistani som.

It is also possible to get historical exchange rates for the year of 1991 and after by calling:

```
 pipenv run python snakexchange.py -b=JPY -d=2001-04-03
```

This will get exchange rates for Japanese Yen on 3rd of April 2001. The date argument should be in YYYY-MM-DD format.

For a full list of arguments you can call:

```
 pipenv run python snakexchange.py -h
```
