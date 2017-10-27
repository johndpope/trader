import json
import models
from exchanges.common import Exchange

class Liqui(Exchange):
    def __init__(self):
        self._prefix = "https://api.liqui.io/api/3"

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
                    "amount":item[1]
                }
                new_orders.append(i)

        token_orders = models.order.Orders(token.lower(),new_orders)
        return token_orders
if __name__ == "__main__":
    b = Liqui()
    print b.get_symbols()