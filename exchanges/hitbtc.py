import json
import datetime
import hashlib
import hmac
import random
import string
import time
import requests

import tornado.gen
import models
from exchanges.common import Exchange
from settings.account import HITBTC

class Hitbtc(Exchange):
    def __init__(self):
        self._prefix = "https://api.hitbtc.com"

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
                    "amount":item[1]
                }
                new_orders.append(i)
        # print new_orders
        token_orders = models.order.Orders(token.lower(),new_orders)
        # print token_orders
        return token_orders

    def order(self,symbol, side, price,quantity):
        """/api/1/trading/new_order"""
        key = HITBTC["key"]
        secret = HITBTC["secret"]
        orderData = {'symbol':symbol, 'side': side, 'quantity': quantity, 'price': price }
        r = requests.post('https://api.hitbtc.com/api/2/order', data = orderData, auth=(key, secret))        
        print(r.json())
        # print result.body

if __name__ == "__main__":
    h = Hitbtc()
    h.order("SNCETH","buy",'0.00012','0.3')
    #print h.get_symbols()
