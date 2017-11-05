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

    def get_all_price(self):
        url = self._prefix + '/api/v1/ticker/allPrices'
        # url = self._prefix + '/api/v1/depth?symbol=' + token.upper() + "ETH"
        all_prices = json.loads(self._fetch(url))
        all_prices = filter(lambda x:x["symbol"].endswith("ETH"), all_prices )
        info = []
        for token in all_prices:
            item = {}
            token_name = token["symbol"][:-4]
            item["token"] = token_name
            item["price"] = token["price"]
            info.append(item)
        print info
        return info

    def parser_order_items(self, token, response):
        orders = json.loads(response)
        new_orders = []
        try:
            for _type,values in orders.items():
                if _type not in ["bids", "asks"]:
                    continue
                for item in values:
                    i = {
                        "type":_type,
                        "price":item[0],
                        "amount":item[1],
                        "exchange":"binance"
                    }
                    new_orders.append(i)
        except:
            pass
        # print new_orders
        token_orders = models.order.Orders(token.lower(),new_orders)
        return token_orders
    def get_balances(self):
        """/account/getbalances
            {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.00002882'}
        """
        url = self._prefix + '/api/v3/account'
        query_string = 'timestamp=' + str(int(time.time()*1000))
        apisign = hmac.new(self._secret.encode(),
                              query_string,
                              hashlib.sha256).hexdigest()
        url = url + '?' + query_string + '&' + 'signature=' + apisign
        result = self._fetch(url, headers={"X-MBX-APIKEY":self._key})
        balances = json.loads(result)["balances"]
        # balances = filter(lambda x : float(x["free"]) >0 or float(x["locked"]) > 0, balances)
        ret = []
        for balance in balances:
            item = {}
            item["token"] = balance["asset"].lower()
            item["amount"] = balance["free"]
            item["exchange"] = "binance"
            ret.append(item)
        return ret

if __name__ == "__main__":
    b = Binance()
    print b.get_symbols()
    # print b.get_token_orders("eos")
    print b.get_all_price()