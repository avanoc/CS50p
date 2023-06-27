import json
import requests
import sys

quote = []
exceptions = (
    requests.RequestException,
    requests.ConnectionError,
    requests.HTTPError,
    requests.URLRequired,
    requests.TooManyRedirects,
    requests.ConnectTimeout,
    requests.ReadTimeout,
    requests.Timeout,
)

bitcoins = sys.argv[1]

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        for currency in response["bpi"]["USD"].values():
            quote.append(currency)
        price = quote[4] * float(bitcoins)
        print(f"${'{:0,.4f}'.format(price)}")

except exceptions:
        pass