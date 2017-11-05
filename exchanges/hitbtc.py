import json
import datetime
import hashlib
import hmac
import random
import string
import time
# import requests

import tornado.gen
import models
from exchanges.common import Exchange
from settings.account import HITBTC

class Hitbtc(Exchange):
    def __init__(self):
        self._prefix = "https://api.hitbtc.com"
        self._key = HITBTC["key"]
        self._secret = HITBTC["secret"]

    def get_symbols(self):
        url = self._prefix + '/api/2/public/symbol'
        symbols = json.loads(self._fetch(url))
        ret = filter(lambda x : x["quoteCurrency"] == "ETH", symbols)
        return [ item["baseCurrency"].lower() for item in ret ]

    def get_token_orders(self, token):
        url = self._prefix + '/api/1/public/' + token.upper() + 'ETH/orderbook'
        return self._fetch(url)

    def parser_order_items(self, token, response):
        orders = json.loads(response)
        new_orders = []
        for _type,values in orders.items():
            for item in values:
                i = {
                    "type":_type,
                    "price":item[0],
                    "amount":item[1],
                    "exchange":"hitbtc"
                }
                new_orders.append(i)
        # print new_orders
        token_orders = models.order.Orders(token.lower(),new_orders)
        # print token_orders
        return token_orders

    def order(self,token, side, price,quantity):
        import requests
        """/api/1/trading/new_order"""
        symbol = token + "eth"
        symbol = symbol.upper()
        key = HITBTC["key"]
        secret = HITBTC["secret"]
        orderData = {'symbol':symbol, 'side': side, 'quantity': quantity, 'price': price }
        print "hitbtc",orderData
        r = requests.post('https://api.hitbtc.com/api/2/order', data = orderData, auth=(key, secret))      
        print(r.json())
        # print result.body
    def transfer(self, token, amount, trans_type):
        import requests
        # key = HITBTC["key"]
        # secret = 
        data = {"currency":token, "amount":amount, "type":trans_type}
        r  = requests.post('https://api.hitbtc.com/api/2/account/transfer', data = data, auth=(self._key, self._secret)) 
        print r.json()

    def get_balances(self):
        import requests
        """/api/2/account/balance
        /api/2/trading/balance"""
        r = requests.get('https://api.hitbtc.com/api/2/trading/balance',auth=(self._key, self._secret))
        # print r
        balances1 = r.json()
        # balances1 = filter(lambda x : float(x["available"]) >0 or float(x["reserved"]) > 0, balances1)
        ret = []
        for balance in balances1:
            item = {}
            item["token"] = balance["currency"].lower()
            item["amount"] = balance["available"]
            item["exchange"] = "hitbtc"
            ret.append(item)
        return ret
    def get_all_price(self):
        url = self._prefix + '/api/2/public/ticker'
        # url = self._prefix + '/api/v1/depth?symbol=' + token.upper() + "ETH"
        all_prices = json.loads(self._fetch(url))
        all_prices = filter(lambda x:x["symbol"].endswith("ETH"), all_prices )
        info = {}
        for token in all_prices:
            item = {}
            token_name = token["symbol"][:-3].lower()
            item["token"] = token_name
            item["price"] = token["bid"]
            item["exchange"] = "hitbtc"
            # info.append(item)
            info[token_name] = item
        # print info
        return info
        # print balances1
        # r = requests.get('https://api.hitbtc.com/api/2/account/balance',auth=(self._key, self._secret))
        # balances2 = r.json()
        # balances2 = filter(lambda x : float(x["available"]) >0 or float(x["reserved"]) > 0, balances2)
        # print balances2

if __name__ == "__main__":
    h = Hitbtc()
    h.get_balances()
    # h.order("SNCETH","buy",'0.00012','0.3')
    #print h.get_symbols()
