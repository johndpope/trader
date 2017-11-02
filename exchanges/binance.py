import json
import models
import hmac
import hashlib
import time
# import requests
from exchanges.common import Exchange
from settings.account import BINANCE
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Binance(Exchange):
    """https://www.binance.com/api/v1/depth?symbol=LRCETH"""
    def __init__(self):
        self._prefix = "https://www.binance.com"
        self._secret = BINANCE["secret"]
        self._key = BINANCE["key"]

    def _sign(self, data):
        if isinstance(data, dict):
            data = urlencode(data)
        return hmac.new(self._secret.encode(), data.encode(), hashlib.sha512).hexdigest()

    def get_symbols(self):
        url = self._prefix  + "/api/v1/ticker/allPrices"
        symbols = [ item["symbol"] for item in json.loads(self._fetch(url)) ]
        raw_items = filter(lambda x:x.endswith("ETH"), symbols)
        return [ item[:-3].lower() for item in raw_items ]

    def get_token_orders(self, token):
        url = self._prefix + '/api/v1/depth?symbol=' + token.upper() + "ETH"
        return self._fetch(url)

    def parser_order_items(self, token, response):
        orders = json.loads(response).values()[0]
        new_orders = []
        for _type,values in orders.items():
            for item in values:
                i = {
                    "type":_type,
                    "price":item[0],
                    "amount":item[1],
                    "exchange":"liqui"
                }
                new_orders.append(i)

        token_orders = models.order.Orders(token.lower(),new_orders)
        return token_orders

if __name__ == "__main__":
    b = Binance()
    print b.get_symbols()
    print b.get_token_orders("eos")