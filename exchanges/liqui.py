import json
import models
import hmac
import hashlib
import time
import requests
from exchanges.common import Exchange
from settings.account import LIQUI
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Liqui(Exchange):
    def __init__(self):
        self._prefix = "https://api.liqui.io/api/3"
        self._secret = LIQUI["secret"]
        self._key = LIQUI["key"]

    def _sign(self, data):
        if isinstance(data, dict):
            data = urlencode(data)
        return hmac.new(self._secret.encode(), data.encode(), hashlib.sha512).hexdigest()

    def get_symbols(self):
        url = self._prefix  + "/info"
        symbols = json.loads(self._fetch(url))["pairs"]
        raw_items = filter(lambda x:x.endswith("eth"), symbols.keys())
        return [ item[:-4].lower() for item in raw_items ]

    def get_token_orders(self, token):
        url = self._prefix + '/depth/' + token.lower() + "_eth"
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

    def get_balances(self):
        """/api/1/trading/new_order"""
        # key = HITBTC["key"]
        # secret = HITBTC["secret"]
        # orderData = {'symbol':symbol, 'side': side, 'quantity': quantity, 'price': price }
        # print orderData
        # https://api.liqui.io/api/3/<method name>/<pair listing>
        # pair = token + "_" + "eth"
        params = {
            "method":'getInfo'
            # "pair":pair, 
            # "type":side, 
            # "rate":price,
            # "amount":quantity
            }
        params.update(nonce=int(time.time()))
        headers = {'Key': self._key, 'Sign': self._sign(params)}
        # print "liqui",params
        resp = requests.post('https://api.liqui.io/tapi', data=params, headers=headers)
        # print resp
        data = resp.json()
        if 'error' in data:
            # raise LiquiApiError(data['error'])
            print data["error"]
        balances = data.get('return', data)
        ret = []
        try:
            for token, amount in balances["funds"].items():
                item = {}
                item["token"] = token.lower()
                item["amount"] = amount
                item["exchange"] = "liqui"
                ret.append(item)
        except:
            pass
        return ret

    def get_all_price(self):
        """use binance and hitbtc price"""
        url = 'https://api.hitbtc.com' + '/api/2/public/ticker'
        # url = self._prefix + '/api/v1/depth?symbol=' + token.upper() + "ETH"
        all_prices = json.loads(self._fetch(url))
        all_prices = filter(lambda x:x["symbol"].endswith("ETH"), all_prices )
        info = {}
        for token in all_prices:
            item = {}
            token_name = token["symbol"][:-3].lower()
            item["token"] = token_name
            item["price"] = token["bid"]
            item["exchange"] = "liqui"
            # info.append(item)
            info[token_name] = item
        # print info
        # return info

        url = 'https://www.binance.com' + '/api/v1/ticker/allPrices'
        # url = self._prefix + '/api/v1/depth?symbol=' + token.upper() + "ETH"
        all_prices = json.loads(self._fetch(url))
        all_prices = filter(lambda x:x["symbol"].endswith("ETH"), all_prices )
        # info = {}
        for token in all_prices:
            item = {}
            token_name = token["symbol"][:-3].lower()
            item["token"] = token_name
            item["price"] = token["price"]
            item["exchange"] = "liqui"
            # info.append(item)
            info[token_name] = item
        # print info
        return info

    def order(self,token, side, price,quantity):
        """/api/1/trading/new_order"""
        # key = HITBTC["key"]
        # secret = HITBTC["secret"]
        # orderData = {'symbol':symbol, 'side': side, 'quantity': quantity, 'price': price }
        # print orderData
        # https://api.liqui.io/api/3/<method name>/<pair listing>
        pair = token + "_" + "eth"
        params = {
            "method":'Trade', 
            "pair":pair, 
            "type":side, 
            "rate":price,
            "amount":quantity
            }
        params.update(nonce=int(time.time()))
        headers = {'Key': self._key, 'Sign': self._sign(params)}
        # print "liqui",params
        resp = requests.post('https://api.liqui.io/tapi', data=params, headers=headers)
        # print resp
        data = resp.json()
        if 'error' in data:
            # raise LiquiApiError(data['error'])
            print data["error"]
        return data.get('return', data)
if __name__ == "__main__":
    b = Liqui()
    print b.get_symbols()
    # print b.order("knc","buy","0.002",1)
    print b.get_balances()
