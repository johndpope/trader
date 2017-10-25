import json
import tornado.gen
import models
from exchanges.common import Exchange

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

