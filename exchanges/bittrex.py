import json
import time
import models
import hmac
import hashlib
from exchanges.common import Exchange
from settings.account import BITTREX

class Bittrex(Exchange):
    def __init__(self):
        self._prefix = "https://bittrex.com/api/v1.1/"
        self._key = BITTREX["key"]
        self._secret = BITTREX["secret"]

    def get_symbols(self):
        url = self._prefix  + "/public/getmarkets"
        symbols = json.loads(self._fetch(url))["result"]
        raw_items = filter(lambda x:x["BaseCurrency"] == "ETH", symbols)
        return [ item["MarketCurrency"].lower() for item in raw_items ]

    def get_token_orders(self, token):
        # url = self._prefix + '/depth/' + token.lower() + "_eth"
        url = self._prefix + '/public/getorderbook?market=ETH-{token}&type=both'.format(token = token.upper())
        return self._fetch(url)
    def parser_order_items(self, token, response):
        orders = json.loads(response)["result"]
        new_orders = []
        TYPE = {
            "buy":"bids",
            "sell":"asks"
        }
        for _type,values in orders.items():
            for item in values:
                i = {
                    "type":TYPE[_type],
                    "price":item["Rate"],
                    "amount":item["Quantity"]
                }
                new_orders.append(i)

        token_orders = models.order.Orders(token.lower(),new_orders)
        return token_orders
    def order(self,symbol, side, price,quantity):
        url = "/api/v1.1/market/buylimit?apikey={apikey}&market={market}&quantity={quantity}&rate={price}".format(apikey=apikey, market=market, quantity=quantity,price=price )
        apisign = hmac.new(self._secret.encode(),
                              url.encode(),
                              hashlib.sha512).hexdigest()
        apikey = ""
        result = self.post("http://api.hitbtc.com" + path, headers={"Api-Signature": signature}, data=newOrder)
        print result

    def get_balance(self):
        url = "https://bittrex.com/api/v1.1/account/getbalance?apikey={key}&currency=BTC&nonce={nonce}".format(key=self._key,nonce = int(time.time()))
        apisign = hmac.new(self._secret.encode(),
                              url.encode(),
                              hashlib.sha512).hexdigest()
        result = self._fetch(url, headers={"apisign":apisign})
        print result
if __name__ == "__main__":
    b = Bittrex()
    # print b.get_symbols()
    b.get_balance()
