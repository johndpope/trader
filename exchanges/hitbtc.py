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
        # key = HITBTC["key"]
        # secret = 
        data = {"currency":token, "amount":amount, "type":trans_type}
        r  = requests.post('https://api.hitbtc.com/api/2/account/transfer', data = data, auth=(self._key, self._secret)) 
        print r.json()

if __name__ == "__main__":
    h = Hitbtc()
    # h.order("SNCETH","buy",'0.00012','0.3')
    #print h.get_symbols()
